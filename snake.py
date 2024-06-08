import time 
from tkinter import *
start = time.time()
timePassed = time.time() - start
speed = 10


def time_fun():
    return time.time() - start
def keyPress(event):
    # canV.config(bg="black")
    # if (event.keysym == "Left"):
    if (event.keysym == "Right"):
        canV.create_rectangle(0, 0, 600, 500,fill='white', outline='white')
        canV.create_rectangle(0  + timePassed * speed, 0, 50  + timePassed * speed, 50,fill='black', outline='green')

 
root = Tk()
root.geometry('600x500')
 
canV = Canvas(width=600, height=600, bg='white')
canV.pack()
 
canV.create_rectangle(0  + timePassed * speed, 0, 50  + timePassed * speed, 50,fill='green', outline='green')

while(timePassed <= 2000):
    # print(timePassed)
    timePassed = time_fun()
    canV.update()
    root.bind("<KeyPress>" , keyPress)
    # canV.create_rectangle(0, 0, 600, 500,fill='white', outline='white')
    # canV.create_rectangle(0  + timePassed * speed, 0, 50  + timePassed * speed, 50,fill='green', outline='green')

    # def keyPress(event):
    #     global moveY
    #     global moveX
    #     global boxPositionY
    #     global boxPositionX
    #     # text.config(text=event)
    #     if (event.keysym == "Down"):
    #         if(moveY < 450):
    #             moveY += 50
    #         robot.config(bg = "#3dffc5" )
    #     if (event.keysym == "Up"):
    #         if(moveY > 0):
    #             moveY -= 50
    #         robot.config(bg = "#3dffc5" )
    #     if (event.keysym == "Left"):
    #         if(moveX > 0):
    #             moveX -= 50
    #         robot.config(bg = "#3dffc5" )
    #     if (event.keysym == "Right"):
    #         if(moveX < 550):
    #             moveX += 50
    #         robot.config(bg = "#3dffc5" )

        



root.bind("<KeyPress>" , keyPress)
# root.bind("<KeyRelease>" , keyRelease)

 


 
root.mainloop()