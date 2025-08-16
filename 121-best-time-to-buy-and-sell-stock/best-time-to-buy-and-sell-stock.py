class Solution(object):
    def maxProfit(self, prices):
        s = prices[0]
        sol = 0
        for i in range(1, len(prices)):
            if prices[i]<s:
                s = prices[i]
            elif prices[i]-s>sol:
                sol = prices[i]-s
        return sol
        