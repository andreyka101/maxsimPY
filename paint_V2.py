from tkinter import *
window = Tk()
click_test = False
num_oval = 1
color_line = 'black'
old_coordinates = [0,0]


def motion(event):
    global click_test , num_oval , color_line
    х,y = window.winfo_pointerxy()
    widget = window.winfo_containing(х,y)
    x = event.x
    y = event.y
    window.title(str(x) + " : " + str(y))

    if click_test and num_oval == 3:
        canV.create_line(old_coordinates[0],old_coordinates[1], x, y ,fill=color_line, width=num_oval )
    if click_test and num_oval == 50:
        canV.create_oval(x-num_oval,y-num_oval, x+num_oval, y+num_oval ,fill=color_line ,  outline=color_line)

    old_coordinates[0] = x
    old_coordinates[1] = y


def keyPress(event):
    global num_oval , click_test , color_line
    if (event.keysym == "space"):
        num_oval = 3
        color_line = 'black'
        click_test = True
    if (event.keysym == "Control_L"):
        num_oval = 50
        color_line = 'white'
        click_test = True
    х,y = window.winfo_pointerxy()
    x = event.x
    y = event.y
    # canV.create_oval(x-num_oval,y-num_oval, x+num_oval, y+num_oval ,fill=color_line ,  outline=color_line)

def keyRelease(event):
    global click_test
    if (event.keysym == "space"):
        click_test = False
    if (event.keysym == "Control_L"):
        click_test = False


 
canV = Canvas(width=700, height=500, bg='white')
# canV.create_oval(9,9, 11, 11 ,fill='black')
canV.pack()





window.title("mouse")
window.geometry('700x500')
window.resizable(False, False)

window.bind("<Motion>" , motion)

window.bind("<KeyPress>" , keyPress)
window.bind("<KeyRelease>" , keyRelease)



window.mainloop()