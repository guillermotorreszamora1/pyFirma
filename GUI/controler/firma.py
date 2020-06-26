from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
from tkinter import messagebox
import model
import view
import traceback
def obtener_fichero(event,gui):
    filename = askopenfilename(title="Fichero a firmar",initialdir="~/Escritorio")
    gui.view.texto2['text'] = filename
def cargarPaso2(event,gui):
    filename = gui.view.texto2['text']
    if filename == '':
        messagebox.showerror("Error","Seleccione un fichero")
        return
    user_list = []
    nif_list = model.cert_storage.list_accepted_cert()
    for nif in nif_list:
        u = model.cert_storage.User.load(nif)
        user_list.append(u)
    gui.resize_and_set(view.firmaPaso2.firmaPaso2(user_list,filename))
def cargarPaso3(event,gui):
    filename = gui.view.filename
    id = gui.view.listbox.curselection()
    if id == ():
        messagebox.showerror("Error","Seleccione un certificado")
        return
    user = gui.view.user_list[id[0]]
    gui.resize_and_set(view.firmaPaso3.firmaPaso3(user,filename))
def firmar(event,gui):
    filename = gui.view.filename
    user = gui.view.user
    print("FIRMADOS")
    print(filename)
    print(user)
    password = gui.view.contrasena_entry.get()
    print(password)
    try:
        signed_doc = model.crypto.sign_doc(filename,user,password)
    except ValueError:
        messagebox.showerror("Error","Contraseña incorrecta")
        return
    except Exception :
        traceback.print_exc()
        messagebox.showerror("Error","Error desconocido")
        return
    messagebox.showinfo("Firma realizada","Firma realizada correctamente. Ahora debera elegir para el archivo firmado")
    filename = asksaveasfilename(title="Guardar documento firmado",
        defaultextension=".pdf",initialdir="~/Escritorio")
    file = open(filename,'wb')
    file.write(signed_doc)
def verificar(event,gui):
    filename = askopenfilename(title="Fichero a verificar",initialdir="~/Escritorio")
    file = open(filename,'rb').read()
    try:
        firma,_ = model.crypto.check_signature(file)
        messagebox.showinfo("Firma Verificada","Fichero firmado por:\n"+firma)
    except:
        messagebox.showerror("Error al verificar","La firma no ha podido ser verificada")
