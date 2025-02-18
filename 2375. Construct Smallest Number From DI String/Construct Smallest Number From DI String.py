pattern = "IIIDIDDD"
sol = [0]*(len(pattern)+1)
temp = 0
for i in range(len(pattern)-1,-1,-1):
    if pattern[i]=="D":
        temp+=1
        sol[i] = temp
    else:
        temp=0
flag = False
temp = 1
temp2 = 0
for i in range(len(sol)):
    if not sol[i] and not flag:
        sol[i] = temp
        temp += 1
    elif not sol[i] and flag:
        sol[i] = temp
        temp = temp2+1
        flag = False
    else:
        sol[i] += temp
        if not flag:
            temp2 = sol[i]
            flag = True
print("".join(map(str,sol)))