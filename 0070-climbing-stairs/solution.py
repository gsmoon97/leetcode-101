class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        else:
            # return self.climbStairs(n-1) + self.climbStairs(n-2)  # top-down recursion leads to stck limit
            prev_prev, prev = 2, 3
            for _ in range(4, n+1):
                prev_prev, prev = prev, prev_prev + prev
            return prev