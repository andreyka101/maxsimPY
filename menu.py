from tkinter import *
window = Tk()
mainmenu = Menu(window)
window.config(menu=mainmenu)

def butt1():
    tex.config(text="1")
def butt2():
    tex.config(text="2")
def butt3():
    tex.config(text="3")

filemenu = Menu(mainmenu, tearoff=0)
filemenu.add_command(label="Открыть...")
filemenu.add_command(label="Новый")
filemenu.add_command(label="Сохранить...")
filemenu.add_command(label="Выход")

menu2 = Menu(mainmenu, tearoff=0)
menu2.add_command(label="1",command=butt1)
menu2.add_command(label="2",command=butt2)
menu2.add_command(label="3",command=butt3)

mainmenu.add_cascade(label="Файл", menu=filemenu)
mainmenu.add_cascade(label="123", menu=menu2)

tex = Label(text="")
tex.place(h=61 , w=61 , x=0 , y = 15)




window.mainloop()