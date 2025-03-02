from collections import defaultdict


nums1 = [[1,2],[2,3],[4,5]]
nums2 = [[1,4],[3,2],[4,1]]

temp = defaultdict(int)

for num in nums1 + nums2:
    temp[num[0]] += num[1]

print(sorted(temp.items()))