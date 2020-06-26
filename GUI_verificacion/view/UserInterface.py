from tkinter import *
from view.main_view import *
class UserInterface():
    root = None
    view = None
    def start(self):
        self.root = Tk()
        self.root.title('PyFirma')
        self.view = main_view()
        self.root.geometry('{}x{}'.format(self.view.x_size,self.view.y_size))#1300,700
        self.view.start(self)
        self.root.mainloop()
    def set(self,view):
        self.root.winfo_children()[0].destroy()
        self.view = view
        self.view.start(self)
    def resize_and_set(self,view,x,y):
        self.root.geometry('{}x{}'.format(x,y))
        self.set(view)
    def resize_and_set(self,view):
        self.root.geometry('{}x{}'.format(view.x_size,view.y_size))
        self.set(view)
