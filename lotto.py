from playsound import playsound
from tkinter import *
from tkinter import messagebox
import random
import requests
import tkinter as tk
from tkinter import ttk

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

entry1 = Entry(root, text="", bg="blue", justify="center", font=70)
entry1.place(x=50, y=140, width="80", height="80")
entry2 = Entry(root, text="", bg="red", justify="center", font=70)
entry2.place(x=150, y=140, width="80", height="80")
entry3 = Entry(root, text="", bg="green", justify="center", font=70)
entry3.place(x=250, y=140, width="80", height="80")
entry4 = Entry(root, text="", bg="purple", justify="center", font=70)
entry4.place(x=350, y=140, width="80", height="80")
entry5 = Entry(root, text="", justify="center", font=(70))
entry5.place(x=450, y=140, width="80", height="80")
entry6 = Entry(root, text="", bg="light green", justify="center", font=(70))
entry6.place(x=550, y=140, width="80", height="80")


def confirm():
    try:
        ent_list = [int(entry1.get()), int(entry2.get()), int(entry3.get()), int(entry4.get()), int(entry5.get()),
                    int(entry6.get())]
        ent_list.sort()
        return ent_list
    except ValueError:
        messagebox.showinfo(message="Fill in all entries")


def lotto_no():
    loto_list = random.sample(range(1, 49), 6)
    loto_list.sort()
    myresult.set(loto_list)
    return loto_list


def prizemoney():
    x = lotto_no()
    y = confirm()
    result = set(x).intersection(set(y))
    prize_mny = {6: "R10,000,000", 5: "R8,584", 4: "R2,384", 3: "R100.50", 2: "R20", 1: "R0", 0: "R0"}
    def claim():
        root.destroy()
        import banking_details

        # claim button
        claim_btn = Button(root, text="Claims", command=claim).place(x=200, y=200)
    mykey = len(result)
    x = {prize_mny.get(mykey)}
    if x == 0 or 1:
        playsound('sad_trombone_gaming_sound_effect_hd_mp3_32171.mp3')
    else:
        playsound('ka-ching_sound_effect_mp3_32039.mp3')
    messagebox.showinfo("you've won", x)




x = StringVar
myresult = StringVar()
my_lotto_num = Label(root, text=" ", textvariable=myresult, bg="yellow", borderwidth=3, font="70").place(x=240, y=340)


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


# currency converter
class my_currency_converter():
    def __init__(self, url):
        self.data = requests.get(url).json()
        self.currencies = self.data['rates']

    def convert(self, from_currency, to_currency, amount):
        initial_amount = amount
        if from_currency != 'USD':
            amount = amount / self.currencies[from_currency]

            # limiting the precision to 4 decimal places
        amount = round(amount * self.currencies[to_currency], 2)
        return amount


class App(tk.Tk):

    def __init__(self, converter):
        tk.Tk.__init__(self)
        self.title = ('Currency Converter')
        self.currency_converter = converter

        self.geometry("300x300")
        self.configure(bg="yellow")

        # Label
        self.intro_label = Label(self, text='Currency Convertor', bg='yellow')
        self.intro_label.config()

        self.intro_label.place(x=35, y=5)

        # Entry box
        self.amount_field = Entry(self, validate='key')
        self.converted_amount_field_label = Label(self, text='')

        # dropdown
        self.from_currency_variable = StringVar(self)
        self.from_currency_variable.set("ZAR")
        self.to_currency_variable = StringVar(self)
        self.to_currency_variable.set("USD")

        self.from_currency_dropdown = Label(self, text="ZAR", bg="yellow")
        self.to_currency_dropdown = ttk.Combobox(self, textvariable=self.to_currency_variable,
                                                 values=list(self.currency_converter.currencies.keys()))

        # placing
        self.from_currency_dropdown.place(x=50, y=100)
        self.amount_field.place(x=90, y=100)
        self.to_currency_dropdown.place(x=30, y=130, width="50")
        self.converted_amount_field_label.place(x=90, y=130, width="125")
        self.intro_label.place(x=100, y=50)

        # Convert button for converter
        self.convert_button = Button(self, text="Convert", command=self.perform)
        self.convert_button.place(x=120, y=195)

        # Exit button
        button_exit = Button(self, text="X", command="exit")
        button_exit.place(x=280, y=0)

    def perform(self):
        amount = float(self.amount_field.get())
        from_curr = self.from_currency_variable.get()
        to_curr = self.to_currency_variable.get()

        converted_amount = self.currency_converter.convert(from_curr, to_curr, amount)
        converted_amount = round(converted_amount, 2)

        self.converted_amount_field_label.config(text=str(converted_amount))


if __name__ == '__main__':
    url = 'https://api.exchangerate-api.com/v4/latest/USD'
    converter = my_currency_converter(url)
    App(converter)

# convert button
# exit button
button_exit = Button(root, text="X", command="exit", bg="red").place(x=650, y=0, width=50, height=40)


# play again button
def play():
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)
    entry5.delete(0, END)
    entry6.delete(0, END)
    (0, END)


play_ag_btn = Button(root, text="clear", command=play, bg="yellow", bd=5).place(x=145, y=230)

# Play button
play_btn1 = Button(root, text="Check Results", command=prizemoney, bg="yellow", bd=5).place(x=500, y=230)

root.mainloop()