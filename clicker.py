from tkinter import *
click = 0
def clicer():
    global click
    click+=1
    # TODO с помощью метода configure я меняю текст кнопки
    button.configure(text=click)

# создаём окно 
window = Tk()
# меняем название окна
window.title("clicker")
window.configure(bg = '#33c5ff')
# меняем ширину и высоту окна 
window.geometry('400x250')
button = Button(text="0", command=clicer , 
                bg = "#910000" , 
                fg="#f2ff66" , 
                activebackground='#f2ff66',
                activeforeground = "#910000",
                font="Verdana 22",
                border = "0"
                )

button.place(h=61 , w=61 , x=170 , y = 95)

window.mainloop()

