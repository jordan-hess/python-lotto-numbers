from tkinter import *
from tkinter import messagebox


root = Tk()
root.title("Banking Details")
root.config(bg="yellow")
root.geometry("400x400")

head_lbl = Label(root, text="Banking Details", font=(80), bg="yellow").place(x=130, y=50)
aac_nm_lbl = Label(root, text="Account Holder's Name: ", bg="yellow").place(x=30, y=150)
aac_nm_en = Entry(root, text="", bg="yellow").place(x=200, y=150)
aac_no_lbl = Label(root, text="Banking Number: ", bg="yellow").place(x=30, y=180)
aac_no_en = Entry(root, text="", bg="yellow").place(x=200, y=180)
bank_lbl = Label(root, text="Bank: ", bg="yellow").place(x=30, y=230)

options = ["Select..", "Capitec", "Nedbank", "FNB", "ABSA"]
variable = StringVar(root)
variable.set(options[0])
bank_menu = OptionMenu(root, variable, *options).place(x=200, y=225, width=90, height=25)

root.mainloop()
