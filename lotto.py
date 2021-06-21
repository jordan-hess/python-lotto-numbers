from playsound import playsound
from tkinter import *
from tkinter import messagebox
import random


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
        if len() > 49 or len() < 1:
            messagebox.showerror(message="All numbers should be in the range of 49")
        else:
            return ent_list

    except ValueError:
        messagebox.showinfo(message="Fill in all entries with numbers")


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
    lost = {1: "R0"}
    noth = {0: "0"}
    myloss = len(result)
    mykey = len(result)
    nothing = len(result)
    xy = {lost.get(myloss)}
    x = {prize_mny.get(mykey)}
    xyz = {noth.get(nothing)}
    if result == xy:
        playsound('sad_trombone_gaming_sound_effect_hd_mp3_32171.mp3')
        messagebox.showinfo(message="You got 1 match dont give up")
    elif result == xyz:
        playsound('sad_trombone_gaming_sound_effect_hd_mp3_32171.mp3')
        messagebox.showinfo(message="unlucky draw")

    else:
        playsound('ka-ching_sound_effect_mp3_32039.mp3')
        messagebox.showinfo("you've won", x)




x = StringVar
myresult = StringVar()
my_lotto_num = Label(root, text=" ", textvariable=myresult, bg="yellow", font="70").place(x=240, y=340)
loto_num_lbl = Label(root, text="Lotto Numbers: ", bg="yellow", font="70").place(x=90,y=340)

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

def claim():
    playsound("windows_10_system_generic_notification_sound_mp3_44661.mp3")
    root.destroy()
    import banking_details

def openconvert():
    playsound("windows_10_system_generic_notification_sound_mp3_44661.mp3")
    root.destroy()
    import converter


play_ag_btn = Button(root, text="clear", command=play, bg="yellow", bd=5).place(x=145, y=230)

# Play button
play_btn1 = Button(root, text="Check Results", command=prizemoney, bg="yellow", bd=5).place(x=500, y=230)
claim_btn = Button(root, text="Claim winnings", command=claim, bg="yellow").place(x=300, y=600)
convert_btn = Button(root, text="convert winnings",command=openconvert, bg="yellow").place(x=440, y=600)

root.mainloop()