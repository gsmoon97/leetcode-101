class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l_idx = 0
        r_idx = len(nums) - 1
        while l_idx <= r_idx:
            m_idx = l_idx + (r_idx - l_idx) // 2  # overflow-safe pattern
            mid = nums[m_idx]
            if target == mid:
                return m_idx
            if target < mid:
                r_idx = m_idx - 1
            else:
                l_idx = m_idx + 1
        return -1
