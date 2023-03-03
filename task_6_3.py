a = int(input())
b = int(input())
res = []
if a <= b:
    for i in range(2, b + 1, 2):
        res.append(i)
print(res)