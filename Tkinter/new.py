from tkinter import *

window = Tk()

window.title('online status')

hello_count = Label(window, text= 'count: ')
hello_count.pack()

btn = Button(window)

btn.configure(text= 'Click me', fg = 'blue')

btn.pack()

window.geometry('400x400')

window.mainloop()