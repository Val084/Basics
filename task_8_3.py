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

count = 0  # init counter
while len(weights) >= 2:  # work while we have at least 2 elements (sailor)
    # out sailor - index 0, search a pair for him
    i = 1       # init iterator
    i_max = 1   # init max element index
    m_max = -1  # init max element value
    while i < len(weights):  # search from second until the end
        if weights[i] >= m_max and weights[0] + weights[i] < m:
            # we found new maximum, and our sailor weight and this new maximum less than m
            i_max = i  # new max index
            m_max = weights[i]  # new max value
        i += 1

    if m_max != -1:
        # we found suitable pair element, this guy will not swim along
        weights.pop(i_max) # remove pair from sailor's list

    weights.pop(0)  # remove our sailor
    count += 1  # increase boat amounts

if len(weights):
    count += 1  # 1 guy left - have to give to him another boat

print("Total boats required count: " + str(count))


#for i in range(2, 2, n):
#    if
#i - одна лодка
#м - масса макс
#st - massa 1 chel
#n - vse pyt





