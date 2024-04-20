from tkinter import *
import json
import random

window = Tk()

dataRead = open("file_robot.json","r").read()
file = json.loads(dataRead)
moveY = file['y']
moveX = file['x']

boxPositionY = 50 * random.randint(0, 11)
boxPositionX = 50 * random.randint(0, 9)


def keyPress(event):
    global moveY
    global moveX
    global boxPositionY
    global boxPositionX
    # text.config(text=event)
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
    if (boxPositionY == moveY and boxPositionX == moveX):
        boxPositionY = 50 * random.randint(0, 10)
        boxPositionX = 50 * random.randint(0, 8)
        box.place(x=boxPositionX, y=boxPositionY)
        text.config(text=str(boxPositionX) + " " + str(boxPositionY))

    with open("file_robot.json", "w") as file_X_Y:
        file_X_Y.write(json.dumps({
            "x": moveX,
            "y": moveY,
        }))


def keyRelease(event):
    # text.config(text=event)
    robot.config(bg = "red")


window.title("keyboard")
window.geometry('600x500')

window.bind("<KeyPress>" , keyPress)
window.bind("<KeyRelease>" , keyRelease)

robot = Label(bg = "red")
robot.place(h=50 , w=50 , x=moveX , y = moveY)

box = Label(bg = "#d5d900")
box.place(h=50 , w=50 , x=boxPositionX , y = boxPositionY)

text = Label(text="ответ:", font='Times 15')
text.place(h=20 , x=170 , y = 85)


window.mainloop()