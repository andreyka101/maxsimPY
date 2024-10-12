# создать словарь
obj = {
    "key": "qwerty",
    "key2": 4555,
    "key3": [1,2,3,4],
    "444": 454,
}
# метод clear() очищает словарь
# obj.clear()


# метод copy() создаёт копию словаря
# copy = obj.copy()
# obj.clear()


# метод items() с помощью цикла for возвращает ключ и значение 
# for k, v in obj.items():
#     print(k, "=", v)


# список ключей
# print(obj.keys())
# список значений
# print(obj.values())


# метод pop('ключ') удаляет ключ из словаря и возвращает значение
# obj.pop('key2')


# метод popitem() удаляет и возвращает пару (ключ, значение)
# obj.popitem()


# метод update() обновляет словарь, добавляя пары (ключ, значение)
# obj.update({"ttt":9,"poi":"uuu"})



num_inp = input("==")
if(num_inp == "q"):
    print(2)
elif(num_inp == "w"):
    print(3)
elif(num_inp == "e"):
    print(4)
elif(num_inp == "r"):
    print(5)
elif(num_inp == "t"):
    print(6)



def fun():
    q = 8*9
    print(70)
if_obj = {
    "q": fun(),
    "w": 3,
    "e": 4,
    "r": 5,
    "t": 6,
}
print(if_obj[num_inp])

