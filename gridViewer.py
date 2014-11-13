from tkinter import *
from PIL import ImageTk, Image

import grid


class GridViewer(Tk):
    def __init__(self, _grid):
        Tk.__init__(self)
        self.title('GridViewer')
        self._grid=_grid
        self.PATH = r'C:\Users\Maël\Desktop\Informatique\Grid\tilespoof.gif'
        self.img = ImageTk.PhotoImage(Image.open(self.PATH))


    def build(self):
        for _row in self._grid.keys():
            for _cell in self._grid[_row]:
                #Label(self, text=str(self._grid[_row][_cell]), image=self.img).grid(row=_row, column=_cell)
                Button(self,
                       text=str(self._grid[_row][_cell]),
                       image=self.img,
                       command=lambda event:print(event)).grid(
                           row=_row, column=_cell)
        

if __name__ == '__main__':
    G = grid.Grid(5, 5)
    GV = GridViewer(G)
    GV.build()
    GV.mainloop()

