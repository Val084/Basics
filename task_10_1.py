import json

pets = dict()
name = input("Кличка животного:")
typ = input("Вид животного:")
age = int(input("Возраст животного:"))
name2 = input("Имя владельца:")
pets[name] = dict()
pets[name]['Вид питомца'] = typ
pets[name]['Возраст питомца'] = age
pets[name]['Имя владельца'] = name2
for it in pets.keys():
    for_print = "Это: " + pets[it]['Вид питомца'] + " по кличке \"" + \
                it + "\". Возраст питомца: " + str(pets[it]['Возраст питомца'])

    tmp = pets[it]['Возраст питомца'] % 10
    if tmp == 1:
        for_print += " год."
    elif (tmp >= 2) and (tmp <= 4):
        for_print += " года."
    else:
        for_print += " лет."

    for_print += ". Имя Владельца: " + pets[it]['Имя владельца']
    print(for_print)


print(pets)










