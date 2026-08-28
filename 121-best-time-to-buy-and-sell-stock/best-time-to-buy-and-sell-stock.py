class Solution(object):
    def maxProfit(self, prices):
        day=prices[0]
        profit=0
        for i in range(len(prices)):
            if day>prices[i]:
                day=prices[i]
            else:
                profit=max(profit,prices[i]-day)
        return profit
