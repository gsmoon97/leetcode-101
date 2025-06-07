# 0125 · Valid Palindrome

| Difficulty | Tags | Latest submission | Last updated |
| --- | --- | --- | --- |
| Easy | two-pointers · string | **Python3** · 3 ms · 18.3 MB | 2025-06-07 13:51 UTC |

---

## Problem Statement
https://leetcode.com/problems/valid-palindrome

---

## Approach
Two-pointers closing in on the middle

---

## Complexity
| | Time | Space |
|---|---|---|
| Solution | O(n) | O(1) |

---

## Code

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()  # convert all uppercases to lowercases
        left = 0
        right = len(s) - 1
        while left < right:
            left_c = s[left]
            if not left_c.isalnum():  # skip if not alphanumeric
                left += 1
                continue
            right_c = s[right]
            if not right_c.isalnum():  # skip if not alphanumeric
                right -= 1
                continue
            if left_c != right_c:
                return False
            left += 1
            right -= 1
        return True
```

---

## Submission Stats
| Runtime | Memory | Beats | Submission |
| --- | --- | --- | --- |
| 3 ms | 18.3 MB | 98.96 % time · 42.8 % memory | [View](https://leetcode.com/problems/valid-palindrome/submissions/1656613073/) |
