
nums = [18,43,36,13,7]
sumList = [0 for _ in range(82)] 
nums.sort()
sol = 0

def numberSum(x):
    temp = 0
    for i in str(x):
        temp += int(i)
    return temp

for i in nums:
    temp = numberSum(i)
    if sumList[temp]:
        sol = max(sol, sumList[temp]+i)
    sumList[temp] = i

print(sol)