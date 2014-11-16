#_*_ coding: utf-8
# mael.cadorel@laposte.net

""" Random snippets for practice. """

import grid
import gridViewer
from tkinter import *

class GUI(Tk):
    """ Generic GUI featuring a menustrip. """
    
    def __init__(self):
        Tk.__init__(self)
        self.title('GUI')
        self.menuStrip = Menu(self)
        self.menuStrip.add_command(label="Hello", command=self.placeholder)
        self.menuStrip.add_command(label="Quit", command=self.close)
        self.config(menu=self.menuStrip)

        # BINDINGS
        self.bindings = {
            '<Up>'  :lambda event:print('Up!'),
            '<Down>':lambda event:print('Down!'),
            '<Left>'  :lambda event:print('Left!'),
            '<Right>':lambda event:print('Right!')
            }
        
        # Bind keys
        for (key, action) in self.bindings.items():
            self.bind(key, action) # TODO (not working)

    def placeholder(self):
        print('Blargh!')

    def close(self):
        """ Needs serious rewriting... Perhaps consider using GUI with context
        manager, with proper __enter__ and __exit__ methods. """
        exit()


if __name__=='__main__':
    g = GUI()
    G = grid.Grid(5, 5)
    GV = gridViewer.GridViewer(G, g, 600, 600, 'black')
    GV.build()
    GV.pack()
