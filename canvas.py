from tkinter import *
 
root = Tk()
root.geometry('600x500')
 
canV = Canvas(width=600, height=600, bg='white')
canV.pack()
 
 #!SECTION урок 1
# canV.create_rectangle(10, 10, 190, 70,fill='yellow', outline='white')
# canV.create_line(10, 10, 190, 70 , width=3 )
# canV.create_polygon(10, 10, 190, 70 , 20, 300 , fill='yellow')

# canV.create_oval(10,10, 160, 160 ,fill='yellow')
# canV.create_text(100, 100, 
#               text="Hello World,\nPython\nand Tk",
#               justify=CENTER, font="Verdana 14", fill="#404040")
# canV.create_rectangle(0, 0, 400, 400,fill='white', outline='white')
# canV.create_line(10, 10, 190, 70 , width=3 )



 #!SECTION урок 2
# canV.create_rectangle(10, 10, 190, 70,fill='yellow', width=20)
# canV.create_oval(10,10, 160, 160 ,fill='yellow', width=10)


 #ANCHOR - line
# fill – цвет линии;
# width – толщина линии;
# stipple – шаблон заполнения линии;
# tags – набор тегов объекта.

# smooth=True
# canV.create_line(10, 10, 190, 50, 90,350,390,200,smooth=True,width=20,stipple='gray50')

# line_id = canV.create_line(10, 10, 200, 100, fill="red", tags=["line"])
# canV.addtag("figure", "withtag", line_id)


#ANCHOR - arc
# start – начальный угол дуги в градусах;
# extent – размер дуги в градусах. Дуга всегда рисуется в направлении 
# против часовой стрелки;
# width – толщина линии дуги;
# outline – цвет дуги;
# style – стиль графического объекта.

# canV.create_arc(50,50,300,300,start=180,extent=120,width=4,fill='green',style='pieslice')
# canV.create_arc(50,50,300,300,start=180,extent=120,width=4,fill='green',style='arc')
# canV.create_arc(50,50,300,300,start=180,extent=120,width=4,fill='green',style='chord')

canV.create_arc(50,50,300,300,start=180,extent=120,width=4,fill='green',style='chord')
canV.create_arc(50,50,300,300,start=0,extent=180,width=4,fill='red',style='chord')
canV.create_window


#ANCHOR - image
python_image = PhotoImage(file="image_4.png")
 
canV.create_image(300, 300, image=python_image)


# canV.create_arc
 
root.mainloop()
# # canV.place()