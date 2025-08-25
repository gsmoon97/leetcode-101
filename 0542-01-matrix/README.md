# 0542 · 01 Matrix

| Difficulty | Tags | Latest submission | Last updated |
| --- | --- | --- | --- |
| Medium | array · dynamic-programming · breadth-first-search · matrix | **Python3** · 139 ms · 20.7 MB | 2025-08-25 21:23 UTC |

---

## Problem Statement
https://leetcode.com/problems/01-matrix/description/

---

## Approach
Multi-source BFS: formulate the problem from finding the shortest path from 'each 1s to 0s' to finding the shortest path from 'each 0s to 1s' triggering BFS search from all 0s

---

## Complexity
| | Time | Space |
|---|---|---|
| Solution | O(m x n) | O(m x n) |

---

## Code

```python
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        distances = [[0] * n for _ in range(m)]  # initialized the distance matrix
        
        # multi-source BFS
        queue = deque()  # use queue for BFS
        for r in range(m):
            for c in range(n):
                if mat[r][c] == 0:
                    value = 0
                    queue.append((r,c))  # initialize the queue with all cells with the value "0" (i.e., multi-source BFS)
                else:
                    value = float('inf')  # if cell value is 1 (i.e., not 0), initialize the value to "infinity" to mark that it is unvisited
                distances[r][c] = value

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # all four possible directions (excluding diagonals)
        while queue:
            r, c = queue.popleft()
            for dir in directions:
                nr, nc = r + dir[0], c + dir[1]
                if (0 <= nr < m) and (0 <= nc < n):  # only update when it is found that the neighboring cell can be reached with a shorter distance
                    if distances[nr][nc] > distances[r][c] + 1:
                        distances[nr][nc] = distances[r][c] + 1
                        queue.append((nr, nc))
        return distances





```

---

## Submission Stats
| Runtime | Memory | Beats | Submission |
| --- | --- | --- | --- |
| 139 ms | 20.7 MB | 53.25 % time · 44.26 % memory | [View](https://leetcode.com/problems/01-matrix/submissions/1748264941/) |
