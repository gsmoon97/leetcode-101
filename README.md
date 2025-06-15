# LeetCode-101 📚

A well-organized, self-contained archive of accepted LeetCode solutions, with each problem neatly stored in its own dedicated folder.

```
<root>/
│
├── .template-problem/      ← reusable blueprint (do not edit)
│   ├── prompt.json         ← problem metadata
│   ├── submission.json     ← submission metrics
│   ├── solution.py         ← solution template
│   └── README.md           ← readme template
│
├── 0001-two-sum/           ← example problem folder
│   ├── prompt.json
│   ├── submission.json
│   ├── solution.py
│   └── README.md
│
├── init.sh                ← scaffold generator
├── gen_readme.py          ← readme generator
├── get_stats.py           ← statistics updater
├── update_submission.py   ← submission updater
├── requirements.txt       ← Python dependencies
└── README.md              ← this file
```

---

## 📊 Statistics

### Overall

- Total Problems Solved: 18
- Average Runtime: 14.17 ms
- Average Memory: 19.95 MB
- Average Time Percentile: 73.29%
- Average Memory Percentile: 56.76%

### Difficulty Breakdown

| Difficulty | Count |
|------------|-------|
| Easy | 17 |
| Medium | 1 |

### Top Tags

| Tag | Count |
|-----|-------|
| string | 5 |
| array | 4 |
| depth-first-search | 4 |
| hash-table | 4 |
| tree | 3 |
| binary-tree | 3 |
| linked-list | 3 |
| breadth-first-search | 2 |
| dynamic-programming | 2 |
| recursion | 2 |

### Languages Used

| Language | Count |
|----------|-------|
| Python3 | 18 |

---

## 🛠  Prerequisites

| Tool | Purpose | Install (macOS) |
|------|---------|-----------------|
| **Python 3.8+** | run scripts & code | `brew install python` |
| **jq** | JSON CLI edits | `brew install jq` |
| **tree** | nice directory printouts (used in `init.sh`) | `brew install tree` |

*(On Linux, replace `brew` with your package manager; on Windows, Scoop or WSL can do the same.)*

---

## 🚀  Workflow

1. **Create a new scaffold**

   ```bash
   ./init.sh 123 "Best Time to Buy and Sell Stock" https://leetcode.com/problems/best-time-to-buy-and-sell-stock
   # → 0123-best-time-to-buy-and-sell-stock/
   ```

2. **Solve the problem**  
   Paste your final accepted code into `solution.py`.

3. **Record submission stats**  
   Edit `submission.json` with runtime, memory, percentiles, etc.

4. **Generate the folder-level README**

   ```bash
   python gen_readme.py 0123-best-time-to-buy-and-sell-stock
   ```

5. **Commit**

   ```bash
   git add 0123-best-time-to-buy-and-sell-stock
   git commit -m "[LeetCode] 0123 – Buy/Sell Stock ✅ Python solution, 47 ms"
   ```

---

## 📁  Folder Blueprint (`.template-problem/`)

| File | Description |
|------|-------------|
| `prompt.json` | Static metadata about the problem (id, title, URL, tags). |
| `submission.json` | Latest submission metrics (timestamp, language, runtime, memory, approach). |
| `solution.*` | Exactly **one** source file representing the latest accepted solution. |
| `README.md` | Auto-generated summary combining the two JSON files + code. |

Copy this directory whenever you start a new problem—our `init.sh` does the copying and placeholder replacement for you.

---

## ⚙️  Helper Scripts

| Script | Description |
|--------|-------------|
| `init.sh` | Scaffolds a new problem folder from `.template-problem`. |
| `gen_readme.py` | Builds/refreshes the per-problem `README.md` using JSON metadata. |
| `get_stats.py` | Updates the root-level README.md with overall statistics (problems solved, runtime, memory, etc.). |
| `update_submission.py` | Updates submission metrics in problem folders. |

All scripts live in the repo root for easy access.

---

## 🔧 Git Hooks

To automatically update the root-level README.md whenever problem files are modified, add this pre-commit hook:

```bash
#!/bin/sh

# Check if any problem folders were modified
if git diff --cached --name-only | grep -E '^[0-9]+-.*/.*\.(json|py)$' > /dev/null; then
    echo "Updating README.md with latest statistics..."
    python3 get_stats.py
    git add README.md
fi
```

Save this as `.git/hooks/pre-commit` and make it executable with `chmod +x .git/hooks/pre-commit`.