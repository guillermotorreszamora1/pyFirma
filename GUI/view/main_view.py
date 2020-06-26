from tkinter import *
from view.solicitar_cert import *
import view
import controler
import view
class main_view(view.GenericView.GenericView):
    y_size=250
    def create_elements(self):
        self.main_frame = Frame(self.root,width=self.x_size,height=self.y_size)
        self.boton_solicitar = Button(self.main_frame,text="Solicitar certificado")
        self.boton_descargar = Button(self.main_frame,text="Descargar certificado")
        self.boton_firmar = Button(self.main_frame,text="Firmar documento")
        self.boton_verificar = Button(self.main_frame,text="Verificar documento")
        self.boton_solicitar.bind('<Button 1>', lambda event: self.gui.resize_and_set(solicitar_cert()))
        self.boton_descargar.bind('<Button 1>', lambda event: controler.list_cert_loader.list_cert_loader(event,self.gui))
        self.boton_firmar.bind('<Button 1>',lambda event: self.gui.resize_and_set(view.firmaPaso1.firmaPaso1()))
        self.boton_verificar.bind('<ButtonRelease-1>',lambda event: controler.firma.verificar(event,self.gui))
    def render(self):
        self.boton_solicitar.place(x=50,y=50)
        self.boton_descargar.place(x=50,y=100)
        self.boton_firmar.place(x=50,y=150)
        self.boton_verificar.place(x=50,y=200)
        self.main_frame.grid()
