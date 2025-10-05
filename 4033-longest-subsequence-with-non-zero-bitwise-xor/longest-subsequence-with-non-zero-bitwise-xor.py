class Solution(object):
    def longestSubsequence(self, nums):
        sol = len(nums)
        xor = 0
        flag = False
        for i in nums:
            if i:
                flag = True
            xor ^= i
        if not flag:
            return 0
        if not xor:
            return sol-1
        return sol
        