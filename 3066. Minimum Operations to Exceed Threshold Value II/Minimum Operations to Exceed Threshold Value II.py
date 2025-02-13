import heapq

nums = [2,11,10,1,3]
k = 10

sol = 0
l = []

for i in nums:
    if i<k:
        heapq.heappush(l,i)

while l:
    if len(l)==1:
        sol+=1
        break
    a, b = heapq.heappop(l), heapq.heappop(l)
    temp = a*2 + b
    if temp < k:
        heapq.heappush(l, temp)
    sol += 1
print(sol)