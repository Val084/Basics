n = int(input())
nu = 0
while n > 0:
    c = int(input())
    if c == 0:
        nu += 1
    n -= 1
print(nu)