from tkinter import *
window = Tk()

def fun():
    st = ent.get()
    text.configure(text= "ответ:" + st.swapcase())

window.title("input")
# меняем ширину и высоту окна 
window.geometry('400x250')
button = Button(text="run", command=fun)
button.place(h=61 , w=61 , x=170 , y = 115)

text = Label(text="ответ:")
text.place(h=11 , x=170 , y = 85)

ent = Entry(text="ответ:")
ent.place(h=31 , w=71 , x=170 , y = 10)

window.mainloop()