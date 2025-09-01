# 0242 · Valid Anagram

| Difficulty | Tags | Latest submission | Last updated |
| --- | --- | --- | --- |
| Easy | hash-table · string · sorting | **Python3** · 11 ms · 17.7 MB | 2025-06-07 15:22 UTC |

---

## Problem Statement
https://leetcode.com/problems/valid-anagram

---

## Approach
One-pass with fix-sized array of all valid characters

---

## Complexity
| | Time | Space |
|---|---|---|
| Solution | O(n) | O(1) |

---

## Code

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):  # early termination when mismatch in length
            return False
        counter = [0] * 26  # 26 since the characters consist of lowercase English letters
        base = ord('a')
        for char_s, char_t in zip(s, t):
            counter[ord(char_s) - base] += 1  # increment count for s
            counter[ord(char_t) - base] -= 1  # decrement count for t
        return all(c == 0 for c in counter)  # check that all the post-processed counts are 0
```

---

## Submission Stats
| Runtime | Memory | Beats | Submission |
| --- | --- | --- | --- |
| 11 ms | 17.7 MB | 72.7 % time · 97.55 % memory | [View](https://leetcode.com/problems/valid-anagram/submissions/1656721520/) |
