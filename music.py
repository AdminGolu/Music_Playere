from tkinter import *
from tkinter import Tk
from tkinter import  filedialog
from pygame import mixer
import os


#Creating Root Window:
root=Tk()
root.title("name of the player is:")
root.geometry("920x670+290+85")
root.configure(background="#333333")
root.resizable(False,False)
mixer.init()


#Creating Music Player Functions:
def Add_Music():
    path = filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs = os.listdir(path)

        for song in songs:
            if song.endswith((".mp3")):
                playlist.insert(END,song)


def Play_Music():
    Music_Nmae=Playlist.get(ACTIVE)
    print(Music_Nmae[0:-4])
    mixer.music.load(Playlist.get(ACTIVE))
    mixer.music.play()


#Creating Icon and Logo
#Icon
Icon_Image = PhotoImage(file="logo2.png")
root.iconphoto(False, Icon_Image=PhotoImage(file="logo2.png"))



Top_Image = PhotoImage(file="top.png")
Label(root,image=Top_Image, background="#0f1a2b").pack()


#Logo
logo_image = PhotoImage(file="logo2.png")
Label(root,image=logo_image, background="#0f1a2b").place(x=65, y=115)