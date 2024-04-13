from tkinter import *
window = Tk()
moveY = 0
moveX = 0


def keyPress(event):
    global moveY
    global moveX
    text.config(text=event)
    if (event.keysym == "Down"):
        if(moveY < 450):
            moveY += 50
        robot.config(bg = "#3dffc5" )
    if (event.keysym == "Up"):
        if(moveY > 0):
            moveY -= 50
        robot.config(bg = "#3dffc5" )
    if (event.keysym == "Left"):
        if(moveX > 0):
            moveX -= 50
        robot.config(bg = "#3dffc5" )
    if (event.keysym == "Right"):
        if(moveX < 550):
            moveX += 50
        robot.config(bg = "#3dffc5" )
    robot.place(y = moveY , x = moveX)


def keyRelease(event):
    text.config(text=event)
    robot.config(bg = "red")


window.title("keyboard")
window.geometry('600x500')

window.bind("<KeyPress>" , keyPress)
window.bind("<KeyRelease>" , keyRelease)

robot = Label(bg = "red")
robot.place(h=50 , w=50 , x=0 , y = 0)

text = Label(text="ответ:", font='Times 15')
text.place(h=20 , x=170 , y = 85)


window.mainloop()