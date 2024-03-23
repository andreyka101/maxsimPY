from tkinter import *
from tkinter import ttk
 
root = Tk()
root.title("METANIT.COM")
root.geometry("250x200")

def five():
    progress.step(5)

def start():
    progress.start()

def stop():
    progress.stop()

runButton = Button(text="run", command=five)
runButton.place(h=61 , w=61 , x=1 , y = 1)

startButton = Button(text="start", command=start)
startButton.place(h=61 , w=61 , x=1 , y = 63)

stopButton = Button(text="stop", command=stop)
stopButton.place(h=61 , w=61 , x=1 , y = 130)




progress = ttk.Progressbar(orient="horizontal", maximum=100 , length=100, value=0)
progress.pack()


root.mainloop()