from tkinter import *
window = Tk()

click = False

def motion(event):
    x = event.x
    y = event.y
    winх,winy = window.winfo_pointerxy()
    widget = window.winfo_containing(winх,winy)
    if (str(widget) == ".!button"):
        widget.place(x=float(winх) - x , y = float(winy) - y)



def butL(event):
    click = True



window.title("mouse")
window.geometry('400x250')

window.bind("<Motion>" , motion)
window.bind("<Button-1>" , butL)

text = Button(text="move")
text.place(h=20 , x=170 , y = 85)


window.mainloop()