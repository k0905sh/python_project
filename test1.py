from tkinter import *

def printHello():
    print('Hi')

root = Tk()

w=Label(root,text='Python Test')
b=Button(root,text='hello Python', command=printHello)
c=Button(root,text="Quit",command = root.quit)

w.pack()
b.pack()
c.pack()

root.mainloop()
