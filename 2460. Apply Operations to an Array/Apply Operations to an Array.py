nums = [1,2,2,4]
n = len(nums)
count = 0
for i in range(n-1):
    if not nums[i]:
        count += 1
        continue
    if nums[i] == nums[i+1]:
        nums[i] *= 2
        nums[i+1] = 0
    nums[i-count],nums[i] = nums[i],nums[i-count]
nums[i+1-count],nums[-1] = nums[-1],nums[i+1-count]
print(nums)