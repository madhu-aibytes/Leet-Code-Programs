class Solution:
    def maxProfit(self, prices):
        buy = prices[0]
        mp = 0
        for i in range(1, len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            else:
                profit = prices[i] - buy
                mp = max(mp, profit)
                
        return mp