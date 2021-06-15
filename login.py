from tkinter import *
from tkinter import messagebox

window = Tk()

name = ("Jordan Hess", "Zoe Erispe", "Jayden May", "Yumkela", "Godwin", "Austin Powers" )
email = ("jchno116012003@gmail.com", "zoeerispe7@gmail.com", "jaydenmay040@gmail.com", "yummykela@gmail.com" , "godwin.lifechoices.co.zo", "areyouhornybaby@gmail.com" )
ID_number = ("0301165062086")


class Login:
    def __init__(self, window):
        # window configuration
        self.window = window
        self.window.configure(bg="yellow")
        self.window.title("Lotto Draw: Jordan Hess")
        self.window.geometry("400x400")

        # Name Input
        self.lablenm = Label(window, text=" Full Name: ", bg="yellow")
        self.lablenm.pack()
        self.entrynm = Entry(window, textvariable=name)
        self.entrynm.pack()
        # Email input
        self.lableem = Label(window, text="Email: ", bg="yellow")
        self.lableem.pack()
        self.entryem = Entry(window, textvariable=email )
        self.entryem.pack()
        # Address input
        self.lableadd = Label(window, text="Address: ", bg="yellow")
        self.lableadd.pack()
        self.entryadd = Entry(window, text="", )
        self.entryadd.pack()
        # ID input
        self.lableid = Label(window, text="ID Number: ", bg="yellow")
        self.lableid.pack()
        self.entryid = Entry(window, textvariable=ID_number )
        self.entryid.pack()


# Submit button
def submit():
    if name == name:
        pass

    if email == email:
        pass
    else:
        messagebox.showinfo("Incorrect Email")

    if ID_number == ID_number:
        pass
    else:
        messagebox.showinfo("Incorrect Password")


sub_btn = Button(window, text="Submit" , width="10", command=submit)
sub_btn.pack()


log = Login(window)
window.mainloop()
