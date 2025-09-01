class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        has_seen = set()
        for num in nums:
            if num in has_seen:
                return True
            has_seen.add(num)
        return False