from tkinter import *
 
root = Tk()
root.title("METANIT.COM")
root.geometry("250x200")


def fun():
    # tex.configure(text=listBox.curselection())
    # listBox.delete(listBox.curselection())
    # tex.configure(text=listBox.get(listBox.curselection()))
    # listBox.insert(listBox.curselection(),"2")
    # tex.configure(text=listBox.size())

    listBox.insert(listBox.curselection(),ent.get())
    listBox.delete(listBox.curselection())
    ent.delete(0, END)

 
arr = ["Python", "JavaScript", "C#", "Java"]
 
listBox = Listbox(listvariable=Variable(value=arr))

#  anchor=NW,
listBox.pack( fill=X, padx=5, pady=5)

tex = Label(text="")
tex.place(h=61 , w=61 , x=170 , y = 15)

button = Button(text="run", command=fun)
button.place(h=61 , w=61 , x=170 , y = 115)

ent = Entry(text="ответ:")
ent.place(h=31 , w=71 , x=170 , y = 10)
 
root.mainloop()