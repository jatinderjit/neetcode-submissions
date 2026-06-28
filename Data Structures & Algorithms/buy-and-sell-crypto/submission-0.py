class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = prices[0]
        for p in prices:
            if p <= buy:
                buy = p
            else:
                profit = max(profit, p - buy)
        return profit