pets = dict()
name = input("Кличка животного:")
typ = input("Вид животного:")
age = int(input("Возраст животного:"))
name2 = input("Имя владельца:")
pets[name] = dict()
pets[name]['Вид питомца'] = typ
pets[name]['Возраст питомца'] = age
pets[name]['Имя владельца'] = name2
#for name in pets.keys():
   # age = pets[name]['Возраст питомца']
   #print("Имя " + name)
   # print("То что в pets " + str(pets))
tmp = pets[name]['Возраст питомца'] % 10
if tmp == 1:



print(pets)


# for по каждому животному
#   tmp = pets['Возраст питомца'] % 10
#   if tmp == 1:
#       print (pet[вид] возраст год)
#   else if tmp in [2, 4]:
#       print года
#   else
#       print лет









