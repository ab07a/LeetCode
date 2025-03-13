nums = [2,0,2]
queries = [[0,2,1],[0,2,1],[1,1,3]]
def minZeroArray(nums, queries):
    n = len(nums)
    lis = [0]*n
    temp = 0
    index = 0
    while index!=n:
        if (nums[index] - (temp + lis[index])) <= 0:
            temp+=lis[index]
            index+=1
        else:
            break
    else:
        return 0
    for i in range(len(queries)):
        l, r, val = queries[i]
        if r>=index:
            if index>l:
                lis[index] += val
            else:
                lis[l] += val
        if r!=n-1 and r>=index:
            lis[r+1] -= val
        while index!=n:
            if (nums[index] - (temp + lis[index])) <= 0:
                temp+=lis[index]
                index+=1
            else:
                break
        else:
            return i+1
    return -1
print(minZeroArray(nums,queries))