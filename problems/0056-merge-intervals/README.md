# 0056 · Merge Intervals

| Difficulty | Tags | Latest submission | Last updated |
| --- | --- | --- | --- |
| Medium | array · sorting | **Python3** · 7 ms · 21.8 MB | 2025-09-07 06:37 UTC |

---

## Problem Statement
https://leetcode.com/problems/merge-intervals/description/

---

## Approach
Sort & Two-Pointers: Sort list `nums` based on the 'start time.' Then, initialize two pointers (`running_start`, `running_end`) to keep track of start and end of the current interval. Only flush when the start of the current interval comes after `running_end`.

---

## Complexity
| | Time | Space |
|---|---|---|
| Solution | O(n x log n) | O(1) |

---

## Code

```python
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort intervals by start time
        intervals.sort(key=lambda x: x[0])

        # keep track of running_start, running_end
        # only flush when running_end < current_start
        # otherwise keep updating the running_end
        merged_intervals = []
        running_start, running_end = intervals[0]
        for curr_start, curr_end in intervals[1:]:
            if curr_start <= running_end:  # if overlapping, extend the running interval
                running_end = max(running_end, curr_end)
            else:  # if non-overalpping, save the current and start a new interval
                merged_intervals.append([running_start, running_end])
                running_start, running_end = curr_start, curr_end
        merged_intervals.append([running_start, running_end])  # flush the remaining interval
        return merged_intervals

```

---

## Submission Stats
| Runtime | Memory | Beats | Submission |
| --- | --- | --- | --- |
| 7 ms | 21.8 MB | 72.95 % time · 15.38 % memory | [View](https://leetcode.com/problems/merge-intervals/submissions/1762334987/) |
