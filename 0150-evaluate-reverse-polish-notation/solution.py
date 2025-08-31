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
