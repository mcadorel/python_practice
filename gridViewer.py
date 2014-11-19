#-*- coding: utf-8
# mael.cadorel@laposte.net

""" Random snippets for practice."""

from tkinter import *
from PIL import ImageTk, Image

import grid

PATH_TO_IMG = r'./tilespoof.gif'


class GridViewer(Frame, Canvas):
    """ Graphical window for viewing a Grid object. """

    def __init__(self, _grid, _root, _width, _height, _bg):
        self.WIDTH = _width
        self.HEIGHT = _height
        self._grid = _grid
        
        Frame.__init__(self,
            _root,
            width=_width,
            height=_height,
            bg=_bg)
        Canvas.__init__(self,
	    _root,
	    width=_width,
	    height=_height,
	    bg=_bg)
        
        try:
            self.img = ImageTk.PhotoImage(Image.open(PATH_TO_IMG))
        except FileNotFoundError:
            print('Warning : Image file not found.')

        # Determine the proportions of displayed tiles
        self.tile_height = self.HEIGHT/self._grid.m 
        self.tile_width  = self.WIDTH/self._grid.n

    def build(self):
        """ Attempts to bring forth a graphical rendition of the grid. """
        for _row in self._grid.keys():
            for _cell in self._grid[_row]:
                # Placeholder for actual rendition of tiles.
                self.create_oval(
                    _row * self.tile_height,
                    _cell * self.tile_width,
                    _row * self.tile_height + (self.tile_height),
                    _cell * self.tile_width + (self.tile_width),
                    fill='white')

    def highlight(self, x:'row', y:'column'):
        """ Temporary, just for debugging. """
        tile_coords = (
            x * self.tile_width + (self.tile_width / 2),
            y * self.tile_height + (self.tile_height / 2)
            )
        self.find_closest(*tile_coords).configure(fill='red') # TODO : find_closest returns a tuple
        


# Test :
if __name__ == '__main__':
    G = grid.Grid(5, 5)
    GV = GridViewer(G, Tk(), 300, 300, 'black')
    GV.build()
    GV.pack()
    GV.mainloop()
