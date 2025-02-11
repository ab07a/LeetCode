s = "daabcbaabcbc"
part = "abc"

while part in s:
    s = s.replace(part,"",1)
print(s)