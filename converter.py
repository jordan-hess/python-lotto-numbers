from tkinter import *
import requests
import tkinter as tk
from tkinter import ttk
from playsound import playsound

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

        self.from_currency_lbl = Label(self, text="ZAR", bg="yellow")
        self.to_currency_dropdown = ttk.Combobox(self, textvariable=self.to_currency_variable,
                                                 values=list(self.currency_converter.currencies.keys()))

        # placing
        self.from_currency_lbl.place(x=50, y=100)
        self.amount_field.place(x=90, y=100)
        self.to_currency_dropdown.place(x=30, y=130, width="50")
        self.converted_amount_field_label.place(x=90, y=130, width="125")
        self.intro_label.place(x=100, y=50)

        # Convert button for converter
        self.convert_button = Button(self, text="Convert", command=self.perform, bg="yellow")
        self.convert_button.place(x=60, y=195)

        def claim():
            App.destroy(self)
            playsound("windows_10_system_generic_notification_sound_mp3_44661.mp3")
            import banking_details

        # claim Button
        self.claim_btn = Button(text="Claim winnings", command=claim, bg="yellow")
        self.claim_btn.place(x=150, y=195)

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





url = 'https://api.exchangerate-api.com/v4/latest/USD'
converter = my_currency_converter(url)
App(converter)
mainloop()