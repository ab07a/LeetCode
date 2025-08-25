class Solution(object):
    def sortColors(self, nums):
        n = len(nums)
        l,r = 0, n-1
        temp = -1
        while l<r:
            if nums[l]>nums[r]:
                nums[l], nums[r] = nums[r], nums[l]
            elif nums[l]==1 and nums[l] == nums[r]:
                temp = r
                while l!=r:
                    if nums[r]!=1:
                        nums[r], nums[temp] = nums[temp], nums[r]
                        r = temp
                        break
                    r-=1
            
            if nums[l]==0:
                l+=1
            if nums[r] == 2:
                r-=1
            
        return nums
        