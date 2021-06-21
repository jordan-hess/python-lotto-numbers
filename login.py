import datetime
from tkinter import *
from dateutil import relativedelta
import rsaidnumber
from playsound import playsound

root = Tk()
root.title("Login")
from tkinter import messagebox

# usernames and passwords
userList = ["jordan", "godwin"]
passwList = ["123", "closethelaptops"]
id_sa_num = []

frame3 = Frame(root, bd=2, width=200, bg="yellow")
frame3.grid(row=0, column=1)

frame5 = Frame(root, bd=2, bg="yellow")
frame5.grid(row=1, column=1)


def login():
    global loginUsername
    global loginPassword
    global IdNumber
    if loginUsername.get() in userList and loginPassw.get() in passwList:
        User = userList.index(loginUsername.get())
        Passw = passwList.index(loginPassword.get())
        Id_num = IdNumber.get()
        int(loginPassword.get())
        birthDay = rsaidnumber.parse(Id_num).date_of_birth
        if User == Passw == Id_num:
            frame3.grid_forget()
            frame5.grid_forget()
            playsound("windows_10_system_generic_notification_sound_mp3_44661.mp3")
        elif relativedelta.relativedelta(datetime.datetime.today(), birthDay).years >= 18:
            messagebox.showinfo(message="welcome")
            playsound("windows_10_system_generic_notification_sound_mp3_44661.mp3")
            root.destroy()
            import lotto
        else:
            messagebox.showerror(message="you are not old enough to play")
            playsound("windows_10_system_generic_notification_sound_mp3_44661.mp3")

    else:
        messagebox.showerror(message="password or username is invalid, try again")
        playsound("windows_10_system_generic_notification_sound_mp3_44661.mp3")


loginLabelUser = Label(frame3, text="Log in:", bg="yellow")
loginLabelUser.pack(anchor=W)

loginUser = StringVar()
loginUsername = Entry(frame3, textvariable=loginUser, width=40)
loginUsername.pack(anchor=W)

loginLabelPassw = Label(frame3, text="Password:", bg="yellow")
loginLabelPassw.pack(anchor=W)

loginPassw = StringVar()
loginPassword = Entry(frame3, textvariable=loginPassw, width=40)
loginPassword.pack()

IdLabel = Label(frame3, text="ID Number", bg="yellow")
IdLabel.pack(anchor=W)

IdNumber = StringVar()
IdNumber = Entry(frame3, textvariable=id_sa_num, width=40)
IdNumber.pack()

# button to login, this will start the function login()
button = Button(frame3, text="Continue...", command=login)
button.pack()

# Checking age by using ID


root = mainloop()