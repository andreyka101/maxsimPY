# импортируем библиотеку tkinter
from tkinter import *

# функция которая должна вызываться при нажатии на кнопку
def click():
    # изменяем текст Label
    # inp.get() берём текст из Entry (input)
    text.configure(text=inp.get())

def printGeometry():
    text.configure(text=window.geometry())

# создаём окно 
window = Tk()
# меняем название окна
window.title("12345")
# меняем ширину и высоту окна 
window.geometry('400x250')

# создаём текст
text = Label(text=window.geometry(), padx=60, pady=30)
text.grid(column=0, row=0)

# создаём ввод (input)
# inp = Entry(width=10)
# inp.grid(column=0, row=1)

# создаём кнопку                     command вызывает функцию
button = Button(text="Не нажимать!", command=printGeometry)
button.place(x=50,y=50)

# метод mainloop() оставляет окно открытым
window.mainloop()