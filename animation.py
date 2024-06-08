import time 
from tkinter import *
start = time.time()
timePassed = time.time() - start
def time_fun():
    return time.time() - start

 
root = Tk()
root.geometry('600x500')
 
canV = Canvas(width=600, height=600, bg='white')
canV.pack()
 
canV.create_rectangle(10  + timePassed * 10, 10, 190  + timePassed * 10, 70,fill='yellow', outline='white')

while(timePassed <= 2000):
    # print(timePassed)
    timePassed = time_fun()
    canV.update()
    canV.create_rectangle(10  + timePassed * 10, 10, 190  + timePassed * 10, 70,fill='yellow', outline='white')

 


 
root.mainloop()