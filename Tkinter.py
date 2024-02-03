from tkinter import *
a=0
def click():
    text.configure(text=inp.get())

window = Tk()
window.title("12345")
window.geometry('400x250')

text = Label(window,text="Привет", padx=60, pady=30)
text.grid(column=0, row=0)

inp = Entry(window,width=10)
inp.grid(column=0, row=1)

button = Button(window,text="Не нажимать!", command=click)
button.grid(column=1, row=1)

# .place(x=50,y=50)




window.mainloop()