# 0139 · Word Break

| Difficulty | Tags | Latest submission | Last updated |
| --- | --- | --- | --- |
| Medium | array · hash-table · string · dynamic-programming · trie · memoization | **Python3** · 7 ms · 18.1 MB | 2025-08-26 22:34 UTC |

---

## Problem Statement
https://leetcode.com/problems/word-break/description/

---

## Approach
Top-down dynamic programming with memoization

---

## Complexity
| | Time | Space |
|---|---|---|
| Solution | O(n^2 x m) | O(n^2) |

---

## Code

```python
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}  # memoization to ensure each unique substring is checked only once
        
        # top-down dynamic programming with memoization
        def dp(s: str) -> bool:
            if not s:
                return True
            
            if s in memo:
                return memo[s]

            for i in range(1, len(s) + 1):
                subword = s[:i]
                if subword in wordDict:
                    if dp(s[i:]):
                        memo[s] = True
                        return True
            memo[s] = False
            return False
        
        return dp(s)
```

---

## Submission Stats
| Runtime | Memory | Beats | Submission |
| --- | --- | --- | --- |
| 7 ms | 18.1 MB | 23.52 % time · 25.17 % memory | [View](https://leetcode.com/problems/word-break/submissions/1749574420/) |
