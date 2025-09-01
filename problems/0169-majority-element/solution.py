class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate, balance = None, 0
        for num in nums:
            if num == candidate:
                balance += 1  # increment balance for every candidate
            else:
                if balance > 0:  # decrement balance for every non-candidate
                    balance -= 1
                else:  # replace candidate if balance <= 0 (i.e., non-candidates have appeared more than the candidate so far)
                    candidate = num
                    balance = 1
        return candidate
