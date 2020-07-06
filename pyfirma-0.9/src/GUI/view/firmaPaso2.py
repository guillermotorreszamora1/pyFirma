from tkinter import *
import view
import controler
class firmaPaso2(view.GenericView.GenericView):
    x_size=400
    y_size=300
    def __init__(self,user_list,filename):
        self.user_list = user_list
        self.filename = filename
    def create_elements(self):
        self.main_frame = Frame(self.root,width=self.x_size,height=self.y_size)
        self.texto = Label(self.main_frame,text="Paso 2: Seleciona una certificado y pulsa continuar")
        self.scroll_frame = Frame(self.main_frame)
        self.listbox = Listbox(self.scroll_frame,height=10,width=30)
        self.scrollbar = Scrollbar(self.scroll_frame,orient="vertical")
        self.scrollbar.config(command=self.listbox.yview)
        self.listbox.config(yscrollcommand=self.scrollbar.set)
        for i in range(0,len(self.user_list)):
            self.listbox.insert(END,str(self.user_list[i]))
        self.button = Button(self.main_frame,text="Siguiente")
        self.button.bind('<ButtonRelease-1>',lambda event: controler.firma.cargarPaso3(event,self.gui))
    def render(self):
        self.texto.place(x=10,y=10)
        self.listbox.pack(side="left",fill="y")
        self.scrollbar.pack(side="right",fill="y")
        self.scroll_frame.place(x=10,y=50)
        self.button.place(x=10,y=250)
        self.main_frame.grid()
