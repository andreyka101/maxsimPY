from tkinter import *
 
root = Tk()
root.geometry('600x500')
 
canV = Canvas(width=400, height=400, bg='white')
canV.pack()
 
# canV.create_rectangle(10, 10, 190, 70,fill='yellow', outline='white')
canV.create_line(10, 10, 190, 70 , width=3 )
# canV.create_polygon(10, 10, 190, 70 , 20, 300 , fill='yellow')

# canV.create_oval(10,10, 160, 160 ,fill='yellow')
canV.create_text(100, 100, 
              text="Hello World,\nPython\nand Tk",
              justify=CENTER, font="Verdana 14", fill="#404040")
canV.create_rectangle(0, 0, 400, 400,fill='white', outline='white')
canV.create_line(10, 10, 190, 70 , width=3 )


# canV.create_arc
 
root.mainloop()
# # canV.place()