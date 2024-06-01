from tkinter import *
import time
window = Tk()
canV = Canvas(width=700, height=500, bg='white')
canV.pack()
coordinates = [10, 10, 190, 70]
canV.create_rectangle(coordinates[0], coordinates[1], coordinates[2], coordinates[3],fill='red', outline='white')
for i in range(20):
    canV.create_rectangle(0, 0, 700, 500,fill='white', outline='white')
    time.sleep(0.5)
    coordinates[0] += i
    coordinates[2] += i
    canV.create_rectangle(coordinates[0], coordinates[1], coordinates[2], coordinates[3],fill='red', outline='white')


window.mainloop()