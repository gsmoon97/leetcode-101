# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        # binary search
        # half the search space per iteration until the start and end pointers converge
        start, end = 1, n
        while start < end:
            query = start + (end - start) // 2
            if isBadVersion(query):
                end = query
            else:
                start = query + 1
        return end