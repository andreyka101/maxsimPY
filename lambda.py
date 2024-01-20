# a = 1.3
# print(type(a))

# def func (x):
#     return x*2
# print(type(func))

# lam = lambda x: x*2 
# print(lam(3))
# print(type(lam))



# lam = lambda x , y: x*y
# print(lam(3,4))



# max_number = lambda a, b: "ок" if a > b else "yyyy"
# print(max_number(7, 5))


# f = lambda: 4
# f = lambda: True
# f = lambda: 'pip'
# print(f())



# arr = [1,2,3,4,5,6,7,8]
# ar2 = []


# for i in arr:
#     ar2.append(i*2)
# print(ar2)


# print(list("rerearr"))

# ar2 = list(map(lambda x : x*2,arr))



# def f (x):
#     print(x)
#     return x*2
# ar2 = list(map(f,arr))






# def f (x):
#     if(x%2 == 0):
#         return True
#     return False
# ar2 = list(filter(f,arr))



# def f (x):
#     if(x%2 == 0):
#         return True
#     return False
# ar2 = list(filter(lambda x : x%2 == 0 and x != 6,arr))

# print(arr)
# print(ar2)







arr = [
    [1,2,3,4,5,6,7,8],
    [1,2,3,4,5,6,7,8],
    [1,2,3,4,5,6,7,8],
    [1,2,3,4,5,6,7,8],
]
ar2 = list(map(lambda x : list(filter(lambda s : s==5 , x)),arr))
print(ar2)

