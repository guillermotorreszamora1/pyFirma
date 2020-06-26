from tkinter import messagebox
from tkinter.filedialog import asksaveasfilename
import tkinter
import model
import view
def solicitar(event,gui):
    nombre = gui.view.nombre_entry.get()
    nif = gui.view.nif_entry.get()
    contrasena = gui.view.contrasena_entry.get()
    repetir_contrasena = gui.view.repetir_contrasena_entry.get()
    if not model.nif.verificar(nif):
        messagebox.showerror("Error","NIF invalido")
        return
    if contrasena!=repetir_contrasena:
        messagebox.showerror("Error","Las contraseñas no coinciden")
        return
    public_pem = model.key.generate_key(contrasena,nif)
    result = model.network.solicitud(nombre,nif,public_pem)
    model.cert_storage.User(nombre,nif,result).save()
    if result==-1:
        messagebox.showerror("Error","No se ha podido realizar la solicitud correctamente")
    else:
        messagebox.showinfo("Solicitud Realizada","Solicitud Realizada correctamente.Imprima el documento y"
        "dirigase a una oficina de registro")
    filename = asksaveasfilename(title="Guardar documento de solicitud",
        defaultextension=".pdf",initialdir="~/Escritorio",initialfile="solicitud")
    model.pdf.save_pdf(filename,result)
    gui.resize_and_set(view.main_view.main_view())
def descargar(event,gui):
    id = gui.view.listbox.curselection()
    if id == ():
        print("Vacio")
    else:
        model.network.descarga(gui.view.user_list[id[0]])
#En los protocolos de comunicación se codifican atributos como nombre y contraseña en BASE64.
