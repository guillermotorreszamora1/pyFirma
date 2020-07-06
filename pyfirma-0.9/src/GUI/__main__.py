from view.UserInterface import *
import model
def main():
    gui = UserInterface()
    model.prepare()
    gui.start()
main()
