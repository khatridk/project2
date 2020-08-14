import tkinter
import cv2
import PIL.Image,PIL.ImageTk
from functools import partial 
import threading
import time
import imutils
from tkinter import ttk
import os



#*********************functions***************************************

    
def play(sp):
    stream=cv2.VideoCapture('videos/'+video.get())
    fr1=stream.get(cv2.CAP_PROP_POS_FRAMES)
    stream.set(cv2.CAP_PROP_POS_FRAMES,fr1+sp)
    gr,frame=stream.read()
    frame=imutils.resize(frame,width=wid,height=he)
    frame=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image=frame
    canvas.create_image(0,0,ancho=tkinter.NW, image=frame)
    print(video.get())


def decision(arg):
    frame=cv2.cvtColor(cv2.imread("images/d_p.jpg"),cv2.COLOR_BGR2RGB)
    frame=imutils.resize(frame,width=wid,height=he)
    frame=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image=frame
    canvas.create_image(0,0,ancho=tkinter.NW, image=frame)
    time.sleep(2)


    if arg=="out":
        frame=cv2.cvtColor(cv2.imread("images/out.jpg"),cv2.COLOR_BGR2RGB)
        frame=imutils.resize(frame,width=wid,height=he)
        frame=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
        canvas.image=frame
        canvas.create_image(0,0,ancho=tkinter.NW, image=frame)
    
        
    else:
        frame=cv2.cvtColor(cv2.imread("images/notout.jpg"),cv2.COLOR_BGR2RGB)
        frame=imutils.resize(frame,width=wid,height=he)
        frame=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
        canvas.image=frame
        canvas.create_image(0,0,ancho=tkinter.NW, image=frame)
   
    
def out():
    th=threading.Thread(target=decision,args=('out',))
    th.daemon=1
    th.start()


def notout():
    th=threading.Thread(target=decision,args=('notout',))
    th.daemon=1
    th.start()





#*****************************designing screen of software***************************************

wid=701
he=438
window=tkinter.Tk()
video=tkinter.StringVar()
videolist=os.listdir('videos/')
vi=''
window.title("DRS SYSTEM")
cv_img=cv2.cvtColor(cv2.imread("images/main.jpg"),cv2.COLOR_BGR2RGB)
canvas=tkinter.Canvas(window,width=wid,height=he)
photo=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
canvas.create_image(0,0,ancho=tkinter.NW, image=photo)
canvas.pack()

#*******************buttons*************************************
l=tkinter.Label(window,text='select video here')
l.pack()
select=ttk.Combobox(window,textvariable=video,value=videolist,width=42)
select.pack()
br=tkinter.Button(window,text="<<PREVIOUS FAST",bd=4,width=50,command=partial(play,-15))
br.pack()
br=tkinter.Button(window,text="<<PREVIOUS SLOW",bd=4,width=50,command=partial(play,-2))
br.pack()
br=tkinter.Button(window,text="NEXT FAST >>",bd=4,width=50,command=partial(play,15))
br.pack()
br=tkinter.Button(window,text="NEXT SLOW >>",bd=4,width=50,command=partial(play,1))
br.pack()
br=tkinter.Button(window,text="GIVE OUT",bd=4,width=50,command=out)
br.pack()
br=tkinter.Button(window,text="GIVE NOT OUT",bd=4,width=50,command=notout)
br.pack()

window.mainloop()