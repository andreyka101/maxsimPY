number_pages=int(input())
lines=int(input())
print("------")
read_Pit = 0
read_Vas = 0
for i in range(1, number_pages+1):
    index = i
    if(index >= lines):
        index = int(i%lines)
    print(index)
    if(index != 0):
        read_Pit += index
        read_Vas += lines - index


print("------")
if read_Pit>read_Vas:
    print('Pit '+str(read_Pit-read_Vas))
elif read_Vas>read_Pit:
    print('Vas '+str(read_Vas-read_Pit))
else:
    print(0)







# lines_Pit=1
# page=0
# read_Pit=0
# read_Vas=0
# while page!=number_pages:
#     if read_Vas==0:
#         lines_Pit=1
#         b=lines-lines_Pit
#     read_Pit+=lines_Pit
#     read_Vas=read_Vas+lines-lines_Pit
#     b=lines-lines_Pit
#     lines_Pit+=1
#     page+=1
# if read_Pit>read_Vas:
#     print('Pit '+str(read_Pit-read_Vas))
# elif read_Vas>read_Pit:
#     print('Vas '+str(read_Vas-read_Pit))
# else:
#     print(0)
# #выдает неверный ответ