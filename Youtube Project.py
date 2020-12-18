#!pip install pytube
import pytube
from pytube import YouTube
from tkinter import *

root = Tk()
root.geometry("300x400")
root.title("YouTube Video Downloader")
def youtube():
   
    a = var.get()#https://youtu.be/9emx__jxcTE
    ytvideo = YouTube(a).streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
   
    ytvideo.download(r"D:\movies\Videos")
   
    print("Entry box",a)
    
l1 = Label(root, text="Paste Your Link Here :-", fg="red", font=("bold",20))
l1.place(x=30,y=20)

var = StringVar()

e1 = Entry(root,textvariable=var,width=60)
e1.place(x=40,y=80)

b1 = Button(root,text = "Download",command=youtube,bg="Purple",width=20,fg="yellow")
b1.place(x=80,y=120)

root.mainloop()