n = int(input())
if n not in range(1, 10000):
    print("Wrong amount of numbers")
    quit()
a = list(map(int, input().split()))
if n != len(a):
    print("Got wrong amount of elements")
    quit()
for i in range(0, n - 1):
    if a[i] not in range(1, 1000000000):
        print("Wrong element number " + str(i + 1) + " == " + str(a[i]))
        quit()
res = []
for i in range(-1, len(a) - 1):
    res.append(a[i])
print(res)

















