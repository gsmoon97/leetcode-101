# 0150 · Evaluate Reverse Polish Notation

| Difficulty | Tags | Latest submission | Last updated |
| --- | --- | --- | --- |
| Medium | array · math · stack | **Python3** · 4 ms · 19.2 MB | 2025-08-31 21:09 UTC |

---

## Problem Statement
https://leetcode.com/problems/evaluate-reverse-polish-notation/description/

---

## Approach
Stack: One-pass iteration on `tokens` while using a stack to keep track of all operands and process them in LIFO order. When operand, push to stack. When operator (+, -, *, /), pop the last two operands from the stack to perform operation and push the result back into the stack.

---

## Complexity
| | Time | Space |
|---|---|---|
| Solution | O(n) | O(n) |

---

## Code

```python
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []  # stack to keep track of all operands and intermediate calculations
        _operators = {'+', '-', '*', '/'}  # use set for O(1) lookup
        for token in tokens:
            if token in _operators:
                b = stack.pop()  # second operand
                a = stack.pop()  # first operand
                if token == '+':
                    c = a + b
                elif token == '-':
                    c = a - b
                elif token == '*':
                    c = a * b
                else:  # '/'
                    c = int(a / b)  # cast to int to always truncate toward zero
                stack.append(c)
            else:
                stack.append(int(token))  # convert to int when storing in the stack
        return stack.pop()

```

---

## Submission Stats
| Runtime | Memory | Beats | Submission |
| --- | --- | --- | --- |
| 4 ms | 19.2 MB | 28.59 % time · 17.35 % memory | [View](https://leetcode.com/problems/evaluate-reverse-polish-notation/submissions/1755202833/) |
