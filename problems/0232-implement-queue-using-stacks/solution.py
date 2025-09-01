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