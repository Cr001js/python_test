# Required modules =)
from tkinter import *

# building a window
window = Tk()

#adding window title
window.title("Radiobutton test")

#making a list of all buttons we want
MODES = [('mmd', 'boy1'), ('abass', 'boy2'), ('ili', 'girl')]

#setting the first choosen one
v = StringVar()
v.set("name") # initialize

#making a loop to create we want to do
for text, mode in MODES:
    b = Radiobutton(window, text=text,variable=v, value=mode)
    b.pack(anchor=W)

#creating the loop for the program
window.mainloop()



