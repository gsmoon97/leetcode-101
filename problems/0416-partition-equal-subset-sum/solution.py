class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # Formulate as a 0/1 Knapsack Problem
        total_sum = sum(nums)
        if total_sum % 2 != 0:  # early termination for odd total sum
            return False
        target_sum = total_sum // 2
        
        # DP: Bottom-Up with iteration
        dp = [False] * (target_sum + 1)
        dp[0] = True  # sum 0 is achievable without using any numbers

        for num in nums:
            for i in range(target_sum, num - 1, -1):  # traverse backwards to prevent using the same `num`
                dp[i] = dp[i] or dp[i-num]
        
        return dp[target_sum]
        