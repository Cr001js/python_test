# This code takes two numbers from the user and multiplies them together :)))
# I have written this code with the help of Tkinter (=^ェ^=)

from tkinter import *

window = Tk()
window.title('multiplication')

def multiplication():
    n1 = num1.get()
    n2 = num2.get()
    n1 = int(n1)
    n2 = int(n2)
    m = n1 * n2
    multiplication_lb.config(text = 'Multiplied number: %i ' % m, fg = 'green')

Label(window, text = 'enter number 1').pack()
num1 = Entry(window)
num1.pack()

Label(window, text = 'enter number 2').pack()
num2 = Entry(window)
num2.pack()

Button(window, text = 'do multiplication', command= multiplication).pack()

multiplication_lb = Label(window, text = 'no Multiplied number', fg = 'red')
multiplication_lb.pack()

window.geometry('400x400')
window.mainloop()