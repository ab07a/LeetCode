colors = [0,1,0,1,0]
k = 3
temp = -1
n = len(colors)
r = colors[k-1]
for i in range(1,k):
    if colors[i] == colors[i-1]:
        temp = i
sol = 1 if temp == -1 else 0
for i in range(1,n):
    if i==temp:
        temp = -1
    if colors[(i+k-1)%n]==r:
        temp = (i+k-1)%n
    r = colors[(i+k-1)%n]
    if temp==-1:
        sol+=1
print(sol)