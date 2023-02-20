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
root.iconphoto(False,Icon_Image)



Top_Image = PhotoImage(file="top.png")
Label(root,image=Top_Image, background="#0f1a2b").pack()


#Logo
logo_image = PhotoImage(file="logo2.png")
Label(root,image=logo_image, background="#0f1a2b").place(x=65, y=115)


# Button
Button_Play = PhotoImage(file="play.png")
Button(root, image=Button_Play, background="#0f1a2b", bd=0, command=Play_Music).place(x=100, y=400)

Button_Stop = PhotoImage(file="stop.png")
Button(root, image=Button_Stop, background="#0f1a2b", bd=0, command=mixer.music.stop).place(x=30, y=500)

Button_Resume = PhotoImage(file="resume.png")
Button(root, image=Button_Resume, background="#0f1a2b", bd=0, command=mixer.music.unpause).place(x=115, y=500)

Button_Pause = PhotoImage(file="pause.png")
Button(root, image=Button_Pause, background="#0f1a2b", bd=0, command=mixer.music.pause).place(x=200, y=500)


#Music
Menu = PhotoImage(file="menu.png")
Label(root, image=Menu, background="#0f1a2b").pack(padx=10, pady=50, side=RIGHT)

Frame_Music = Frame(root, background=2, relief=RIDGE)
Frame_Music.place(x=330, y=560, width=560, height=250)

Button(root, text="Add Music", width=15, height=2, font=("Times New Roman", 12, "bold"), fg="Black", background="#21b3de", COMMAND=Add_Music).place(x=330, y=300)
SCROLL = Scrollbar(Frame_Music)
Playlist = Listbox(Frame_Music, width=100, font=("Times New Roman",10), background="#333333", fg="grey", selectbackground="lightblue", cursor="hand2",bd=0, yscrollcommand=SCROLL.set)
SCROLL.config(command=Playlist.yview)
SCROLL.pack(side=RIGHT, fill=Y)
Playlist.pack(side=LEFT, fill=BOTH)


root.mainloop()

