class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        result = nums[0]+nums[1]+nums[2]
        n = len(nums)
        for i in range(n):
            l, r = i+1, n-1
            while l<r:
                t=nums[i]+nums[l]+nums[r]
                if abs(target-t)<abs(target-result):
                    result = t
                if t>target:
                    r-=1
                else:
                    l+=1
        return result
        