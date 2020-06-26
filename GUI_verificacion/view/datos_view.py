from tkinter import *
import controler
class datos_view():
    nombre = None
    nif = None
    number = None
    x_size=500
    y_size=250
    def __init__(self,nombre,nif,number):
        self.nombre = nombre
        self.nif = nif
        self.number = number
    def start(self,gui):
        self.root = gui.root
        self.gui = gui
        self.create_elements()
        self.render()
    def create_elements(self):
        self.main_frame = Frame(self.root,width=self.x_size,height=self.y_size)
        self.texto = Label(self.main_frame,text="Datos del usuario a verificar")
        self.texto2 = Label(self.main_frame,text="Nombre: "+self.nombre)
        self.texto3 = Label(self.main_frame,text="NIF: "+self.nif)
        self.texto4 = Label(self.main_frame,text="Escriba aceptar o denegar y pulse confirmar")
        self.texto_entry = Entry(self.main_frame,width=10)
        self.boton = Button(self.main_frame,text="Confirmar")
        self.boton.bind('<ButtonRelease-1>',lambda event: controler.verificacion.aceptar(event,self.gui))
    def render(self):
        self.texto.grid()
        self.texto2.grid()
        self.texto3.grid()
        self.texto4.grid()
        self.texto_entry.grid()
        self.boton.grid()
        self.main_frame.grid()
