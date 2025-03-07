left, right = 10, 19
prime = [0]*(right+1)
sol = [-1,-1]
m = float("inf")
pre = 0
for i in range(2,right+1):
    if not prime[i]:
        if i>=left and pre>=left and pre!=0 and i-pre < m:
            sol = [pre,i]
            m = i-pre
        pre = i
    else:
        continue
    for j in range(i*i,right+1,i):
        prime[j] = 1
print(sol)