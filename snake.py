import time 
from tkinter import *
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
move_snake_number_x = 0
move_snake_number_y = 0
move_snake_number_wh = 50
timePassed_old = 0



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
 
canV.create_rectangle(move_snake_number_x, move_snake_number_y, move_snake_number_x + move_snake_number_wh, move_snake_number_y + move_snake_number_wh,fill='green', outline='green')

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
                  move_snake_number_x -= speed
            else: 
                move_snake_number_x += speed
                move_snake_old = move_snake
    if(move_snake == "Left" and round(timePassed_old) != round(timePassed)):
            if(move_snake_old == "Right"):
                  move_snake_number_x += speed
            else: 
                move_snake_number_x -= speed
                move_snake_old = move_snake
    elif(move_snake == "Down" and round(timePassed_old) != round(timePassed)):
            if(move_snake_old == "Up"):
                move_snake_number_y -= speed
                if(move_snake_number_y<0):
                    move_snake_number_y =450
            else: 
                if(move_snake_number_y>450):
                    move_snake_number_y =0
                move_snake_number_y += speed
                move_snake_old = move_snake
    elif(move_snake == "Up" and round(timePassed_old) != round(timePassed)):
            if(move_snake_old == "Down"):
                move_snake_number_y += speed
                if(move_snake_number_y>550):
                    move_snake_number_y =0
            else: 
                move_snake_number_y -= speed
                if(move_snake_number_y<0):
                    move_snake_number_y =450
                move_snake_old = move_snake
    canV.create_rectangle(0, 0, 600, 500,fill='white', outline='white')
    canV.create_rectangle(move_snake_number_x, move_snake_number_y, move_snake_number_x + move_snake_number_wh, move_snake_number_y + move_snake_number_wh,fill='green', outline='green')
    # canV.create_rectangle(0  + round(timePassed) * speed, 0, 50  + round(timePassed) * speed, 50,fill='green', outline='green')

        



root.bind("<KeyPress>" , keyPress)
# root.bind("<KeyRelease>" , keyRelease)

 


 
root.mainloop()