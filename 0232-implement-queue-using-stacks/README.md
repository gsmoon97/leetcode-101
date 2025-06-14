# 0232 · Implement Queue using Stacks

| Difficulty | Tags | Latest submission | Last updated |
| --- | --- | --- | --- |
| Easy | stack · design · queue | **Python3** · 0 ms · 18.0 MB | 2025-06-14 11:08 UTC |

---

## Problem Statement
https://leetcode.com/problems/implement-queue-using-stacks

---

## Approach
Two internal stacks where `_in` (FIFO) maintains all elements that are pushed and `_out` (reverse FIFO) maintains all elements that are to be pulled. Transfer from `_in` to `_out` is only triggered when `_out` is empty (lazy transfer). This ensures that all elements are transferred at most once only to keep the amortized bound to O(1).

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
        self._in = deque()  # LIFO
        self._out = deque()  # reverse LIFO (FIFO)
    
    # move all elements from _in to _out
    def _transfer(self) -> None:
        while self._in:
            self._out.append(self._in.pop())

    def push(self, x: int) -> None:
        self._in.append(x)

    def pop(self) -> int:
        if not self._out:
            self._transfer()  # only trigger _transfer when _out is empty
        return self._out.pop()

    def peek(self) -> int:
        if not self._out:
            self._transfer()  # only trigger _transfer when _out is empty
        return self._out[-1]

    def empty(self) -> bool:
        return (not self._in) and (not self._out)


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
| 0 ms | 18.0 MB | 100.0 % time · 19.69 % memory | [View](https://leetcode.com/problems/implement-queue-using-stacks/submissions/1663778202/) |
