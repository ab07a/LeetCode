class Solution(object):
    def alternatingSum(self, nums):
        sol = 0
        mul = 1
        for i in nums:
            sol += mul*i
            mul *= -1
        return sol
        