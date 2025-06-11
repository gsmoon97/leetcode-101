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
├── create_problem.sh        ← scaffold generator
├── generate_readme.py       ← readme generator
├── update_submission.py     ← submission updater
├── requirements.txt         ← Python dependencies
└── README.md                ← this file
```

---

## 📊 Statistics

### Overall

- Total Problems Solved: 11
- Average Runtime: 13.55 ms
- Average Memory: 19.27 MB
- Average Time Percentile: 79.37%
- Average Memory Percentile: 55.47%

### Difficulty Breakdown

| Difficulty | Count |
|------------|-------|
| Easy | 10 |
| Medium | 1 |

### Top Tags

| Tag | Count |
|-----|-------|
| array | 4 |
| depth-first-search | 4 |
| tree | 3 |
| binary-tree | 3 |
| string | 3 |
| breadth-first-search | 2 |
| hash-table | 2 |
| matrix | 1 |
| dynamic-programming | 1 |
| binary-search-tree | 1 |

### Languages Used

| Language | Count |
|----------|-------|
| Python3 | 11 |
### Overall

- Total Problems Solved: 10
- Average Runtime: 14.60 ms
- Average Memory: 19.30 MB
- Average Time Percentile: 80.60%
- Average Memory Percentile: 58.30%

### Difficulty Breakdown

| Difficulty | Count |
|------------|-------|
| Easy | 9 |
| Medium | 1 |

### Top Tags

| Tag | Count |
|-----|-------|
| array | 4 |
| depth-first-search | 3 |
| string | 3 |
| breadth-first-search | 2 |
| tree | 2 |
| binary-tree | 2 |
| hash-table | 2 |
| matrix | 1 |
| dynamic-programming | 1 |
| binary-search-tree | 1 |

### Languages Used

| Language | Count |
|----------|-------|
| Python3 | 10 |
## 🛠  Prerequisites

| Tool | Purpose | Install (macOS) |
|------|---------|-----------------|
| **Python 3.8+** | run scripts & code | `brew install python` |
| **jq** | JSON CLI edits | `brew install jq` |
| **tree** | nice directory printouts (used in `create_problem.sh`) | `brew install tree` |

*(On Linux, replace `brew` with your package manager; on Windows, Scoop or WSL can do the same.)*

---

## 🚀  Workflow

1. **Create a new scaffold**

   ```bash
   ./create_problem.sh 123 "Best Time to Buy and Sell Stock" https://leetcode.com/problems/best-time-to-buy-and-sell-stock
   # → 0123-best-time-to-buy-and-sell-stock/
   ```

2. **Solve the problem**  
   Paste your final accepted code into `solution.py`.

3. **Record submission stats**  
   Edit `submission.json` with runtime, memory, percentiles, etc.

4. **Generate the folder-level README**

   ```bash
   python generate_readme.py 0123-best-time-to-buy-and-sell-stock
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

Copy this directory whenever you start a new problem—our `create_problem.sh` does the copying and placeholder replacement for you.

---

## ⚙️  Helper Scripts

| Script | Description |
|--------|-------------|
| `create_problem.sh` | Scaffolds a new problem folder from `.template-problem`. |
| `generate_readme.py` | Builds/refreshes the per-problem `README.md` using JSON metadata. |

Both live in the repo root for easy access.