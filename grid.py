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
        self.root = root
        self.m = m
        self.n = n

        # By default, a Screen is centred on the centre of the Grid it depicts
        self.curX = root.m //2
        self.curY = root.n //2

    def build(self):
        """ Builds from original grid. """
        I = 0
        for i in range(self.curX-(self.m//2)-1, self.curX+(self.m//2)):
            J = 0
            for j in range(self.curY-(self.n//2)-1, self.curY+(self.n//2)):
                self[I][J] = self.root[i][j]
                J += 1
            I += 1

    def offset(self, x, y):
        """ Moves (centres) the Screen onto another tile. x is vertical, y is horizontal. """ # needs swapping x and y!
        xmin = 1 + (self.n//2)
        xmax = self.root.n - (self.n//2)
        ymin = 1 + (self.m//2)
        ymax = self.root.m - (self.m//2)

        if self.curX + x < xmin:       # bump north
            self.curX = xmin
        elif self.curX + x > xmax:     # bump south
            self.curX = xmax
        else:
            self.curX += x
            
        if self.curY + y < ymin:       # bump west
            self.curY = ymin
        elif self.curY + y > ymax:     # bump east
            self.curY = ymax
        else:
            self.curY += y

        self.build() # TODO : definitely suboptimal

# Test :
if __name__ == '__main__':
    G = Grid(18, 18)
    print(G)
    
    S = Screen(G)
    S.build()
    print(S)
    
    print('\nBumping east : ')
    S.offset(0, 12)
    print(S)
    
    print('\nBumping north : ')
    S.offset(-64, 0)
    print(S)

    print('\nBumping south : ')
    S.offset(1281, 0)
    print(S)

    print('\nBumping west : ')
    S.offset(0, -17)
    print(S)
