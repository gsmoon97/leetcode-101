# 0020 · Valid Parentheses

| Difficulty | Tags | Latest submission | Last updated |
| --- | --- | --- | --- |
| Easy | string · stack | **Python3** · 0 ms · 17.7 MB | 2025-06-03 20:22 UTC |

---

## Problem Statement
https://leetcode.com/problems/valid-parentheses

---

## Approach
One-pass stack with look-up map

---

## Complexity
| | Time | Space |
|---|---|---|
| Solution | O(n) | O(n) |

---

## Code

```python
from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()  # LIFO
        bracket_pairs = {')': '(', '}': '{', ']': '['}  # mapping of close -> open brackets
        for char in s:
            if char in bracket_pairs.values():
                stack.append(char)
            else:
                if not stack:
                    return False  # early termination when attempt to close without any opening bracket
                opened = stack.pop()
                if opened != bracket_pairs[char]:  # bracket types don't match
                    return False
        return not stack  # stack should be empty at the end
```

---

## Submission Stats
| Runtime | Memory | Beats | Submission |
| --- | --- | --- | --- |
| 0 ms | 17.7 MB | 100.0 % time · 80.76 % memory | [View](https://leetcode.com/problems/valid-parentheses/submissions/1653064881/) |
