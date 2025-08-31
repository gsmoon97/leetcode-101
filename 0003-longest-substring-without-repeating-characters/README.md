# 0003 · Longest Substring Without Repeating Characters

| Difficulty | Tags | Latest submission | Last updated |
| --- | --- | --- | --- |
| Medium | hash-table · string · sliding-window | **Python3** · 19 ms · 17.8 MB | 2025-08-31 02:50 UTC |

---

## Problem Statement
https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

---

## Approach
Sliding window approach with HashMap: One-pass iteration of the string with a `start` to keep track of the start of the substring and `seen` to keep track of when each unique character was seen most recently. When the current character has been seen before (i.e., duplicate), 1) update `start` to the position right after the duplicate or maintain the current `start`, whichever is later.

---

## Complexity
| | Time | Space |
|---|---|---|
| Solution | O(n) | O(1) |

---

## Code

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        start = 0
        max_length = 0
        for end, char in enumerate(s):
            if char in seen:
                start = max(seen[char] + 1, start)  # update start to the very next character after the duplicate (but only update if the current start is earlier than the updated start)
            seen[char] = end
            max_length = max(max_length, end - start + 1)  # update the maximum length to keep track of the length of the longest substring
        return max_length
```

---

## Submission Stats
| Runtime | Memory | Beats | Submission |
| --- | --- | --- | --- |
| 19 ms | 17.8 MB | 53.22 % time · 52.54 % memory | [View](https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/1754078229/) |
