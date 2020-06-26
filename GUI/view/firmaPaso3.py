from tkinter import *
import view
import controler
class firmaPaso3(view.GenericView.GenericView):
    x_size=1000
    def __init__(self,user,filename):
        self.user = user
        self.filename = filename
    def create_elements(self):
        self.main_frame = Frame(self.root,width=self.x_size,height=self.y_size)
        self.texto = Label(self.main_frame,text="Paso 3: Introducir contraseña y firmar")
        self.texto2 = Label(self.main_frame,text=str(self.filename))
        self.texto3 = Label(self.main_frame,text=str(self.user))
        self.texto4 = Label(self.main_frame,text="Introduzca la contraseña")
        self.contrasena_entry = Entry(self.main_frame,show="*")
        self.boton = Button(self.main_frame,text="Firmar")
        self.boton.bind('<ButtonRelease-1>',lambda event: controler.firma.firmar(event,self.gui))
    def render(self):
        print("H")
        self.texto.grid()
        self.texto2.grid()
        self.texto3.grid()
        self.texto4.grid()
        self.contrasena_entry.grid()
        self.boton.grid()
        self.main_frame.grid()
