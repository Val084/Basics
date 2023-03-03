a = int(input())
b = int(input())
x = int(input())
if x == a and x == b:
    print(2)
elif (a >= x) and (b < x):
    print("Mike")
elif (a < x) and (b >= x):
    print("Ivan")
elif ((a < x) + (b < x)) >= x:
    print(1)
else:
    print(0)