# this code will get a request if you press the button =)

from tkinter import *
import requests




def Change_status() :
    r = requests.get('https://github.com/')
    s_l.config(text= 'status: response(200)', fg = 'green')
    r_l.config(text= 'response 200', fg = 'black')

window = Tk()
window.title('Github request status')


s_l = Label(window, text= 'status: requests not found', fg= 'red')
s_l.pack()

r_l = Label(window, text= '', fg= 'black')
r_l.pack()

Button(window, text= 'Click me', bg = 'white', command= Change_status).pack()

window.geometry('400x400')
window.mainloop()