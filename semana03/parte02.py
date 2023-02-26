from tkinter import Tk,Button,Label,filedialog
import cv2
from PIL import Image, ImageTk
import imutils
cap=None
def chooseVideo():
    global cap
    pathVideo=filedialog.askopenfilename(filetypes=[
        ("all video format",".mp4")
    ])
    if len(pathVideo)>0:
        videoPathL['text']='Ruta del video: {}'.format(pathVideo)
        cap=cv2.VideoCapture(pathVideo)
        showVideo()

def showVideo():
    global cap
    ret, frame=cap.read()
    if ret==True:
        frame=imutils.resize(frame, width=1040)
        frame=cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        i=Image.fromarray(frame)
        img=ImageTk.PhotoImage(image=i)

        videoL.configure(image=img)
        videoL.image=img
        videoL.after(10,showVideo)


window=Tk()
window.title='Detector de rostros'
window.state('zoomed')
window.configure(bg='#3e78dd')

#Boton para elegir video
seeB=Button(window, text='Elegir video',font=('monospace',14),command=chooseVideo)
seeB.grid(row=0, column=0,padx=10,pady=10)

#Label para mostrar ruta
videoPathL=Label(window,text='Ruta del video: No hay algun video')
videoPathL.grid(row=1,column=0)
videoPathL.configure(bg='green',font=('monospace',14))

#Label para el video
videoL=Label(window)
videoL.grid(row=3, column=0)
window.mainloop()

