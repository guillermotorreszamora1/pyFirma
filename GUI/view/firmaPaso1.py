from tkinter import *
import view
import controler
class firmaPaso1(view.GenericView.GenericView):
    x_size=1000
    def create_elements(self):
        self.main_frame = Frame(self.root,width=self.x_size,height=self.y_size)
        self.texto = Label(self.main_frame,text="Paso 1: Seleccionar Fichero")
        self.boton = Button(self.main_frame,text="Seleccionar")
        self.boton.bind('<ButtonRelease-1>',lambda event: controler.firma.obtener_fichero(event,self.gui))
        self.texto2 = Label(self.main_frame,text="")
        self.boton2 = Button(self.main_frame,text="Siguiente")
        self.boton2.bind('<ButtonRelease-1>',lambda event: controler.firma.cargarPaso2(event,self.gui))
    def render(self):
        self.texto.grid()
        self.boton.grid()
        self.texto2.grid()
        self.boton2.grid()
        self.main_frame.grid()
