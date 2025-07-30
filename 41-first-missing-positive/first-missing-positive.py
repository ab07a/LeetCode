class Solution(object):
    def firstMissingPositive(self, nums):
        d = set(nums)
        for i in range(1,len(nums)+1):
            if i not in d:
                return i
        return len(nums)+1