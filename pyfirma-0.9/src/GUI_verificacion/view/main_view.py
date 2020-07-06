from tkinter import *
import controler
class main_view():
    x_size=500
    y_size=250
    def start(self,gui):
        self.root = gui.root
        self.gui = gui
        self.create_elements()
        self.render()
    def create_elements(self):
        self.main_frame = Frame(self.root,width=self.x_size,height=self.y_size)
        self.texto = Label(self.main_frame,text="Aplicacion para la verificacion de identidad en el certificado electronico.")
        self.texto2 = Label(self.main_frame,text="Escane el documento y pulse continuar")
        self.boton_solicitar = Button(self.main_frame,text="Continuar")
        self.boton_solicitar.bind('<ButtonRelease-1>',lambda event: controler.verificacion.cargar_documento(event,self.gui))
    def render(self):
        self.texto.grid()
        self.texto2.grid()
        self.boton_solicitar.grid()
        self.main_frame.grid()
