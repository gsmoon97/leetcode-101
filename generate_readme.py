#!/usr/bin/env python3
"""
generate_readme.py

Build/refresh a per-problem README.md by merging `prompt.json`, `submission.json`,
and the solution file (first file that matches 'solution.*').

Usage:
    python generate_readme.py <problem_directory>

Example:
    python generate_readme.py 0146-lru-cache
"""

import json
import sys
import datetime
from pathlib import Path
import glob

def load_json(path: Path) -> dict:
    if not path.exists():
        sys.exit(f"✘ Missing file: {path}")
    try:
        return json.loads(path.read_text(encoding='utf-8'))
    except json.JSONDecodeError as e:
        sys.exit(f"✘ JSON error in {path}: {e}")

def friendly_table(mapping):
    # Generate header row
    header = "| " + " | ".join(mapping.keys()) + " |"
    # Generate separator row
    separator = "| " + " | ".join(["---"] * len(mapping)) + " |"
    # Generate data row
    data = "| " + " | ".join(str(v) for v in mapping.values()) + " |"
    # Combine all rows
    return "\n".join([header, separator, data])

def main():
    if len(sys.argv) < 2:
        sys.exit("Usage: python generate_readme.py <problem_directory>")
    dir_path = Path(sys.argv[1]).expanduser().resolve()
    if not dir_path.is_dir():
        sys.exit(f"✘ Directory not found: {dir_path}")

    prompt_path = dir_path / "prompt.json"
    sub_path    = dir_path / "submission.json"

    prompt = load_json(prompt_path)
    sub    = load_json(sub_path)

    # detect solution file (solution.py / solution.cpp / etc.)
    sol_files = list(dir_path.glob("solution.*"))
    if not sol_files:
        sys.exit("✘ No solution.* file found inside directory.")
    solution_file = sol_files[0]
    code_content  = solution_file.read_text(encoding='utf-8')
    code_lang     = {
        '.py': 'python',
        '.cpp': 'cpp',
        '.java': 'java',
        '.js': 'javascript',
        '.ts': 'typescript',
        '.cs': 'csharp',
    }.get(solution_file.suffix, '')

    readme_content = f"""# {prompt['id']:04d} · {prompt['title']}

{friendly_table({
    'Difficulty': prompt.get('difficulty', 'Unrated'),
    'Tags': ' · '.join(prompt.get('tags', [])) or '–',
    'Latest submission': f"**{sub.get('language','?')}** · {sub.get('runtime_ms', '?')} ms · {sub.get('memory_mb', '?'):.1f} MB" if sub.get('memory_mb') else '–',
    'Last updated': datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')
})}

---

## Problem Statement
{prompt.get('url','–')}

---

## Approach
{sub.get('approach','-')}

---

## Complexity
| | Time | Space |
|---|---|---|
| Solution | {sub.get('time_complexity','N/A')} | {sub.get('space_complexity','N/A')} |

---

## Code

```{code_lang}
{code_content}
```

---

## Submission Stats
{friendly_table({
    'Runtime': f"{sub.get('runtime_ms','?')} ms",
    'Memory': f"{sub.get('memory_mb','?'):.1f} MB" if sub.get('memory_mb') else '?',
    'Beats': f"{sub.get('time_percentile','?')} % time · {sub.get('memory_percentile','?')} % memory"
})}
"""

    (dir_path / "README.md").write_text(readme_content.strip() + "\n", encoding='utf-8')
    print(f"✅ README generated at {dir_path / 'README.md'}")

if __name__ == "__main__":
    main()
