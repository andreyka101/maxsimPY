from tkinter import *
from tkinter import ttk
 
root = Tk()
root.title("METANIT.COM")
root.geometry("250x200")

def fun(getNum):
    int_value = round(float(getNum))
    text.config(text=int_value)
    text.place(x=int_value)


scale1 = ttk.Scale(orient=HORIZONTAL , length=200 , from_=1 , to=200 , command=fun)
scale1.pack()

text = Label(text="ответ:")
text.place(h=11 , x=0 , y = 85)

root.mainloop()