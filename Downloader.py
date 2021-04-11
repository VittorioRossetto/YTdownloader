from tkinter import *
from pytube import YouTube

import os


root = Tk()
root.geometry('500x400')
root.resizable(0,0)
root.title("youtube video downloader")
root.configure(bg = 'black')

Label(root,text = 'Youtube Video Downloader', font = 'arial 20 bold', fg = 'white', bg = 'black').pack()
link = StringVar()
folder = StringVar()

Label(root, text = 'Paste Folder Path Here:', font = 'arial 15 bold', fg = 'white', bg = 'black').place(x = 130, y = 60)
folder_enter = Entry(root, width = 70,textvariable = folder).place(x = 32, y = 90)

Label(root, text = 'Paste Link Here:', font = 'arial 15 bold', fg = 'white', bg = 'black').place(x = 160, y = 140)
folder_enter = Entry(root, width = 70,textvariable = link).place(x = 32, y = 170)

Label(root, text = 'By Vittorio Rossetto', font = 'arial 9', fg = 'white', bg = 'black').place(x = 0, y = 380)



def snd1():
   os.system('.\\pirateria.mp4')

def Downloader():
    url = YouTube(str(link.get()))
    video = url.streams.first()
    video.download(str(folder.get()))
    Label(root, text = 'DOWNLOADED', font = 'arial 15', fg = 'white', bg = 'black').place(x = 180, y = 320)

var = IntVar()
rb1 = Button(root, text = 'RICORDA', font = 'arial 11', fg = 'white', bg = 'red', command = snd1).place(x = 207, y = 270)
Button(root,text = 'DOWNLOAD', font = 'arial 15 bold' ,fg = 'white', bg = 'pale violet red', padx = 2, command = Downloader).place(x = 180, y = 220)

root.mainloop()