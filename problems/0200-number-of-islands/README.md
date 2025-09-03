# 0200 · Number of Islands

| Difficulty | Tags | Latest submission | Last updated |
| --- | --- | --- | --- |
| Medium | array · depth-first-search · breadth-first-search · union-find · matrix | **Python3** · 243 ms · 20.0 MB | 2025-09-03 18:11 UTC |

---

## Problem Statement
https://leetcode.com/problems/number-of-islands/description/

---

## Approach
Recursive DFS: Recursively explore all connected lands using DFS and 'sink' any visited land to mark as visited. Number of recursive DFS calls == Number of islands.

---

## Complexity
| | Time | Space |
|---|---|---|
| Solution | O(m x n) | O(m x n) |

---

## Code

```python
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # recursive dfs
        m, n = len(grid), len(grid[0])
        count = 0
        
        # the number of recursive dfs calls == the number of islands
        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != "1":  # base case
                return

            # "sink" any visited land to mark as visited
            grid[i][j] = 0

            # propagate in all four directions
            dfs(i-1, j)
            dfs(i+1, j)
            dfs(i, j-1)
            dfs(i, j+1)
        
        # recursively call dfs everytime an unvisited land is encountered
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    dfs(i, j)
                    count += 1
        return count



```

---

## Submission Stats
| Runtime | Memory | Beats | Submission |
| --- | --- | --- | --- |
| 243 ms | 20.0 MB | 64.21 % time · 82.91 % memory | [View](https://leetcode.com/problems/number-of-islands/submissions/1758546372/) |
