from tkinter import *
from tkinter import messagebox

#Funcion de mostrar una ventana
def showMessage():
    print('Click')
    messagebox.showinfo(
        title='Ventana de warning',
        message='Warning'
    )

window=Tk()
window.title('Taller de Python')
# window.geometry('400x400')
window.configure(bg='#3e78dd')

button01=Button(window,text="Aceptar",command=showMessage)
button01.place(x=20,y=20)

window.mainloop()
