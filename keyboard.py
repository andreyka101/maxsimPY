from tkinter import *
window = Tk()


def keyPress(event):
    text.config(text=event)
def keyRelease(event):
    text.config(text=event)


window.title("keyboard")
window.geometry('400x250')

window.bind("<KeyPress>" , keyPress)
window.bind("<KeyRelease>" , keyRelease)

text = Label(text="ответ:", font='Times 15')
text.place(h=20 , x=170 , y = 85)


window.mainloop()