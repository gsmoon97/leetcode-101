class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # key observation: for any arbitrary pivot, at least one half is always sorted
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            if nums[left] <= nums[mid]:  # left side is the sorted half
                if nums[left] <= target < nums[mid]:  # target must be in the sorted half, if it exists 
                    right = mid - 1
                else:  # target must be in the unsorted half, if it exists
                    left = mid + 1
            elif nums[mid] <= nums[right]:  # right side is the sorted half
                if nums[mid] < target <= nums[right]:  # target must be in the sorted half, if it exists 
                    left = mid + 1
                else:  # target must be in the unsorted half, if it exists
                    right = mid - 1
        return -1
            


