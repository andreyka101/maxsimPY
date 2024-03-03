from tkinter import *
from tkinter import ttk
window = Tk()

def fun():
    tex.configure(text=comboBox.get())

window.title("Listbox")
# меняем ширину и высоту окна 
window.geometry('400x250')

arr = ["Python", "JavaScript", "C#", "Java"]
comboBox = ttk.Combobox(values=arr)
comboBox.place(x=0 , y = 0)




tex = Label(text="")
tex.place(h=61 , w=61 , x=170 , y = 15)

button = Button(text="run", command=fun)
button.place(h=61 , w=61 , x=170 , y = 115)

window.mainloop()