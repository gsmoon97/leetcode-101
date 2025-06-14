# 0383 · Ransom Note

| Difficulty | Tags | Latest submission | Last updated |
| --- | --- | --- | --- |
| Easy | hash-table · string · counting | **Python3** · 19 ms · 17.7 MB | 2025-06-14 13:07 UTC |

---

## Problem Statement
https://leetcode.com/problems/ransom-note

---

## Approach
One-pass of both `magazine` and `ransomNote` with a fixed 26-slot array of all valid lowercase English characters

---

## Complexity
| | Time | Space |
|---|---|---|
| Solution | O(m+n) | O(1) |

---

## Code

```python
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):  # early termination
            return False
        counter = [0] * 26  # lowercase English letters
        base = ord('a')
        for m in magazine:
            counter[ord(m) - base] += 1
        for r in ransomNote:
            idx = ord(r) - base
            counter[idx] -= 1
            if counter[idx] == -1:
                return False
        return True
```

---

## Submission Stats
| Runtime | Memory | Beats | Submission |
| --- | --- | --- | --- |
| 19 ms | 17.7 MB | 59.03 % time · 99.71 % memory | [View](https://leetcode.com/problems/ransom-note/submissions/1663864450/) |
