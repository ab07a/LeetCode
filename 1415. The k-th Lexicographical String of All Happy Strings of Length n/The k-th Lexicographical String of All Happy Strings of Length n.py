n = 6
k = 9
d = {'a':['b','c'], 'b':['a','c'], 'c':['a','b']}
solK = 3*(2**(n-1))
sol = []
def happyString(s,c):
    if len(s) == n-1:
        sol.append(s+c)
    else:
        happyString(s+c,d[c][0])
        happyString(s+c,d[c][1])
happyString("",'a')
happyString("",'b')
happyString("",'c')
print(sol[93],solK)