# 0973 · K Closest Points to Origin

| Difficulty | Tags | Latest submission | Last updated |
| --- | --- | --- | --- |
| Medium | array · math · divide-and-conquer · geometry · sorting · heap-priority-queue · quickselect | **Python3** · 69 ms · 60.9 MB | 2025-08-30 20:06 UTC |

---

## Problem Statement
https://leetcode.com/problems/k-closest-points-to-origin/

---

## Approach
Max Heap: One-pass iteration of `points` while maintaining k points with smallest distance from the origin

---

## Complexity
| | Time | Space |
|---|---|---|
| Solution | O(n log k) | O(k) |

---

## Code

```python
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            x, y = point
            distance = x ** 2 + y ** 2
            heapq.heappush(heap, (-1 * distance, point))  # negate the distance (i.e., priority) since Python's heapq is min heap by default (maintaining smallest K requires max heap instead)
            if len(heap) > k:
                heapq.heappop(heap) # remove the element with the largest distance
        return [point for distance, point in heap]
```

---

## Submission Stats
| Runtime | Memory | Beats | Submission |
| --- | --- | --- | --- |
| 69 ms | 60.9 MB | 22.31 % time · 76.6 % memory | [View](https://leetcode.com/problems/k-closest-points-to-origin/submissions/1754006088/) |
