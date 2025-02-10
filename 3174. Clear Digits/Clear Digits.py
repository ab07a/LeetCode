s = "cba34"
temp = 0
sol = ""
for i in range(len(s)-1,-1,-1):
    if s[i].isdigit():
        temp += 1
        continue
    if temp:
       temp -= 1
    else:
        sol = s[i] + sol
print(sol) 