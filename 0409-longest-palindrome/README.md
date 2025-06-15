# 0409 · Longest Palindrome

| Difficulty | Tags | Latest submission | Last updated |
| --- | --- | --- | --- |
| Easy | hast-table · string · greedy | **Python3** · 0 ms · 17.8 MB | 2025-06-15 07:10 UTC |

---

## Problem Statement
https://leetcode.com/problems/longest-palindrome

---

## Approach
Hash map to count frequency of each unique letter and sum the largest even contribution per letter (e.g., 1 for 2, 2 for 5, etc.). Lastly, add 1 more count if any odd count exists (the remaining element can be used as the center character).

---

## Complexity
| | Time | Space |
|---|---|---|
| Solution | O(n) | O(1) |

---

## Code

```python
class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = [0] * (26 * 2)  # 2 sets (upper and lower) of 26 alphabets
        base_A = ord('A')
        base_a = ord('a')
        for c in s:
            offset = ord(c) - base_A
            if offset > 25:
                offset = ord(c) - base_a + 26
            counter[offset] += 1
        
        has_odd_count = False
        len_pal = 0
        for count in counter:
            if (count % 2) != 0:
                has_odd_count = True
            len_pal += (count // 2) * 2
        return (len_pal + 1) if has_odd_count else len_pal

        

```

---

## Submission Stats
| Runtime | Memory | Beats | Submission |
| --- | --- | --- | --- |
| 0 ms | 17.8 MB | 0.0 % time · 46.28 % memory | [View](https://leetcode.com/problems/longest-palindrome/submissions/1664675923/) |
