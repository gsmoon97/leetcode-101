# 0232 · Implement Queue using Stacks

| Difficulty | Tags | Latest submission | Last updated |
| --- | --- | --- | --- |
| Easy | stack · design · queue | **Python3** · 1 ms · 17.8 MB | 2025-06-14 10:55 UTC |

---

## Problem Statement
https://leetcode.com/problems/implement-queue-using-stacks

---

## Approach
Two internal stacks (FIFO and reverse FIFO) where only one is always full

---

## Complexity
| | Time | Space |
|---|---|---|
| Solution | O(n) | O(n) |

---

## Code

```python
from collections import deque

class MyQueue:

    def __init__(self):
        self.stack1 = deque()  # LIFO
        self.stack2 = deque()  # reverse LIFO (FIFO)

    def push(self, x: int) -> None:
        while self.stack2:
            self.stack1.append(self.stack2.pop())
        self.stack1.append(x)

    def pop(self) -> int:
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

    def peek(self) -> int:
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        return self.stack2[-1]

    def empty(self) -> bool:
        return (not self.stack1) and (not self.stack2)


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
```

---

## Submission Stats
| Runtime | Memory | Beats | Submission |
| --- | --- | --- | --- |
| 1 ms | 17.8 MB | 1.83 % time · 90.32 % memory | [View](https://leetcode.com/problems/implement-queue-using-stacks/submissions/1663763680/) |
