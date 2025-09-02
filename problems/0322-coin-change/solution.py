class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 1-D DP
        dp = [float('inf')] * (amount + 1)  # +1 for amount = 0
        dp[0] = 0  # initialize DP

        # bottom-up approach
        for curr_amount in range(1, amount+1):
            # check for all coins
            for coin in coins:
                if coin <= curr_amount:
                    dp[curr_amount] = min(dp[curr_amount], dp[curr_amount - coin] + 1)  # based on the assumption that min(amount) = min(amount-coin) + 1
        
        return dp[amount] if dp[amount] != float('inf') else -1