from abc import ABC,abstractmethod
class GenericView(ABC):
    x_size=300
    y_size=200
    def start(self,gui):
        self.root = gui.root
        self.gui = gui
        self.create_elements()
        self.render()
    @abstractmethod
    def create_elements(self):
        pass
    @abstractmethod
    def render(self):
        pass
