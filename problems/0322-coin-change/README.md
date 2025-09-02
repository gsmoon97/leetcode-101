# 0322 · Coin Change

| Difficulty | Tags | Latest submission | Last updated |
| --- | --- | --- | --- |
| Medium | array · dynamic-programming · breadth-first-search | **Python3** · 707 ms · 18.2 MB | 2025-09-02 00:50 UTC |

---

## Problem Statement
https://leetcode.com/problems/coin-change/description/

---

## Approach
1-D DP: Bottom-up approach based on the assumption that min(amount) = min(amount - coin) + 1

---

## Complexity
| | Time | Space |
|---|---|---|
| Solution | O(m x n) where m = amount, n = len(coins) | O(m) where m = amount |

---

## Code

```python
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
```

---

## Submission Stats
| Runtime | Memory | Beats | Submission |
| --- | --- | --- | --- |
| 707 ms | 18.2 MB | 79.49 % time · 56.81 % memory | [View](https://leetcode.com/problems/coin-change/submissions/1756407453/) |
