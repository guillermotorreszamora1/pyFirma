from tkinter import *
import controler
import view
class solicitar_cert(view.GenericView.GenericView):
    x_size=450
    y_size=250
    def create_elements(self):
        self.main_frame = Frame(self.root,width=self.x_size,height=self.y_size)
        self.texto = Label(self.main_frame,
            text="Solicitud de certificado digital.Más información en : cert.hopto.org")
        self.nombre_label = Label(self.main_frame,text="Nombre")
        self.nombre_entry = Entry(self.main_frame,width=50)
        self.nif_label = Label(self.main_frame,text="NIF")
        self.nif_entry = Entry(self.main_frame,width=15)
        self.contrasena_label = Label(self.main_frame,text="Contraseña")
        self.contrasena_entry = Entry(self.main_frame,width=15,show="*")
        self.repetir_contrasena_label = Label(self.main_frame,text="Repetir contraseña")
        self.repetir_contrasena_entry = Entry(self.main_frame,width=15,show="*")
        self.boton_solicitar = Button(self.main_frame,text="Solicitar certificado")
        self.boton_solicitar.bind('<ButtonRelease-1>',lambda event: controler.cert.solicitar(event,self.gui))
        pass
    def render(self):
        self.texto.grid()
        self.nombre_label.grid()
        self.nombre_entry.grid()
        self.nif_label.grid()
        self.nif_entry.grid()
        self.contrasena_label.grid()
        self.contrasena_entry.grid()
        self.repetir_contrasena_label.grid()
        self.repetir_contrasena_entry.grid()
        self.boton_solicitar.grid()
        self.main_frame.grid()
