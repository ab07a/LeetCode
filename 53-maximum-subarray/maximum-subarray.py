class Solution(object):
    def maxSubArray(self, nums):
        s = 0
        sol = -float('inf')
        for i in nums:
            s+=i
            if s>sol:
                sol = s
            if s<0:
                s=0
        return sol
        