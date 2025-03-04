n = 10
while n > 0:
    if n % 3 == 2:
        print(False)
        break
    n //= 3
else:
    print(True)