from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Fuck off")
tri_maybe = Image.open("C:/Users/Victor/Documents/Python/GitHub/Random/scripts/Assets/rtriangle.png")
not_tri = tri_maybe.resize((300, 300))
tri = ImageTk.PhotoImage(not_tri)

# Creating Widgets
triLabel = Label(image=tri)
c1 = Entry(root, width=5)
c2 = Entry(root, width=5)
h = Entry(root, width=5)

# Gridding Widgets
triLabel.grid(row=0, column=1)
c1.grid(row=0, column=0)
c2.grid(row=1, column=1)
h.grid(row=0, column=2)

# Code
c1.insert(0, "c1")
c2.insert(0, "c2")
h.insert(0, "h")

# Event loop
root.mainloop()
