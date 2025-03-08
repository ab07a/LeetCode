blocks = "BBWBWBWBW"
k = 2
index = 0
n = len(blocks)
count = 0
for i in range(k):
    if blocks[i]=="W":
        count+=1
sol = count
while (k<n):
    if blocks[k]=="W" and blocks[index] == "B":
        count+=1
    elif blocks[k]=="B" and blocks[index] == "W":
        count-=1
    k+=1
    index+=1
    sol = min(count,sol)
print(sol)