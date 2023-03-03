x = int(input())
if x not in range(2000000000):
    print("Wrong amount of numbers")
    quit()
count = 2
for i in range(2, (x//2)+1):
    if x % i == 0:
     count += 1
print(count)