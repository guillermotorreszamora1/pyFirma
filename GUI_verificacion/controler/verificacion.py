from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from pyzbar.pyzbar import decode
from PIL import Image
from pdf2image import convert_from_path
from view import datos_view
from view import main_view
import model
def cargar_documento(event,gui):
    file = askopenfilename(initialdir="~/Escritorio")
    number = int(decode(convert_from_path(file)[0])[0][0])
    nombre = model.database.get_nombre(number)
    nif = model.database.get_nif(number)
    view = datos_view.datos_view(nombre,nif,number)
    gui.resize_and_set(view)
def aceptar(event,gui):
    texto = gui.view.texto_entry.get()
    if texto=='aceptar':
            clave = model.database.get_clave_publica(gui.view.number)
            cert = model.crypto.certificate(clave,"Nombre:"+gui.view.nombre+"\nNIF:"+gui.view.nif,gui.view.number)
            model.database.anadir_certificado(gui.view.nombre,gui.view.nif,gui.view.number,cert)
            model.database.aceptar_solicitud(gui.view.number)
    if texto=='aceptar' or texto=='denegar':
        messagebox.showinfo(texto,"Solicitud procesada correctamente")
        view = main_view.main_view()
        gui.resize_and_set(view)
    else:
        messagebox.showerror("texto incorrecto","texto incorrecto")
