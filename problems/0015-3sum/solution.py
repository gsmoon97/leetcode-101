class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # sort the numbers first to use two pointers later
        triplets = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:  # to skip duplicates
                continue
            target = -1 * nums[i]
            left, right = i + 1, len(nums) - 1
            while left < right:
                two_sum = nums[left] + nums[right]
                if two_sum < target:
                    left += 1
                elif two_sum > target:
                    right -= 1
                else:
                    triplets.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    # Skip duplicates for left
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    # Skip duplicates for right  
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
        return triplets