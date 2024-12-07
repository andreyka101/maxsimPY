from tkinter import *
from PIL import Image, ImageTk
root = Tk()

# pip install Pillow

# image = Image.open("image.jpg")
image = Image.open("image_2.jpg")
# image = Image.open("happy.gif")
image.resize((500, 300))
# photo = [ImageTk.PhotoImage(file='mygif.gif',format = 'gif -index %i' %(i)) for i in range(100)]
photo = ImageTk.PhotoImage(image)

labImage = Label(image=photo)
labImage.place(x=0, y=0)
# labImage.pack()

root.mainloop()