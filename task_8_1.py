n = int(input())
res = []
if (n >= 1) and (n <= 10000):
    for i in range(n):
        a = int(input())
        res.append(a)
res.reverse()
print(res)