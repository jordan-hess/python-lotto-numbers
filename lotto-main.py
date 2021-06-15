from tkinter import *
from tkinter import messagebox
import random
import requests

root = Tk()
root.title("Lotto Draw")
root.config(bg="yellow")
root.geometry("700x700")
# image
img = PhotoImage(file="7c7d04d6-daily_lotto_results_numbers-removebg-preview.png")
Label(root, image=img, bg="yellow", height="300").place(x=-130, y=-150)
# header
head_lbl = Label(root, text="Welcome!", font="bold", bg="yellow").place(x=450, y=40)
head_lbl2 = Label(root, text="Please select your numbers", font="bold", bg="yellow").place(x=380, y=70)

# Your number selection
entry1 = Entry(root, text="", bg="blue", justify="center", font=(70))
entry1.place(x=50, y=140, width="80", height="80")
entry2 = Entry(root, text="", bg="red", justify="center", font=(70))
entry2.place(x=150, y=140, width="80", height="80")
entry3 = Entry(root, text="", bg="green", justify="center", font=(0))
entry3.place(x=250, y=140, width="80", height="80")
entry4 = Entry(root, text="", bg="purple", justify="center", font=(70))
entry4.place(x=350, y=140, width="80", height="80")
entry5 = Entry(root, text="", justify="center", font=(70))
entry5.place(x=450, y=140, width="80", height="80")
entry6 = Entry(root, text="", bg="light green", justify="center", font=(70))
entry6.place(x=550, y=140, width="80", height="80")


# defined all entries under 1 button , all functions of confirm button
def confirm():
    try:
        int(entry1.get())
    except ValueError:
        messagebox.showerror(message="That is not a number, make sure all entries are filled")

def confirm():
    try:
        int(entry2.get())
    except ValueError:
        messagebox.showerror(message="That is not a number, make sure all entries are filled")

def confirm():
    try:
        int(entry3.get())
    except ValueError:
        messagebox.showerror(message="That is not a number, make sure all entries are filled")

def confirm():
    try:
        int(entry4.get())
    except ValueError:
        messagebox.showerror(message="That is not a number or you are missing a number")

def confirm():
    try:
        int(entry5.get())
    except ValueError:
        messagebox.showerror(message="That is not a number or you are missing a number")

def confirm():
    try:
        int(entry6.get())
        messagebox.showinfo(message="Numbers Confirmed ;)")
    except ValueError:
        messagebox.showerror(message="That is not a number, make sure all entries are filled")


# Play button
play_btn = Button(root, text="Confirm Your Numbers", command=confirm, bg="yellow", bd=5).place(x=255, y=230)


def lotto_no():
    o = random.randint(1, 49)
    t = random.randint(1, 49)
    r = random.randint(1, 49)
    f = random.randint(1, 49)
    i = random.randint(1, 49)
    s = random.randint(1, 49)
    # assigned values into variables
    num1.set(o)
    num2.set(t)
    num3.set(r)
    num4.set(f)
    num5.set(i)
    num6.set(s)
    return


#variables for random draw
num1 = StringVar()
num2 = StringVar()
num3 = StringVar()
num4 = StringVar()
num5 = StringVar()
num6 = StringVar()

var = StringVar()
var.set("Lotto Draw")
# winning numbers
lot_no_ent1 = Entry(root, textvariable=num1, font=(30), justify="center", bg="brown")
lot_no_ent1.place(x=50, y=280, width="80", height="80")
lot_no_ent2 = Entry(root, textvariable=num2, font=(30), justify="center", bg="purple")
lot_no_ent2.place(x=150, y=280, width="80", height="80")
lot_no_ent3 = Entry(root, textvariable=num3, font=(30), justify="center", bg="pink")
lot_no_ent3.place(x=250, y=280, width="80", height="80")
lot_no_ent4 = Entry(root, textvariable=num4, font=(30), justify="center", bg="blue")
lot_no_ent4.place(x=350, y=280, width="80", height="80")
lot_no_ent5 = Entry(root, textvariable=num5, font=(30), justify="center", bg="red")
lot_no_ent5.place(x=450, y=280, width="80", height="80")
lot_no_ent6 = Entry(root, textvariable=num6, font=(30), justify="center", bg="green")
lot_no_ent6.place(x=550, y=280, width="80", height="80")

# Random numbers button
win_btn = Button(root, text="Generate winning numbers", command=lotto_no, bg="yellow", bd=5)
win_btn.place(x=240, y=370)
# winnings area
lbl_money = Label(root, text="Dividends: ", font="40", bg="yellow")
lbl_money.place(x=50, y=440)
lbl_6 = Label(root, text="6 correct numbers -     R10,000,000.00", font="40", bg="yellow")
lbl_6.place(x=50, y=465)
lbl_5 = Label(root, text="5 correct numbers -     R8,584.00", font="40", bg="yellow")
lbl_5.place(x=50, y=485)
lbl_4 = Label(root, text="4 correct numbers -     R2,385.00", font="40", bg="yellow")
lbl_4.place(x=50, y=505)
lbl_3 = Label(root, text="3 correct numbers -     R100.50", font="40", bg="yellow")
lbl_3.place(x=50, y=525)
lbl_2 = Label(root, text="2 correct numbers -     R20.00", font="40", bg="yellow")
lbl_2.place(x=50, y=545)
lbl_1 = Label(root, text="1 correct numbers -     R0", font="40", bg="yellow")
lbl_1.place(x=50, y=565)
lbl_0 = Label(root, text="0 correct numbers -     R0", font="40", bg="yellow")
lbl_0.place(x=50, y=585)
# Your total amount gained
lbl_ttl = Label(root, text="Total amount won: ", font="40", bg="yellow")
lbl_ttl.place(x=50, y=625)
ent_ttl = Entry(root, bg="yellow" , text="converted amount")
ent_ttl.place(x=240, y=645)

# currency converter
def convert():
    pass

amount_ent = Entry(root, text="R", bg="yellow")
amount_ent.place(x=240, y=625)
# convert button
convert_btn = Button(root, text="convert to :", command=convert)
# exit button
button_exit = Button(text="X", command="exit" , bg="red")
button_exit.place(x=650, y=0, width=50, height=40)
# play again button
def play():
   entry1.delete(0, END)
   entry2.delete(0, END)
   entry3.delete(0, END)
   entry4.delete(0, END)
   entry5.delete(0, END)
   entry6.delete(0, END)
   lot_no_ent6.delete(0, END)
   lot_no_ent2.delete(0, END)
   lot_no_ent3.delete(0, END)
   lot_no_ent4.delete(0, END)
   lot_no_ent5.delete(0, END)
   lot_no_ent1.delete(0, END)

play_ag_btn = Button(root, text="Play Again", command=play, bg="yellow", bd=5).place(x=145, y=230)


root.mainloop()
