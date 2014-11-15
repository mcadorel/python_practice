#_*_ coding: utf-8
# mael.cadorel@laposte.net

""" Random snippets for practice. """


from tkinter import Tk, Menu

class GUI(Tk):
    """ Generic GUI featuring a menustrip. """
    
    def __init__(self):
        Tk.__init__(self)
        self.title('GUI')
        self.menuStrip = Menu(self)
        self.menuStrip.add_command(label="Hello", command=self.placeholder)
        self.menuStrip.add_command(label="Quit", command=self.close)
        self.config(menu=self.menuStrip)

    def placeholder(self):
        print('Blargh!')

    def close(self):
        """ Needs serious rewriting... Perhaps consider using GUI with context
        manager, with proper __enter__ and __exit__ methods. """
        exit()


if __name__=='__main__':
    g = GUI()
