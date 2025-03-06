grid = [[1,3],[2,2]]
n = len(grid)
n*=n
visit = [0]*n
s = 0
sol = [0,0]
for i in grid:
    for j in i:
        if visit[j-1]:
            sol[0] = j
            s-=j
        visit[j-1] = 1
        s+=j
sol[1] = (n*(n+1))/2 - s
print(sol)