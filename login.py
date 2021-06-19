from tkinter import *
from tkinter import messagebox
import csv


# window configuration
window = Tk()
window.configure(bg="yellow")
window.title("Lotto Draw: Jordan Hess")
window.geometry("400x400")

# Email
eml_lbl = Label(window, text="Enter your Email: ").place(x=50, y=100)
eml_ent= Entry(window, textvariable=eml_lbl).place(x=180, y=100)

# Password
passw_lbl = Label(window, text="Enter you password: ").place(x=50, y=150)
passw_ent = Entry(window, text="", textvariable=passw_lbl).place(x=180, y=150)

def txt_fle():
    with open("user-txt") as file:
        file_reader = csv.reader(file)
        email_finder(file_reader)
        file.close()

eml_ent = StringVar()
passw_ent = StringVar()

# Submit button
def email_finder(file):
    for row in file:
        if row[0] == eml_ent:
            messagebox.showerror(message="Email not found")
            email_list = [row[0], row[1]]
            pass_check(email_list)
            break
        else:
            messagebox.showerror(message="Email not found")

def pass_check(email_list):
    if email_list[1] == passw_ent:
        messagebox.showinfo(message="password match")
    else:
        messagebox.showerror(message="password does not match")

def submit():
        if eml_ent.get() == email_finder and passw_ent.get() == pass_check:
            messagebox.showinfo(message="welocome")
        else:
            messagebox.showerror(message="email not recognised")


sub_btn = Button(window, text="Submit", width="10", command=submit)
sub_btn.pack()



window.mainloop()