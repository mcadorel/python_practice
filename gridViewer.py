#-*- coding: utf-8
# mael.cadorel@laposte.net

""" Random snippets for practice."""

from tkinter import *
from PIL import ImageTk, Image

import grid

PATH_TO_IMG = r'./tilespoof.gif'


class GridViewer(Tk):
    """ Graphical window for viewing a Grid object. Needs rewriting
    as a tkinter.Frame or tkinter.Canvas subclass, so as to support
    proper key-binding etc. """

    def __init__(self, _grid):
        Tk.__init__(self)
        self.title('GridViewer')
        self._grid=_grid
        try:
            self.img = ImageTk.PhotoImage(Image.open(PATH_TO_IMG))A
        except FileNotFoundError:
            print('Warning : Image file not found.')


    def build(self):
        """ Attempts to bring forth a graphical rendition of the grid. """
        for _row in self._grid.keys():
            for _cell in self._grid[_row]:
                Button(self, # Terrible idea (except perhaps if making a minesweeper kind of game.)
                       text=str(self._grid[_row][_cell]),
                       image=self.img,
                       command=lambda event:print(event)).grid(
                           row=_row, column=_cell)
        

""" Test : """
if __name__ == '__main__':
    G = grid.Grid(5, 5)
    GV = GridViewer(G)
    GV.build()
    GV.mainloop()
