from tkinter import *

import requests as requests

window = Tk()
# add widgets here


window.title('Hello Python')
window.geometry("300x200+10+20")
r = requests.get('http://127.0.0.1:8000/api/')

i = 0
for invoice in r.json():
    lbl = Label(window, text=invoice['car']['model']['name'], fg='white', font=("Helvetica", 20))
    lbl.place(x=5, y=5 + i * 30)
    i += 1


btn = Button(window, text="This is Button widget", fg='white', font=("Helvetica", 20))


def change():
    lbl.destroy()


btn.config(command=change)
btn.place(x=5, y=5 + i * 30)
window.mainloop()
