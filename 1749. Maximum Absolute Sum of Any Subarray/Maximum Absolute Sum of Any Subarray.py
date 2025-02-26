nums = [2,-5,1,-4,3,-2]
min_prefix_sum = 0
max_prefix_sum = 0
prefix_sum = 0

for num in nums:
    prefix_sum += num

    min_prefix_sum = min(min_prefix_sum, prefix_sum)
    max_prefix_sum = max(max_prefix_sum, prefix_sum)

print(max_prefix_sum-min_prefix_sum)