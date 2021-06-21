from tkinter import *
from tkinter import messagebox
import smtplib

root = Tk()
root.title("Banking Details")
root.config(bg="yellow")
root.geometry("400x400")


def send_message():
    address_info = address.get()

    email_body_info = email_body.get()

    print(address_info, email_body_info)

    sender_email = "jchno116012003@gmail.com"

    sender_password = "googleaccount"

    server = smtplib.SMTP('smtp.gmail.com', 587)

    server.starttls()

    server.login(sender_email, sender_password)

    print("Login successful")

    server.sendmail(sender_email, address_info, email_body_info)

    print("Message sent")


address_field = Label(root, text="Recipient Address :", bg="yellow").place(x=30, y=240)
email_body_field = Label(root, text="Message :", bg="yellow").place(x=30, y=210)
address = StringVar()
email_body = StringVar()
address_entry = Entry(root, textvariable=address, bg="yellow").place(x=200, y=240)
email_body_entry = Entry(root, textvariable=email_body, bg="yellow").place(x=200, y=210)
head_lbl = Label(root, text="Banking Details", font=(80), bg="yellow").place(x=130, y=50)
aac_nm_lbl = Label(root, text="Account Holder's Name: ", bg="yellow").place(x=30, y=150)
aac_nm_en = Entry(root, text="", bg="yellow").place(x=200, y=150)
aac_no_lbl = Label(root, text="Banking Number: ", bg="yellow").place(x=30, y=180)
aac_no_en = Entry(root, text="", bg="yellow").place(x=200, y=180)
bank_lbl = Label(root, text="Bank: ", bg="yellow").place(x=30, y=270)
con_btn = Button(root, text="Confirm", command=send_message).place(x=130, y=300)

options = ["Select..", "Capitec", "Nedbank", "FNB", "ABSA"]
variable = StringVar(root)
variable.set(options[0])
gender_menu = OptionMenu(root, variable, *options).place(x=200, y=270, height="30")

root.mainloop()