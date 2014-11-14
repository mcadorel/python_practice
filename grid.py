#-*- coding: utf-8
# mael.cadorel@laposte.net

""" Random snippets for practice."""

from random import randint

class Tile(object):
    """ A tile in a 2D-grid, for either ascii or graphical display.
    Possibly useful as a container for other objects (critters, 
    items lying on ground, etc.) """

    def __init__(self, symbol='.'):
        self.symbol = str(symbol)

    def __repr__(self):
        return self.symbol

    __str__ = __repr__


class Grid(dict):
    """ A multi-purposed 2D-grid. Because wheels are for reinventing. """
    
    def __init__(self, m:'rows', n:'columns', fill='random'):
        self.m = m # Number of rows
        self.n = n # Number of columns = cells per row
        dict.__init__(self)
        for i in range(m):
            self[i] = dict()
            for j in range(n):
                if fill == 'random':
                    self[i][j] = randint(0, 9)
                else :
                    self[i][j] = fill
                
    def __repr__(self):
        S = ''
        for i in range(self.m):
            S += '\n'
            for j in range(self.n):
                S += ' ' + str(self[i][j]) + ' '
        return S

    __str__ = __repr__

class Screen(Grid):
    """ Used for displaying a portion of the grid centred on a 
    particular tile (roguelike-style.) """

    def __init__(self, root:'Grid', m=3, n=3):
        Grid.__init__(self, m, n, fill='.')
        self.curX = root.m //2
        self.curY = root.n //2
        I = 0
        for i in range(self.curX-(m//2)-1, self.curX+(m//2)):
            J = 0
            for j in range(self.curY-(n//2)-1, self.curY+(n//2)):
                self[I][J] = root[i][j]
                J += 1
            I += 1

""" Test : """
if __name__ == '__main__':
    G = Grid(18, 18)
    print(G)
    S = Screen(G)
    print(S)
