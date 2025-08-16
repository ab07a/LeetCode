class Solution(object):
    def maxProfit(self, prices):
        smallest=0
        max_val=0
        for i in range(0, len(prices)):
            if(prices[i]<prices[smallest]):
                smallest=i
            else:
                max_val=max(max_val, prices[i]-prices[smallest])
        return max_val
        