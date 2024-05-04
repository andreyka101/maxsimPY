# students_num = int(input())
import random
students_num = 10000
students_grade_arr = []
num = 0

def cheating_function(x):
    global grade
    if(x >= grade):
        return x-1
    return x


for i in range(students_num):
    students_grade_arr.append(random.randint(1, 100000))

print("*******************")
# print(students_grade_arr)
while students_grade_arr!=[]:
    num +=1
    if(students_grade_arr[0] == 0):
        students_grade_arr.pop(0)
    else:
        grade = students_grade_arr[0]
        students_grade_arr.pop(0)
        students_grade_arr = list(map(cheating_function , students_grade_arr))
        students_grade_arr.append(grade - 1)
    # print(students_grade_arr)

print("===============")
# print(students_grade_arr)
print("end",num)
# 1.18 - 1.19
    










# a=int(input())
# a1=0
# c=[]
# while a1!=a:
#     c.append(int(input()))
#     a1+=1
# bb=0
# while c!=[]:
#     a=c[0]
#     c.remove(a)
#     vv=0
#     for i in c:
#         if a!=0 and i>=a and i>0:
#             c[vv]=i-1
#         vv+=1
#     a=a-1
#     if a>=0:
#         c.append(a)
#     bb+=1
# print(bb)
#Превышен лимит времени исполнения