# 0057 · Insert Interval

| Difficulty | Tags | Latest submission | Last updated |
| --- | --- | --- | --- |
| Medium | array | **Python3** · 0 ms · 19.5 MB | 2025-08-25 06:03 UTC |

---

## Problem Statement
https://leetcode.com/problems/insert-interval/description/

---

## Approach
Divide into three phases:
	1) Add all intervals that end before `newInterval` starts
	2) Merge all intervals that start before `newInterval` ends
	3) Add all remaining intervals that start after newInterval ends

---

## Complexity
| | Time | Space |
|---|---|---|
| Solution | O(n) | O(1) |

---

## Code

```python
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        final_intervals = []
        i = 0
        n = len(intervals)
        
        # Phase I: find all intervals that end before start of `newInterval`
        while i < n and intervals[i][1] < newInterval[0]:
            final_intervals.append(intervals[i])
            i += 1

        # Phase II: find all intervals to merge with `newInterval`
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]
            i += 1
        final_intervals.append(newInterval)
        
        # Phase II: find all remaining intervals that start after the end of `newInterval`
        while i < n:
            final_intervals.append(intervals[i])
            i += 1

        return final_intervals
```

---

## Submission Stats
| Runtime | Memory | Beats | Submission |
| --- | --- | --- | --- |
| 0 ms | 19.5 MB | 100.0 % time · 89.64 % memory | [View](https://leetcode.com/problems/insert-interval/submissions/1747370754/) |
