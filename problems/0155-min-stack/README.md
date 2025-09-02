# 0155 · Min Stack

| Difficulty | Tags | Latest submission | Last updated |
| --- | --- | --- | --- |
| Medium | stack · design | **Python3** · 8 ms · 21.3 MB | 2025-09-02 21:20 UTC |

---

## Problem Statement
https://leetcode.com/problems/min-stack/description/

---

## Approach
Two-stack approach: 1) `stack` to keep track of elements in the order push/pop operation (LIFO) 2) `min_stack` to keep track of the minimum value at each point of the push operation

---

## Complexity
| | Time | Space |
|---|---|---|
| Solution | O(1) | O(n) |

---

## Code

```python
class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(val, self.min_stack[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()  # no need to keep track of the minimum at the point when the "popped" element was "pushed" anymore

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]  # min_stack always keeps track of the minimum at the point of "push" operations

        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
```

---

## Submission Stats
| Runtime | Memory | Beats | Submission |
| --- | --- | --- | --- |
| 8 ms | 21.3 MB | 40.2 % time · 60.27 % memory | [View](https://leetcode.com/problems/min-stack/submissions/1757563747/) |
