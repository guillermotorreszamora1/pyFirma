from tkinter import *
import controler
import view
class list_pending_cert(view.GenericView.GenericView):
    x_size=300
    y_size=300
    def __init__(self,user_list):
        self.user_list = user_list
    def create_elements(self):
        self.main_frame = Frame(self.root,width=self.x_size,height=self.y_size)
        self.texto = Label(self.main_frame,text="Seleciona una solicitud y pulse descargar")
        self.scroll_frame = Frame(self.main_frame)
        self.listbox = Listbox(self.scroll_frame,height=10,width=30)
        self.scrollbar = Scrollbar(self.scroll_frame,orient="vertical")
        self.scrollbar.config(command=self.listbox.yview)
        self.listbox.config(yscrollcommand=self.scrollbar.set)
        for i in range(0,len(self.user_list)):
            self.listbox.insert(END,str(self.user_list[i]))
        self.button = Button(self.main_frame,text="Descargar")
        self.button.bind('<ButtonRelease-1>',lambda event: controler.cert.descargar(event,self.gui))
    def render(self):
        self.texto.place(x=10,y=10)
        self.listbox.pack(side="left",fill="y")
        self.scrollbar.pack(side="right",fill="y")
        self.scroll_frame.place(x=10,y=50)
        self.button.place(x=10,y=250)
        self.main_frame.grid()
