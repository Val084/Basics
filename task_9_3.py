
res1 = list(map(int, input().split()))
r = set()
for i in res1:
    if i in r:
        print("Yes")
    else:
        print("No")
        r.add(i)



