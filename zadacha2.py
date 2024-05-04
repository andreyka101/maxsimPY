# a=int(input())
import random
a=10000
a1=0
c=[]
while a1!=a:
    c.append(random.randint(1, 100000))
    a1+=1
bb=0
while c!=[]:
    a=c[0]
    c.remove(a)
    vv=0
    for i in c:
        if a!=0 and i>=a and i>0:
            c[vv]=i-1
        vv+=1
    a=a-1
    if a>=0:
        c.append(a)
    bb+=1
print(bb)
#Превышен лимит времени исполнения
# 2.22 - 2.23