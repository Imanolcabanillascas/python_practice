from tkinter import Tk, Button, Label, filedialog
import cv2 # pip install opencv-contrib-python
from PIL import Image, ImageTk #pip install Pillow
import imutils
import mediapipe as mp


cap=None
mp_face_mesh=mp.solutions.face_mesh
mp_drawing=mp.solutions.drawing_utils


def chooseVideo():
    global cap
    pathVideo=filedialog.askopenfilename(filetypes=[
        ("all video format", ".mp4")
    ])
    if len(pathVideo)>0:
        videoPathL['text']='Ruta del video: {}'.format(pathVideo)
        cap=cv2.VideoCapture(pathVideo)
        showVideo()


def streamingVideo():
    global cap
    cap=cv2.VideoCapture(0)
    showVideo()


def showVideo():
    global cap
    ret, frame=cap.read()
    if ret == True:
        frame=imutils.resize(frame, width=1040)
        frame=cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)


        ##############################################
        with mp_face_mesh.FaceMesh(
            static_image_mode=False,
            max_num_faces=5,
            min_detection_confidence=0.5
        ) as face_mesh:


            result=face_mesh.process(frame)
            detection=result.multi_face_landmarks


            cont=0
            if detection is not None:
                for face_landmarks in detection:
                    # mp_drawing.draw_landmarks(frame, face_landmarks, mp_face_mesh.FACEMESH_TESSELATION)
                    mp_drawing.draw_landmarks(frame, face_landmarks, mp_face_mesh.FACEMESH_CONTOURS)
                    cont=cont+1
                faceContL['text']='N° de rostros: {}'.format(cont)
        ##############################################




        i=Image.fromarray(frame)
        img=ImageTk.PhotoImage(image=i)
        videoL.configure(image=img)  
        videoL.image=img
        videoL.after(10, showVideo)


window=Tk()
window.title('Detector de rostros')
window.state('zoomed')
window.configure(bg='#3e78dd')


# Buton para elegir video
seeB=Button(window, text='Elegir video', font=('Times', 24), command=chooseVideo)
seeB.grid(row=0, column=0, padx=10, pady=10)


# Buton para elegir video
seeStreamingB=Button(window, text='Usar cámara', font=('Times', 24), command=streamingVideo)
seeStreamingB.grid(row=0, column=1, padx=100, pady=10)


#Label para mostrar ruta
videoPathL=Label(window, text='Ruta del video: No hay algún video aún')
videoPathL.grid(row=1, column=0)
videoPathL.configure(bg='#3e78dd', font=('Times', 24))


# Label para el video
videoL=Label(window)
videoL.grid(row=3, column=0, padx=10)


#Contrador de rostros
faceContL=Label(window, text='N° de rostros: ', font=('Times', 24))
faceContL.grid(row=3, column=1, padx=10)


window.mainloop()