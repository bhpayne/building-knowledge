# http://effbot.org/tkinterbook/tkinter-hello-tkinter.htm

from Tkinter import *

root = Tk()

w = Label(root, text="Hello, world!")
w.pack()

root.mainloop()