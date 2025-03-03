nums = [9,12,5,10,14,3,10]
pivot = 10
less = equal = large = 0
for i in nums:
    if i<pivot:
        less += 1
    elif i == pivot:
        equal += 1
large = (less+equal)
equal = less
less = 0
sol = [0]*len(nums)
for i in nums:
    if i<pivot:
        sol[less] = i
        less +=1
    elif i>pivot:
        sol[large] = i
        large +=1
    else:
        sol[equal] = i
        equal +=1
print(sol)