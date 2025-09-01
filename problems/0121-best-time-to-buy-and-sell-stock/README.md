# 0121 · Best Time to Buy and Sell Stock

| Difficulty | Tags | Latest submission | Last updated |
| --- | --- | --- | --- |
| Easy | array · dynamic-programming | **Python3** · 75 ms · 26.9 MB | 2025-06-04 17:06 UTC |

---

## Problem Statement
https://leetcode.com/problems/best-time-to-buy-and-sell-stock

---

## Approach
One-pass iteration of the 'prices' with update to the 'buy price' only when a smaller value is encountered

---

## Complexity
| | Time | Space |
|---|---|---|
| Solution | O(n) | O(1) |

---

## Code

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # only change the buy date when the current date price < buy date price
        buy_price = prices[0]
        max_profit = 0
        for price in prices[1:]:  # max profit is 0 if there is only one price
            if price < buy_price:
                buy_price = price
            else:
                max_profit = max(price - buy_price, max_profit)
        return max_profit

```

---

## Submission Stats
| Runtime | Memory | Beats | Submission |
| --- | --- | --- | --- |
| 75 ms | 26.9 MB | 68.96 % time · 77.67 % memory | [View](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/1653942312/) |
