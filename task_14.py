def rec(x):
    if x < 0:
        return
    else:
        rec(x - 1)
        print(x)


rec(16)
print("End of list")
