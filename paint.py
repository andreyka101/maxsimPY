from tkinter import *
window = Tk()


def motion(event):
    х,y = window.winfo_pointerxy()
    widget = window.winfo_containing(х,y)
    x = event.x
    y = event.y
    window.title(str(x) + " : " + str(y))
    canV.create_oval(x-1,y-1, x+1, y+1 ,fill='black')


 
canV = Canvas(width=700, height=500, bg='white')
# canV.create_oval(9,9, 11, 11 ,fill='black')
canV.pack()





window.title("mouse")
window.geometry('700x500')
window.resizable(False, False)

window.bind("<Motion>" , motion)
# window.bind("<Button-1>" , butL)



window.mainloop()