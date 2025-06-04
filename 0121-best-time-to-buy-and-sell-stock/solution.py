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
