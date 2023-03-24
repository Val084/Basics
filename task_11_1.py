def factorial(n: int) -> int:
    if n < 1:
        return "Your number is not natural"
    elif n == 1:
        return 1
    else:
        return n * factorial(n - 1)


num = int(input("Enter an integer natural number:"))
lst = []
for i in reversed(range(1, factorial(num) + 1)):
    lst.append(factorial(i))
print(factorial(num))

print(lst)









