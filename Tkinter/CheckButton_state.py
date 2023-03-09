from tkinter import *


window = Tk()
window.title('Checkbutton')

def get_state() :
    s = male_val.get()
    if s == 1:
        lb.config(text = 'online', fg = 'green')
    elif s == 0:
        lb.config(text = 'offline', fg = 'red')



male_val = IntVar()
Checkbutton(window, text = 'connection', variable = male_val).pack()

Button(window, text = 'Show State', command = get_state).pack()

lb = Label(window, text = '', fg = 'red')
lb.pack()
window.geometry('300x300')
window.mainloop()