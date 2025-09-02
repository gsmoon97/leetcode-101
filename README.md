# LeetCode-101 📚

A well-organized, self-contained archive of accepted LeetCode solutions, with each problem neatly stored in its own dedicated folder.

```
<root>/
│
├── problems/               ← all LeetCode problems
│   ├── .template-problem/  ← reusable blueprint (do not edit)
│   │   ├── prompt.json     ← problem metadata
│   │   ├── submission.json ← submission metrics
│   │   ├── solution.py     ← solution template
│   │   └── README.md       ← readme template
│   │
│   ├── 0001-two-sum/       ← example problem folder
│   │   ├── prompt.json
│   │   ├── submission.json
│   │   ├── solution.py
│   │   └── README.md
│   └── ...
│
├── init.sh                ← scaffold generator
├── gemini_init.py         ← AI-powered scaffold generator
├── gen_readme.py          ← readme generator
├── get_stats.py           ← statistics updater
├── requirements.txt       ← Python dependencies
└── README.md              ← this file
```

---

## 📊 Statistics

### Overall

- Total Problems Solved: 37
- Average Runtime: 49.76 ms
- Average Memory: 21.66 MB
- Average Time Percentile: 67.65%
- Average Memory Percentile: 54.43%

### Difficulty Breakdown

| Difficulty | Count |
|------------|-------|
| Easy | 23 |
| Medium | 14 |

### Top Tags

| Tag | Count |
|-----|-------|
| array | 14 |
| hash-table | 10 |
| string | 9 |
| breadth-first-search | 8 |
| depth-first-search | 8 |
| dynamic-programming | 6 |
| tree | 6 |
| binary-tree | 6 |
| sorting | 5 |
| math | 4 |

### Languages Used

| Language | Count |
|----------|-------|
| Python3 | 37 |

---

## 🛠  Prerequisites

| Tool | Purpose | Install (macOS) |
|------|---------|-----------------|
| **Python 3.8+** | run scripts & code | `brew install python` |
| **jq** | JSON CLI edits | `brew install jq` |
| **tree** | nice directory printouts (used in `init.sh`) | `brew install tree` |

*(On Linux, replace `brew` with your package manager; on Windows, Scoop or WSL can do the same.)*

### AI Setup (for `gemini_init.py`)

1. **Install AI dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up Gemini API key:**
   ```bash
   # Create .env file with your Google API key
   echo "GOOGLE_API_KEY=your_google_api_key_here" > .env
   ```
   
   Get your API key from [Google AI Studio](https://makersuite.google.com/app/apikey)

---

## 🚀  Workflow

1. **Create a new scaffold**

   **Option A: AI-Powered (Recommended)**
   ```bash
   python gemini_init.py https://leetcode.com/problems/best-time-to-buy-and-sell-stock
   # → problems/0123-best-time-to-buy-and-sell-stock/ (with auto-populated metadata)
   ```
   
   **Option B: Manual**
   ```bash
   ./init.sh 123 "Best Time to Buy and Sell Stock" https://leetcode.com/problems/best-time-to-buy-and-sell-stock
   # → problems/0123-best-time-to-buy-and-sell-stock/ (requires manual metadata entry)
   ```

2. **Solve the problem**  
   Paste your final accepted code into `solution.py`.

3. **Record submission stats**  
   Edit `submission.json` with runtime, memory, percentiles, etc.

4. **Generate the folder-level README**

   ```bash
   python gen_readme.py problems/0123-best-time-to-buy-and-sell-stock
   ```

5. **Commit**

   ```bash
   git add problems/0123-best-time-to-buy-and-sell-stock
   git commit -m "Best Time to Buy and Sell Stock"
   ```

---

## 📁  Folder Blueprint (`.template-problem/`)

| File | Description |
|------|-------------|
| `prompt.json` | Static metadata about the problem (id, title, URL, tags). |
| `submission.json` | Latest submission metrics (timestamp, language, runtime, memory, approach). |
| `solution.*` | Exactly **one** source file representing the latest accepted solution. |
| `README.md` | Auto-generated summary combining the two JSON files + code. |

Copy this directory whenever you start a new problem—both `init.sh` and `gemini_init.py` handle the copying and metadata population for you.

---

## ⚙️  Helper Scripts

| Script | Description |
|--------|-------------|
| `init.sh` | Scaffolds a new problem folder from `.template-problem` with manual metadata entry. |
| `gemini_init.py` | AI-powered scaffold generator using Gemini to extract metadata from LeetCode URLs. |
| `gen_readme.py` | Builds/refreshes the per-problem `README.md` using JSON metadata. |
| `get_stats.py` | Updates the root-level README.md with overall statistics (problems solved, runtime, memory, etc.). |

All scripts live in the repo root for easy access.

---

## 🔧 Git Hooks

To automatically update the root-level README.md whenever problem files are modified, add this pre-commit hook:

```bash
#!/bin/sh

# Check if any problem folders were modified
if git diff --cached --name-only | grep -E '^problems/[0-9]+-.*/.*\.(json|py)$' > /dev/null; then
    echo "Updating README.md with latest statistics..."
    python3 get_stats.py
    git add README.md
fi
```

Save this as `.git/hooks/pre-commit` and make it executable with `chmod +x .git/hooks/pre-commit`.