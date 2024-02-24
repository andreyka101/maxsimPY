from tkinter import *
def clicer():
    text.configure(text=checkData.get())
    if (checkData.get() == 1):
        window.configure(bg = '#26a110')
    else:
        window.configure(bg = '#33c5ff')
window = Tk()
window.title("clicker")
window.configure(bg = '#33c5ff')
window.geometry('400x250')
# button = Button(text="0", command=clicer )
# button.place(h=61 , w=61 , x=170 , y = 95)
checkData = IntVar()
# checkData = StringVar()
# checkData = BooleanVarVar()
# checkData = DoubleVar()

check = Checkbutton(text = "check" , variable=checkData , command=clicer)
check.place( x=0 , y = 5)

text = Label(text=checkData.get())
text.place(h=11 , x=0 , y = 40)




window.mainloop()