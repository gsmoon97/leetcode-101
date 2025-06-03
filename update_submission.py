
#!/usr/bin/env python3
"""update_submission.py

Fetch a LeetCode submission page and write the key statistics into
<problem_dir>/submission.json.

Required packages:
    pip install requests beautifulsoup4

Usage:
    python update_submission.py \
           https://leetcode.com/problems/two-sum/submissions/1651054846 \
           0001-two-sum

The script extracts:
    * timestamp        (UTC ISO‑8601)
    * language
    * runtime_ms
    * memory_kb
    * time_percentile
    * memory_percentile

The JSON schema matches what generate_readme.py expects.
"""

import re
import json
import sys
import datetime
from pathlib import Path
from typing import Optional

import requests
from bs4 import BeautifulSoup

FIELD_PATTERNS = {
    "runtime_ms":       re.compile(r"Runtime\s*\n\s*(\d+)\s*ms"),
    "memory_kb":        re.compile(r"Memory\s*\n\s*([\d\.]+)\s*MB"),
    "language":         re.compile(r"Language\s*\n\s*([A-Za-z0-9+#]+)"),
    "time_percentile":  re.compile(r"Runtime\s*\n\s*\d+\s*ms\s*\n\s*Beats\s*\n\s*([\d\.]+)%"),
    "memory_percentile":re.compile(r"Memory\s*\n\s*[\d\.]+\s*MB\s*\n\s*Beats\s*\n\s*([\d\.]+)%"),
    "submitted_at":     re.compile(r"Submitted\s*on\s*([A-Za-z]{3}\s+\d{1,2},\s+\d{4}\s+\d{2}:\d{2})")
}

def scrape_submission(url: str) -> dict:
    """Return dict with extracted stats."""
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64)"
    }
    resp = requests.get(url, headers=headers, timeout=10)
    resp.raise_for_status()
    html = resp.text

    soup = BeautifulSoup(html, "html.parser")
    text = soup.get_text(separator="\n")

    data = {}
    for key, pattern in FIELD_PATTERNS.items():
        m = pattern.search(text)
        if m:
            data[key] = m.group(1)

    # Convert numeric fields
    if "runtime_ms" in data:
        data["runtime_ms"] = int(data["runtime_ms"])
    if "memory_kb" in data:
        # convert MB to KB
        data["memory_kb"] = int(float(data["memory_kb"]) * 1024)

    if "time_percentile" in data:
        data["time_percentile"] = float(data["time_percentile"])
    if "memory_percentile" in data:
        data["memory_percentile"] = float(data["memory_percentile"])

    # timestamp convert to ISO
    if "submitted_at" in data:
        ts = datetime.datetime.strptime(data["submitted_at"], "%b %d, %Y %H:%M")
        data["timestamp"] = ts.isoformat() + "Z"
        del data["submitted_at"]
    else:
        data["timestamp"] = datetime.datetime.utcnow().isoformat() + "Z"

    return data

def merge_submission(problem_dir: Path, new_data: dict):
    sub_path = problem_dir / "submission.json"
    if sub_path.exists():
        try:
            current = json.loads(sub_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            current = {}
    else:
        current = {}

    current.update(new_data)
    sub_path.write_text(json.dumps(current, indent=4), encoding="utf-8")
    print(f"✅ Updated {sub_path}")

def main():
    if len(sys.argv) != 3:
        print("Usage: python update_submission.py <submission_url> <problem_dir>")
        sys.exit(1)

    url = sys.argv[1]
    dir_path = Path(sys.argv[2]).expanduser().resolve()
    if not dir_path.is_dir():
        print(f"Error: {dir_path} is not a directory")
        sys.exit(1)

    print("Fetching submission page …")
    data = scrape_submission(url)
    merge_submission(dir_path, data)

if __name__ == "__main__":
    main()
