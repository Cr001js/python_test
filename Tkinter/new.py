# This code is made by Tkinter library and if you push the show response 
# button it will print the response


# Required modules :)
from tkinter import *
import requests


# Explaining functions ¯\_(ツ)_/¯
def p ():
    r = requests.get('https://icc-aria.ir/courses/%D8%B1%D8%A7%D8%A8%D8%B7-%DA%AF%D8%B1%D8%A7%D9%81%DB%8C%DA%A9%DB%8C-tkinter-%D9%BE%D8%A7%DB%8C%D8%AA%D9%88%D9%86/episode/%D8%A7%D8%B3%D8%AA%D9%81%D8%A7%D8%AF%D9%87-%D8%A7%D8%B2-%DA%A9%D9%84%DB%8C%D8%AF-%D8%AF%D8%B1-%D8%B9%D9%85%D9%84')
    print(r)
def pr ():
    print(r)


# making Tkinter window ｡^‿^｡
window = Tk()
window.title('First App')
window.geometry('400x400')
Label(window, text = 'click to get response').pack()
b = Button(window)
b.configure(text = 'Respone', bg = 'white',command= p)
b.pack()
window.mainloop()