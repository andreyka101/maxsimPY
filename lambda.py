# a = 1.3
# print(type(a))

# def func (x):
#     return x*2
# print(type(func))

# lam = lambda x: x*2 
# print(lam(3))
# print(type(lam))



# пример как использовать лямбду:
# lam = lambda x , y: x*y
# print(lam(3,4))



# пример лямбды с if:
# max_number = lambda a, b: "условие выполнилось" if a > b else "условие не выполнилось"
# print(max_number(7, 5))



# лямбда как переменная
# f = lambda: 4
# f = lambda: True
# f = lambda: 'pip'
# print(f())



# метод map
# нужно все числа из массива arr умножить на 2 и добавить в ar2
# arr = [1,2,3,4,5,6,7,8]
# ar2 = []

# вариант 1
# for i in arr:
#     ar2.append(i*2)
# print(ar2)

# метод list
# print(list("rerearr"))

# вариант 2
# метод map используется для применения функции к каждому элементу (объекта , массива , списка)
# ar2 = list(map(lambda x : x*2,arr))

# вариант 3
# def f (x):
#     print(x)
#     return x*2
# метод map используется для применения функции к каждому элементу (объекта , массива , списка)
# ar2 = list(map(f,arr))





# метод filter
# метод filter это как метод map , но только фильтрует каждый элемент
# def f (x):
#     if(x%2 == 0):
#         return True
#     return False
# ar2 = list(filter(f,arr))



# метод filter лучше работает с лямбдой
# ar2 = list(filter(lambda x : x%2 == 0 and x != 6,arr))

# print(arr)
# print(ar2)






# пример работы с методами map и filter
arr = [
    [1,2,3,4,5,6,7,8],
    [1,2,3,4,5,6,7,8],
    [1,2,3,4,5,6,7,8],
    [1,2,3,4,5,6,7,8],
]
arr = list(map(lambda x : list(filter(lambda s : s==5 , x)),arr))
print(arr)


