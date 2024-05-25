from tkinter import *
window = Tk()
click_test = False
num_oval = 1
color_oval = 'black'


def motion(event):
    global click_test , num_oval , color_oval
    х,y = window.winfo_pointerxy()
    widget = window.winfo_containing(х,y)
    x = event.x
    y = event.y
    window.title(str(x) + " : " + str(y))
    if click_test:
        canV.create_oval(x-num_oval,y-num_oval, x+num_oval, y+num_oval ,fill=color_oval ,  outline=color_oval)


def keyPress(event):
    global num_oval , click_test , color_oval
    if (event.keysym == "space"):
        num_oval = 3
        color_oval = 'black'
        click_test = True
    if (event.keysym == "Control_L"):
        num_oval = 20
        color_oval = 'white'
        click_test = True
    х,y = window.winfo_pointerxy()
    x = event.x
    y = event.y
    canV.create_oval(x-num_oval,y-num_oval, x+num_oval, y+num_oval ,fill=color_oval ,  outline=color_oval)

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