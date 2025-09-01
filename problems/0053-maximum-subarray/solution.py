class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Kadane's Algorithm
        max_sum = running_sum = nums[0]
        for num in nums[1:]:
            if num > (running_sum + num):  # only reset the running sum if the current number is larger than current number + running sum
                running_sum = num
            else:
                running_sum += num  # otherwise, add the current number to the running sum
            max_sum = max(max_sum, running_sum)
        return max_sum