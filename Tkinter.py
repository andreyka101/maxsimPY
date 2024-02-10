# импортируем библиотеку tkinter
from tkinter import *

# функции которая должны вызываться при нажатии на кнопку
# def click():
#     # изменяем текст Label
#     # inp.get() берём текст из Entry (input)
#     text.configure(text=inp.get())

# def printGeometry():
    # text.configure(text=window.geometry())

click = 0
def clicer():
    global click
    click+=1
    # TODO с помощью метода configure я меняю текст кнопки
    button.configure(text=click)



# создаём окно 
window = Tk()
# меняем название окна
window.title("12345")
# меняем ширину и высоту окна 
window.geometry('400x250')

# window.geometry() выводит ширину и высоту окна
print(window.geometry())

# создаём текст
# text = Label(text=window.geometry(), padx=60, pady=30)
# text.pack(anchor="center")

# создаём ввод (input)
# inp = Entry(width=10)
# TODO все виды позиционирования элементов 
# inp.pack(expand=True)
# inp.pack(anchor="s", padx=100, pady=100)
# inp.pack(fill=X)
# inp.pack(fill=BOTH, expand=True)
# inp.pack(side=BOTTOM)

# создаём кнопку                     command вызывает функцию
# TODO padx=30, pady=30 задают толщину рамок блока
# button = Button(text="000000000", command=clicer , padx=30, pady=30)
button = Button(text="0", command=clicer , bg = "#910000")
# button.pack(expand=True)
# TODO h=60 , w=60 задают ширину и высоту блока
button.place(h=60 , w=60)
# button.pack(anchor="center")

# метод mainloop() оставляет окно открытым
window.mainloop()