import time 
from tkinter import *
start = time.time()
timePassed = time.time() - start
speed = 50
move_snake = "Right"
move_snake_number_XY = {
    "x1":50,
    "y1":0,
    "x2":100,
    "y2":50,
}
move_snake_number_x = 0
move_snake_number_y = 0
move_snake_number_wh = 50
#FIXME - ghuhgrughgr
fg = 0



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
 
canV = Canvas(width=600, height=600, bg='white')
text_l = Label(text="ответ:")
canV.pack()
 
canV.create_rectangle(move_snake_number_x, move_snake_number_y, move_snake_number_x + move_snake_number_wh, move_snake_number_y + move_snake_number_wh,fill='green', outline='green')

while(timePassed <= 2000):
    # print(timePassed)
    timePassed = time_fun() - fg
    print(round(timePassed) * speed)
    canV.update()
    root.bind("<KeyPress>" , keyPress)
    if(move_snake == "Right"):
        # fg = 
        move_snake_number_x = round(timePassed) * speed
    elif(move_snake == "Down"):
        move_snake_number_y = round(timePassed) * speed
    canV.create_rectangle(0, 0, 600, 500,fill='white', outline='white')
    canV.create_rectangle(move_snake_number_x, move_snake_number_y, move_snake_number_x + move_snake_number_wh, move_snake_number_y + move_snake_number_wh,fill='green', outline='green')
    # canV.create_rectangle(0  + round(timePassed) * speed, 0, 50  + round(timePassed) * speed, 50,fill='green', outline='green')

        



root.bind("<KeyPress>" , keyPress)
# root.bind("<KeyRelease>" , keyRelease)

 


 
root.mainloop()