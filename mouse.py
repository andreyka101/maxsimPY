from tkinter import *
window = Tk()

def motion(event):
    x = event.x
    y = event.y
    window.title(str(x) + " : " + str(y))
def b1(event):
    # text.config(text=event)
    text.config(text="b1")
def b2(event):
    text.config(text="b2")
def b3(event):
    text.config(text="b3")


window.title("mouse")
window.geometry('400x250')

window.bind("<Motion>" , motion)
window.bind("<Button-1>" , b1)
window.bind("<Button-2>" , b2)
window.bind("<Button-3>" , b3)

text = Label(text="ответ:")
text.place(h=11 , x=170 , y = 85)


window.mainloop()