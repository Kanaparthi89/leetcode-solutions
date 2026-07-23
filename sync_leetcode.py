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
    "python3": "py", "python": "py", "java": "java", "c": "c", "cpp": "cpp",
    "csharp": "cs", "javascript": "js", "typescript": "ts", "kotlin": "kt",
    "swift": "swift", "golang": "go", "ruby": "rb", "scala": "scala",
    "rust": "rs", "php": "php", "mysql": "sql", "racket": "rkt",
    "erlang": "erl", "elixir": "ex", "dart": "dart",
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
    data = gql(query, {"username": username, "limit": limit}, cookies)
    return data["recentAcSubmissionList"]


def get_question_meta(title_slug, cookies):
    query = """
    query questionData($titleSlug: String!) {
      question(titleSlug: $titleSlug) {
        questionFrontendId
        title
        titleSlug
        difficulty
        topicTags { name slug }
        content
      }
    }
    """
    data = gql(query, {"titleSlug": title_slug}, cookies)
    return data["question"]


def get_submission_code(submission_id, cookies, csrf_token):
    query = """
    query submissionDetails($submissionId: Int!) {
      submissionDetails(submissionId: $submissionId) {
        code
        lang { name }
      }
    }
    """
    data = gql(
        query,
        {"submissionId": int(submission_id)},
        cookies,
        extra_headers={"x-csrftoken": csrf_token},
    )
    return data["submissionDetails"]


def slugify(text):
    text = text.strip().lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")


def strip_html(html):
    text = re.sub(r"<[^>]+>", "", html or "")
    return text.strip()


def load_state():
    if STATE_FILE.exists():
        return set(json.loads(STATE_FILE.read_text()))
    return set()


def save_state(synced_ids):
    STATE_FILE.write_text(json.dumps(sorted(synced_ids, key=str), indent=2))


def main():
    username = os.environ["LEETCODE_USERNAME"]
    session = os.environ["LEETCODE_SESSION"]
    csrf_token = os.environ["LEETCODE_CSRF_TOKEN"]
    cookies = {"LEETCODE_SESSION": session, "csrftoken": csrf_token}

    synced = load_state()
    recent = get_recent_accepted(username, cookies, limit=20)

    new_count = 0
    for sub in recent:
        sub_id = sub["id"]
        if sub_id in synced:
            continue

        title_slug = sub["titleSlug"]
        question = get_question_meta(title_slug, cookies)
        tags = question.get("topicTags") or []
        primary_tag = slugify(tags[0]["name"]) if tags else "uncategorized"

        details = get_submission_code(sub_id, cookies, csrf_token)
        lang_name = details["lang"]["name"].lower()
        ext = LANG_EXTENSION.get(lang_name, "txt")

        problem_id = question["questionFrontendId"].zfill(4)
        folder_name = f"{problem_id}-{title_slug}"
        target_dir = REPO_ROOT / primary_tag / folder_name
        target_dir.mkdir(parents=True, exist_ok=True)

        (target_dir / f"solution.{ext}").write_text(details["code"])

        all_tags = ", ".join(t["name"] for t in tags) if tags else "None"
        readme = (
            f"# {problem_id}. {question['title']}\n\n"
            f"**Difficulty:** {question['difficulty']}\n\n"
            f"**Tags:** {all_tags}\n\n"
            f"**Link:** https://leetcode.com/problems/{title_slug}/\n\n"
            f"---\n\n{strip_html(question.get('content', ''))[:2000]}\n"
        )
        (target_dir / "README.md").write_text(readme)

        synced.add(sub_id)
        new_count += 1
        print(f"Synced: {primary_tag}/{folder_name}")
        time.sleep(1)  # be polite to the API

    save_state(synced)
    print(f"Done. {new_count} new solution(s) synced.")


if __name__ == "__main__":
    main()
