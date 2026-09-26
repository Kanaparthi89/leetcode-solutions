```python
#!/usr/bin/env python3
"""
LeetCode -> GitHub topic-based sync.

Fetches your recent Accepted submissions, looks up each problem's topic
tags (Binary Search, String, Array, Dynamic Programming, ...), and writes
the solution into a folder named after the primary tag, e.g.:

    binary-search/0704-binary-search/solution.py
    string/0125-valid-palindrome/solution.py

Keeps a record of already-synced submission ids in `.leetcode_synced.json`
so re-runs don't duplicate work.

Required environment variables (set as GitHub Actions secrets):
    LEETCODE_USERNAME   - your LeetCode username (from your profile URL)
    LEETCODE_SESSION    - the LEETCODE_SESSION cookie value
    LEETCODE_CSRF_TOKEN - the csrftoken cookie value
"""

import json
import os
import re
import time
from pathlib import Path

import requests

GRAPHQL_URL = "https://leetcode.com/graphql/"
STATE_FILE = Path(".leetcode_synced.json")
REPO_ROOT = Path(".")

LANG_EXTENSION = {
    "python3": "py",
    "python": "py",
    "java": "java",
    "c": "c",
    "cpp": "cpp",
    "csharp": "cs",
    "javascript": "js",
    "typescript": "ts",
    "kotlin": "kt",
    "swift": "swift",
    "golang": "go",
    "ruby": "rb",
    "scala": "scala",
    "rust": "rs",
    "php": "php",
    "mysql": "sql",
    "racket": "rkt",
    "erlang": "erl",
    "elixir": "ex",
    "dart": "dart",
}


def gql(query, variables, cookies, extra_headers=None):
    headers = {
        "Content-Type": "application/json",
        "Referer": "https://leetcode.com",
        "User-Agent": "Mozilla/5.0",
    }

    if extra_headers:
        headers.update(extra_headers)

    resp = requests.post(
        GRAPHQL_URL,
        json={"query": query, "variables": variables},
        headers=headers,
        cookies=cookies,
        timeout=30,
    )

    resp.raise_for_status()

    data = resp.json()

    if "errors" in data:
        raise RuntimeError(data["errors"])

    return data["data"]


def get_recent_accepted(username, cookies, limit=20):
    query = """
    query recentAcSubmissions($username: String!, $limit: Int!) {
      recentAcSubmissionList(username: $username, limit: $limit) {
        id
        title
        titleSlug
        timestamp
      }
    }
    """

    data = gql(
        query,
        {
            "username": username,
            "limit": limit,
        },
        cookies,
    )

    return data.get("recentAcSubmissionList") or []


def get_question_meta(title_slug, cookies):
    query = """
    query questionData($titleSlug: String!) {
      question(titleSlug: $titleSlug) {
        questionFrontendId
        title
        titleSlug
        difficulty
        topicTags {
          name
          slug
        }
        content
      }
    }
    """

    data = gql(
        query,
        {
            "titleSlug": title_slug,
        },
        cookies,
    )

    return data.get("question")


def get_submission_code(submission_id, cookies, csrf_token):
    query = """
    query submissionDetails($submissionId: Int!) {
      submissionDetails(submissionId: $submissionId) {
        code
        lang {
          name
        }
      }
    }
    """

    data = gql(
        query,
        {
            "submissionId": int(submission_id),
        },
        cookies,
        extra_headers={
            "x-csrftoken": csrf_token,
        },
    )

    return data.get("submissionDetails")


def slugify(text):
    text = text.strip().lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")


def strip_html(html):
    text = re.sub(r"<[^>]+>", "", html or "")
    return text.strip()


def load_state():
    if STATE_FILE.exists():
        try:
            return set(json.loads(STATE_FILE.read_text()))
        except (json.JSONDecodeError, OSError):
            print("Warning: Could not read state file. Starting with empty state.")
            return set()

    return set()


def save_state(synced_ids):
    STATE_FILE.write_text(
        json.dumps(
            sorted(synced_ids, key=str),
            indent=2,
        )
    )


def main():
    username = os.environ["LEETCODE_USERNAME"]
    session = os.environ["LEETCODE_SESSION"]
    csrf_token = os.environ["LEETCODE_CSRF_TOKEN"]

    cookies = {
        "LEETCODE_SESSION": session,
        "csrftoken": csrf_token,
    }

    synced = load_state()

    recent = get_recent_accepted(
        username,
        cookies,
        limit=20,
    )

    new_count = 0

    for sub in recent:
        sub_id = sub.get("id")

        if not sub_id:
            print("Skipping submission: submission id is missing")
            continue

        if sub_id in synced:
            continue

        title_slug = sub.get("titleSlug")

        if not title_slug:
            print(f"Skipping submission {sub_id}: title slug is missing")
            continue

        # Get problem metadata
        question = get_question_meta(
            title_slug,
            cookies,
        )

        if not question:
            print(
                f"Skipping submission {sub_id}: "
                f"question data is missing"
            )
            continue

        tags = question.get("topicTags") or []

        primary_tag = (
            slugify(tags[0]["name"])
            if tags and tags[0].get("name")
            else "uncategorized"
        )

        # Get submitted solution
        details = get_submission_code(
            sub_id,
            cookies,
            csrf_token,
        )

        # Prevent crash if LeetCode returns no submission details
        if not details:
            print(
                f"Skipping submission {sub_id}: "
                f"submission details are missing"
            )
            continue

        # Prevent crash if LeetCode returns lang: null
        lang = details.get("lang")

        if not lang or not lang.get("name"):
            print(
                f"Skipping submission {sub_id}: "
                f"language information is missing"
            )
            continue

        lang_name = lang["name"].lower()
        ext = LANG_EXTENSION.get(lang_name, "txt")

        code = details.get("code")

        if code is None:
            print(
                f"Skipping submission {sub_id}: "
                f"solution code is missing"
            )
            continue

        frontend_id = question.get("questionFrontendId")

        if not frontend_id:
            print(
                f"Skipping submission {sub_id}: "
                f"problem ID is missing"
            )
            continue

        problem_id = str(frontend_id).zfill(4)

        title = question.get("title") or sub.get("title") or title_slug

        folder_name = f"{problem_id}-{title_slug}"

        target_dir = (
            REPO_ROOT
            / primary_tag
            / folder_name
        )

        target_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

        # Write solution
        solution_file = target_dir / f"solution.{ext}"

        solution_file.write_text(
            code,
            encoding="utf-8",
        )

        # Build README
        all_tags = (
            ", ".join(
                t["name"]
                for t in tags
                if t.get("name")
            )
            if tags
            else "None"
        )

        difficulty = question.get("difficulty") or "Unknown"

        problem_content = strip_html(
            question.get("content", "")
        )

        readme = (
            f"# {problem_id}. {title}\n\n"
            f"**Difficulty:** {difficulty}\n\n"
            f"**Tags:** {all_tags}\n\n"
            f"**Language:** {lang['name']}\n\n"
            f"**Link:** "
            f"https://leetcode.com/problems/{title_slug}/\n\n"
            f"---\n\n"
            f"{problem_content[:2000]}\n"
        )

        (target_dir / "README.md").write_text(
            readme,
            encoding="utf-8",
        )

        # Mark as synced only after successful file creation
        synced.add(sub_id)
        new_count += 1

        print(
            f"Synced: {primary_tag}/{folder_name} "
            f"[{lang['name']}]"
        )

        # Be polite to the API
        time.sleep(1)

    save_state(synced)

    print(
        f"Done. {new_count} new solution(s) synced."
    )


if __name__ == "__main__":
    main()
```
