from playsound import playsound
from tkinter import *
import multiprocessing

window = Tk()
m = multiprocessing.Process(target=playsound, args=("2pac_hit_em_up_lyrics_mp3_25544.mp3"))


def play_sound():
    m.start()


def stop_music():
    m.terminate()
    window.destroy()


Button(window, text="Stop", command=stop_music()).pack()
Button(window, text="Play", command=play_sound()).pack()

window.mainloop()
