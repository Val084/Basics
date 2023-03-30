def create():
#новая запись с информацией о питомце(в pets)
def read():
#Информация о запрашиваемом питомце
def update():
#обн инф об указанном питомце
def delete():
#удаляет запись о питомце


pets = dict()
command = 'n'



while True:
    command = input()
    if command == "stop":
        break


# for name in pets.keys():
# age = pets[name]['Возраст питомца']
# print("Имя " + name)
# print("То что в pets " + str(pets))