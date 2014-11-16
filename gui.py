#_*_ coding: utf-8
# mael.cadorel@laposte.net

""" Random snippets for practice. """

from collections import OrderedDict
import grid
import gridViewer
from tkinter import *

class GUI(Tk):
    """ Generic GUI featuring a menustrip. """
    
    def __init__(self):
        Tk.__init__(self)
        self.title('GUI')
        self.fullscreen = False

        # MENU
        self.menu_options = OrderedDict([
            ('Placeholder'  , self.placeholder),
            ('Quit'         , self.close)
            ])


        self.menuStrip = Menu(self)
        for (_label, action) in self.menu_options.items():
            self.menuStrip.add_command(label=_label, command=action)
        self.config(menu=self.menuStrip)

        # BINDINGS
        self.bindings = OrderedDict([
            ('<Up>'      , lambda event: print('Up!')),
            ('<Down>'    , lambda event: print('Down!')),
            ('<Left>'    , lambda event: print('Left!')),
            ('<Right>'   , lambda event: print('Right!')),
            ('<F11>'     , self.toggle_fullscreen)
            ])
        
        # Bind keys
        for (key, action) in self.bindings.items():
            self.bind(key, action)

    def toggle_fullscreen(self, event):
        """ Same func for turning it on and off. """
        if not self.fullscreen:
            self.sizeBuffer = (self.winfo_height(), self.winfo_width())
            self.geometry(
                "{0}x{1}+0+0".format(
                    self.winfo_screenwidth(),
                    self.winfo_screenheight()
                    )
                )
            self.overrideredirect(1)
            self.focus_set()
            self.fullscreen = True
        else:
            self.overrideredirect(0)
            self.geometry(
                "{0}x{1}+0+0".format(
                    *self.sizeBuffer
                    )
                )
            self.fullscreen = False

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
