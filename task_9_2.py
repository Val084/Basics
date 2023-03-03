n = int(input("Enter the number of lines:"))
lst = []
if n not in range(100000):
    print("Wrong amount of numbers")
    quit()

for i in range(n):
    res1 = int(input())
    lst.append(res1)
res1 = set(lst)

n2 = int(input("Enter the number of lines:"))
lst1 = []
if n2 not in range(100000):
    print("Wrong amount of numbers")
    quit()

for i in range(n2):
    res2 = int(input())
    lst1.append(res2)
res2 = set(lst1)

res1.intersection_update(res2)
print(len(res1))








