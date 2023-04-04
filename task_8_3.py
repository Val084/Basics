m = int(input("Max weight:"))
if m not in range(1, 1000000):
    print("Wrong amount of numbers")
    quit()

weights = []
n = int(input("Number of fishermen:"))
if (n >= 1) and (n <= 100):
    for i in range(n):
        st = int(input("Weight of one fisherman:"))
        if st not in range(1, m):
            print("ERROR: Wrong amount of numbers!")
            quit()
        weights.append(st)

count = 0
while len(weights) >= 2:

    i_max = 1
    m_max = -1
    while i < len(weights):
        if weights[i] >= m_max and weights[0] + weights[i] < m:

            i_max = i
            m_max = weights[i]
        i += 1

    if m_max != -1:

        weights.pop(i_max)

    weights.pop(0)
    count += 1

if len(weights):
    count += 1

print("Total boats required count: " + str(count))


#for i in range(2, 2, n):
#    if
#i - одна лодка
#м - масса макс
#st - massa 1 chel
#n - vse pyt





