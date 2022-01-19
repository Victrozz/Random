from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Fuck off")



def onClickNo():
    Label(root, text=">:) you cant stop me!").grid(row=2, column=0)

def onClickMeToo():
    Label(root, text="what the actual fuck dude thats like not even funny").grid(row=2, column=0)

# Creating Label Widgets
textLabel = Label(root, text="i fucked your dad")

# Creating Button Widgets
simpleButton = Button(root, text="Noooo!", padx=50, command=onClickNo)
simpleButton2 = Button(root, text="Me too", padx=50, command=onClickMeToo)

textLabel.grid(row=0, column=0)
simpleButton.grid(row=1, column=0)
simpleButton2.grid(row=1, column=1)

root.mainloop() 