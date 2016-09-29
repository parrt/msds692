from Tkinter import *

master = Tk()
Label(master, text="Username").grid(row=0)
Label(master, text="Password").grid(row=1)

user = Entry(master)
password = Entry(master, show="*")

user.grid(row=0, column=1)
password.grid(row=1, column=1)

def login():
    print "hi"
    master.quit()

Button(master, text='Login', command=login).grid(row=3, column=0, sticky=W, pady=4)

mainloop()

print user.get(), password.get()