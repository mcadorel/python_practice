#-*- coding: utf-8
# mael.cadorel@laposte.net


""" Random snippets for practice. """

from data import Data
from grid import Grid, Screen
from gridViewer import GridViewer
from gui import GUI
        

class App(object):
    """ Main executable. Composed of
    - Data
    - GUI."""
    
    def __init__(self):
        self.data = Data()
        self.gui = GUI()

        self.data['grid']           = Grid(15, 15, fill='.') # "Let's pretend" this is a world map or whatever

# Test
if __name__ == '__main__':
    someApp = App()
    gv = GridViewer(
        Screen(someApp.data['grid']),
        someApp.gui,
        200,
        200,
        'black')
    gv.build()
    gv.grid(row=0, column=0)
    
