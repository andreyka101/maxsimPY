from tkinter import *
window = Tk()


def motion(event):
    х,y = window.winfo_pointerxy()
    widget = window.winfo_containing(х,y)
    x = event.x
    y = event.y
    window.title(str(x) + " : " + str(y))
    text.config(text = window.winfo_pointerxy())


def butL(event):
    х,y = window.winfo_pointerxy()
    widget = window.winfo_containing(х,y)
    # if(x<250 and y<250):
    if(str(widget) == ".!label" or str(widget) == ".!label2" or str(widget) == ".!label3" or str(widget) == ".!label4"):
        widget.config(bg = "#f2dd22")
    


def butR(event):
    х,y = window.winfo_pointerxy()
    widget = window.winfo_containing(х,y)
    # if(x<250 and y<250):
    if(str(widget) == ".!label" or str(widget) == ".!label2" or str(widget) == ".!label3" or str(widget) == ".!label4"):
        widget.config(bg = "#888888")




window.title("mouse")
window.geometry('500x500')

window.bind("<Motion>" , motion)
window.bind("<Button-1>" , butL)
window.bind("<Button-3>" , butR)

block1 = Label(text="" , bg = "#2ac9a2")
block1.place(h=250 , w =250 , x=0 , y = 0)
block2 = Label(text="" , bg = "#2ac9a2")
block2.place(h=250 , w =500 , x=251 , y = 0)
block3 = Label(text="" , bg = "#2ac9a2")
block3.place(h=500 , w =250 , x=0 , y = 251)
block4 = Label(text="" , bg = "#2ac9a2")
block4.place(h=500 , w =500 , x=251 , y = 251)
text = Label(text="ответ:")
text.place(h=11 , x=170 , y = 85)


window.mainloop()