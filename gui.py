#_*_ coding: utf-8
# mael.cadorel@laposte.net

""" Random snippets for practice. """

from collections import OrderedDict
import grid
import gridViewer
from tkinter import *

class GUI(Tk):
    """ Generic GUI featuring a menustrip, fullscreen mode, ... """
    
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
        
        for (key, action) in self.bindings.items():
            self.bind(key, action)

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.close()

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
            del self.sizeBuffer
            self.fullscreen = False

    def placeholder(self):
        print('Blargh!')

    def close(self):
        """ Close application (not just root window.) """
        self.destroy()
        print('Quitting...')
        exit(0)

# Test 
if __name__=='__main__':
    with GUI() as someGui:
        someGrid = grid.Grid(5, 5)
        someGridViewer = gridViewer.GridViewer(
            someGrid,
            someGui,
            600, 600,
            'black')
        someGridViewer.build()
        someGridViewer.grid(row=0, column=0, sticky=NW)
        someGui.mainloop()
