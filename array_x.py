import array
# https://pythonworld.ru/moduli/modul-array-massivy-v-python.html
arr = array.array('i',[180,2,3,1,2,3])
print(arr)
# 14479

# размер в байтах одного элемента в массиве.
# print(arr.itemsize)

# добавление элемента в конец массива.
# arr.append(9)
# print(arr)

# изменить порядок следования байтов в каждом элементе массива. Полезно при чтении данных из файла, написанного на машине с другим порядком байтов.
# arr.byteswap()
# print(arr)

# возвращает количество вхождений х в массив.
# print(arr.count(3))

# добавление элементов из списка и массива в массив.
# arr.extend(array.array('i',[4,5,6]))
# print(arr)

#FIXME -   arr.frombytes(bytes('\xd0\x91\xd0\xb0\xd0\xb9', encoding = 'utf-8'))
# print(arr.itemsize)

#FIXME -   with open("file_array_less.txt",'r') as file:
#     arr.fromfile(file,3)
# print(arr)

# номер первого вхождения x в массив.
# print(arr.index(3))

# включить новый пункт со значением х в массиве перед номером n. Отрицательные значения рассматриваются относительно конца массива.
# arr.insert(3,77)
# print(arr)

# удаляет i-ый элемент из массива и возвращает его. По умолчанию удаляется последний элемент.
# arr.pop(3)
# print(arr)

# удалить первое вхождение х из массива
# arr.remove(2)
# print(arr)

#  обратный порядок элементов в массиве.
# arr.reverse()
# print(arr)

#  преобразование к байтам.
# print(arr.tobytes())

# преобразование массива в список.
# print(type(arr))
# print(type(arr.tolist()))
efefef