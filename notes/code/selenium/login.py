from Tkinter import *

def login():
    master = Tk()
    Label(master, text="Username").grid(row=0)
    Label(master, text="Password").grid(row=1)

    user = Entry(master)
    password = Entry(master, show="*")

    user.grid(row=0, column=1)
    password.grid(row=1, column=1)

    Button(master, text='Login', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)

    mainloop()

    return user.get(), password.get()

if __name__ == '__main__':
    print login()