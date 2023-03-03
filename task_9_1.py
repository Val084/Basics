n = int(input())
if n not in range(1, 100000):
    print("Wrong amount of numbers")
    quit()
a = list(map(int, input().split()))
if n != len(a):
    print("Got wrong amount of elements")
    quit()
for i in range(n):
    if a[i] not in range(20000000000):
        print("Wrong element number " + str(i + 1) + " == " + str(a[i]))
        quit()
print(len(set((a))))




