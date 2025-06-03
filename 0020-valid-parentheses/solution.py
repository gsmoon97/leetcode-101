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