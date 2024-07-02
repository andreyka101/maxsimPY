import time 
from tkinter import *
import random
start = time.time()
timePassed = time.time() - start
speed = 50
move_snake = "Right"
move_snake_old = "Right"
move_snake_number_XY = {
    "x1":50,
    "y1":0,
    "x2":100,
    "y2":50,
}
arr_move_snake_number = [
     {
     "move_snake_number_x" : 0,
     "move_snake_number_y" : 0,
},
]
move_snake_number_wh = 50
timePassed_old = 0

applePositionY = 50 * random.randint(0, 9)
applePositionX = 50 * random.randint(0, 11)



def time_fun():
    return time.time() - start
def keyPress(event):
    global move_snake
    # canV.config(bg="black")
    move_snake = event.keysym
    # if (event.keysym == "Left"):
    # if (event.keysym == "Down"):
    #     canV.create_rectangle(0, 0, 600, 500,fill='white', outline='white')
    #     canV.create_rectangle(0  + timePassed * speed, 0, 50  + timePassed * speed, 50,fill='black', outline='green')

 
root = Tk()
root.geometry('600x500')
 
canV = Canvas(width=600, height=500, bg='white')
text_l = Label(text="ответ:")
canV.pack()
 
canV.create_rectangle(arr_move_snake_number[0]["move_snake_number_x"], arr_move_snake_number[0]["move_snake_number_y"], arr_move_snake_number[0]["move_snake_number_x"] + move_snake_number_wh, arr_move_snake_number[0]["move_snake_number_y"] + move_snake_number_wh,fill='green', outline='green')

canV.create_rectangle(applePositionX, applePositionY, applePositionX + move_snake_number_wh, applePositionY + move_snake_number_wh,fill='green', outline='green')

while(timePassed <= 2000):
    timePassed_old = timePassed
    timePassed = time_fun()
    print(timePassed , timePassed_old)
    # print(round(timePassed) * speed)
    canV.update()
    root.bind("<KeyPress>" , keyPress)
    print(move_snake)
    if(move_snake == "Right" and round(timePassed_old) != round(timePassed)):
            if(move_snake_old == "Left"):
                arr_move_snake_number[0]["move_snake_number_x"] -= speed
                if(arr_move_snake_number[0]["move_snake_number_x"]<0):
                    arr_move_snake_number[0]["move_snake_number_x"] = 550
            else: 
                arr_move_snake_number[0]["move_snake_number_x"] += speed
                if(arr_move_snake_number[0]["move_snake_number_x"]>550):
                    arr_move_snake_number[0]["move_snake_number_x"] = 0
                move_snake_old = move_snake
    if(move_snake == "Left" and round(timePassed_old) != round(timePassed)):
            if(move_snake_old == "Right"):
                arr_move_snake_number[0]["move_snake_number_x"] += speed
                if(arr_move_snake_number[0]["move_snake_number_x"]>550):
                    arr_move_snake_number[0]["move_snake_number_x"] = 0
            else: 
                arr_move_snake_number[0]["move_snake_number_x"] -= speed
                if(arr_move_snake_number[0]["move_snake_number_x"]<0):
                    arr_move_snake_number[0]["move_snake_number_x"] = 550
                move_snake_old = move_snake
    elif(move_snake == "Down" and round(timePassed_old) != round(timePassed)):
            if(move_snake_old == "Up"):
                arr_move_snake_number[0]["move_snake_number_y"] -= speed
                if(arr_move_snake_number[0]["move_snake_number_y"]<0):
                    arr_move_snake_number[0]["move_snake_number_y"] =450
            else: 
                arr_move_snake_number[0]["move_snake_number_y"] += speed
                if(arr_move_snake_number[0]["move_snake_number_y"]>450):
                    arr_move_snake_number[0]["move_snake_number_y"] = 0
                move_snake_old = move_snake
    elif(move_snake == "Up" and round(timePassed_old) != round(timePassed)):
            if(move_snake_old == "Down"):
                arr_move_snake_number[0]["move_snake_number_y"] += speed
                if(arr_move_snake_number[0]["move_snake_number_y"]>450):
                    arr_move_snake_number[0]["move_snake_number_y"] = 0
            else:
                for i in range(len(arr_move_snake_number)):
                     
                arr_move_snake_number[0]["move_snake_number_y"] -= speed
                if(arr_move_snake_number[0]["move_snake_number_y"]<0):
                    arr_move_snake_number[0]["move_snake_number_y"] = 450
                move_snake_old = move_snake
    
    if(arr_move_snake_number[0]["move_snake_number_y"] == applePositionY and arr_move_snake_number[0]["move_snake_number_x"] == applePositionX):
        # canV.create_rectangle(arr_move_snake_number[0]["move_snake_number_x"], arr_move_snake_number[0]["move_snake_number_y"], arr_move_snake_number[0]["move_snake_number_x"] + move_snake_number_wh, arr_move_snake_number[0]["move_snake_number_y"] + move_snake_number_wh,fill='green', outline='green')
        if(move_snake == "Right"):
             arr_move_snake_number.append({
                "move_snake_number_x" : arr_move_snake_number[0]["move_snake_number_x"] - speed,
                "move_snake_number_y" : arr_move_snake_number[0]["move_snake_number_y"],
            })
        elif(move_snake == "Left"):
             arr_move_snake_number.append({
                "move_snake_number_x" : arr_move_snake_number[0]["move_snake_number_x"] + speed,
                "move_snake_number_y" : arr_move_snake_number[0]["move_snake_number_y"],
            })
        elif(move_snake == "Down"):
             arr_move_snake_number.append({
                "move_snake_number_x" : arr_move_snake_number[0]["move_snake_number_x"],
                "move_snake_number_y" : arr_move_snake_number[0]["move_snake_number_y"] - speed,
            })
        elif(move_snake == "Up"):
             arr_move_snake_number.append({
                "move_snake_number_x" : arr_move_snake_number[0]["move_snake_number_x"],
                "move_snake_number_y" : arr_move_snake_number[0]["move_snake_number_y"] + speed,
            })
        for i in arr_move_snake_number:
            while(i["move_snake_number_y"] == applePositionY and i["move_snake_number_x"] == applePositionX):
                applePositionY = 50 * random.randint(0, 9)
                applePositionX = 50 * random.randint(0, 11)
    canV.create_rectangle(0, 0, 600, 500,fill='white', outline='white')
    canV.create_arc(applePositionX, applePositionY, applePositionX + move_snake_number_wh, applePositionY + move_snake_number_wh,fill='red', outline='red',start=0,extent=359)
    for i in arr_move_snake_number:
        canV.create_rectangle(i["move_snake_number_x"], i["move_snake_number_y"], i["move_snake_number_x"] + move_snake_number_wh, i["move_snake_number_y"] + move_snake_number_wh,fill='green', outline='green')
    # canV.create_rectangle(0  + round(timePassed) * speed, 0, 50  + round(timePassed) * speed, 50,fill='green', outline='green')

        



root.bind("<KeyPress>" , keyPress)
# root.bind("<KeyRelease>" , keyRelease)

 


 
root.mainloop()