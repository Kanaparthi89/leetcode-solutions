
#!/usr/bin/env python3

import json
import os
import re
import time
from pathlib import Path

import requests

URL = "https://leetcode.com/graphql/"
STATE_FILE = Path(".leetcode_synced.json")

LANG_EXTENSION = {
    "python3": "py",
    "python": "py",
    "java": "java",
    "cpp": "cpp",
    "c": "c",
    "csharp": "cs",
    "javascript": "js",
    "typescript": "ts",
    "kotlin": "kt",
    "swift": "swift",
    "golang": "go",
    "ruby": "rb",
    "rust": "rs",
    "php": "php",
    "mysql": "sql",
}


def gql(query, variables, cookies):
    r = requests.post(
        URL,
        json={"query": query, "variables": variables},
        cookies=cookies,
        headers={
            "Content-Type": "application/json",
            "Referer": "https://leetcode.com",
            "User-Agent": "Mozilla/5.0",
        },
        timeout=30,
    )
    r.raise_for_status()
    data = r.json()

    if "errors" in data:
        raise RuntimeError(data["errors"])

    return data["data"]


def recent_submissions(username, cookies):
    query = """
    query($username: String!, $limit: Int!) {
        recentAcSubmissionList(username: $username, limit: $limit) {
            id
            titleSlug
        }
    }
    """
    return gql(query, {"username": username, "limit": 20}, cookies)[
        "recentAcSubmissionList"
    ] or []


def question_data(slug, cookies):
    query = """
    query($slug: String!) {
        question(titleSlug: $slug) {
            questionFrontendId
            title
            difficulty
            topicTags { name }
            content
        }
    }
    """
    return gql(query, {"slug": slug}, cookies)["question"]


def submission_data(submission_id, cookies, csrf):
    query = """
    query($id: Int!) {
        submissionDetails(submissionId: $id) {
            code
            lang { name }
        }
    }
    """
    return gql(
        query,
        {"id": int(submission_id)},
        cookies,
    )["submissionDetails"]


def slugify(text):
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def main():
    username = os.environ["LEETCODE_USERNAME"]
    session = os.environ["LEETCODE_SESSION"]
    csrf = os.environ["LEETCODE_CSRF_TOKEN"]

    cookies = {
        "LEETCODE_SESSION": session,
        "csrftoken": csrf,
    }

    synced = set(json.loads(STATE_FILE.read_text())) if STATE_FILE.exists() else set()
    count = 0

    for sub in recent_submissions(username, cookies):
        sub_id = sub["id"]

        if sub_id in synced:
            continue

        slug = sub["titleSlug"]
        question = question_data(slug, cookies)

        if not question:
            print(f"Skipping {slug}: question not found")
            continue

        details = submission_data(sub_id, cookies, csrf)

        if not details or not details.get("lang"):
            print(f"Skipping {slug}: language information missing")
            continue

        language = details["lang"].get("name")

        if not language:
            print(f"Skipping {slug}: language information missing")
            continue

        extension = LANG_EXTENSION.get(language.lower(), "txt")
        tags = question.get("topicTags") or []
        topic = slugify(tags[0]["name"]) if tags else "uncategorized"

        problem_id = str(question["questionFrontendId"]).zfill(4)
        folder = Path(topic) / f"{problem_id}-{slug}"
        folder.mkdir(parents=True, exist_ok=True)

        (folder / f"solution.{extension}").write_text(
            details.get("code", ""),
            encoding="utf-8",
        )

        tag_names = ", ".join(t["name"] for t in tags) or "None"

        readme = f"""# {problem_id}. {question["title"]}

**Difficulty:** {question["difficulty"]}

**Tags:** {tag_names}

**Language:** {language}

**Link:** https://leetcode.com/problems/{slug}/
"""

        (folder / "README.md").write_text(readme, encoding="utf-8")

        synced.add(sub_id)
        count += 1

        print(f"Synced: {topic}/{problem_id}-{slug}")
        time.sleep(1)

    STATE_FILE.write_text(json.dumps(sorted(synced, key=str), indent=2))
    print(f"Done. {count} new solution(s) synced.")


if __name__ == "__main__":
    main()

