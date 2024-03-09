from tkinter import *
 
root = Tk()
root.title("METANIT.COM")
root.geometry("250x200")


def fun():
    # tex.configure(text=listBox.curselection())
    # listBox.delete(listBox.curselection())
    # tex.configure(text=listBox.get(listBox.curselection()))
    listBox.insert(listBox.curselection(),"2")
    # tex.configure(text=listBox.size())

    

 
arr = ["Python", "JavaScript", "C#", "Java", "JavaScript", "C#", "Java", "JavaScript", "C#", "Java", "JavaScript", "C#", "Java", "JavaScript", "C#", "Java", "JavaScript", "C#", "Java"]
 
listBox = Listbox(listvariable=Variable(value=arr),selectmode=EXTENDED)
listBox.pack( x=0 , y = 0,  padx=5, pady=5)
#  anchor=NW,
                  

scrollbar = Scrollbar(orient="vertical", command=listBox.yview)
scrollbar.pack(side=RIGHT, fill=Y)
listBox["yscrollcommand"]=scrollbar.set



tex = Label(text="")
tex.place(h=61 , w=61 , x=170 , y = 45)

button = Button(text="run", command=fun)
button.place(h=61 , w=61 , x=170 , y = 115)

ent = Entry(text="ответ:")
ent.place(h=31 , w=71 , x=170 , y = 10)
 
root.mainloop()