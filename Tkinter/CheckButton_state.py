from tkinter import *


window = Tk()
window.title('Checkbutton')

def get_state() :
    print('state is: ', male_val.get())



male_val = IntVar()
Checkbutton(window, text = 'male', variable = male_val).pack()

Button(window, text = 'Show State', command = get_state).pack()

window.geometry('300x300')
window.mainloop()