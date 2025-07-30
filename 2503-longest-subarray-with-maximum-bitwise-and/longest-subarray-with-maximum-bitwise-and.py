class Solution(object):
    def longestSubarray(self, nums):
        count = 0
        largest = 0
        result = 0
        for i in nums:
            if i>largest:
                largest = i
                count = 1
                result = 0
            elif i == largest:
                count += 1
            else:
                result = count if count>result else result
                count = 0
        result = count if count>result else result
        return result
        