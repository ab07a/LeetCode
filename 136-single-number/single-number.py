class Solution(object):
    def singleNumber(self, nums):
        sol = 0
        for i in nums:
            sol ^= i
        return sol
        