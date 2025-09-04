# 0994 · Rotting Oranges

| Difficulty | Tags | Latest submission | Last updated |
| --- | --- | --- | --- |
| Medium | array · breadth-first-search · matrix | **Python3** · 3 ms · 18.0 MB | 2025-09-04 01:19 UTC |

---

## Problem Statement
https://leetcode.com/problems/rotting-oranges/description/

---

## Approach
Multi-source BFS: Use queue (i.e., deque) to keep track of all newly rotten oranges at each minute. Use the fixed length of the queue at the start of each minute to process only the relevant cells for the corresponding minute (i.e., BFS level).

---

## Complexity
| | Time | Space |
|---|---|---|
| Solution | O(m x n) | O(m x n) |

---

## Code

```python
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # multi-source BFS
        m, n = len(grid), len(grid[0])
        queue = deque()
        fresh_count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i,j))  # find all initially rotten oranges
                elif grid[i][j] == 1:
                    fresh_count += 1  # count all initially fresh oranges
        
        minutes = 0
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        
        while queue and fresh_count > 0:
            minutes += 1
            for _ in range(len(queue)):  # use the fixed length of the queue at the start of each minute to process only the relevant cells for the corresponding minute (i.e., BFS level)
                root_i, root_j = queue.popleft()
                for dir_i, dir_j in directions:
                    new_i, new_j = root_i + dir_i, root_j + dir_j
                    if 0 <= new_i < m and 0 <= new_j < n and grid[new_i][new_j] == 1:
                        grid[new_i][new_j] = 2  # mark as rotten
                        fresh_count -= 1
                        queue.append((new_i, new_j))
        return minutes if fresh_count == 0 else -1
```

---

## Submission Stats
| Runtime | Memory | Beats | Submission |
| --- | --- | --- | --- |
| 3 ms | 18.0 MB | 81.46 % time · 26.36 % memory | [View](https://leetcode.com/problems/rotting-oranges/submissions/1758804200/) |
