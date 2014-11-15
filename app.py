#-*- coding: utf-8
# mael.cadorel@laposte.net


""" Random snippets for practice. """


from grid import Grid, Screen
from gridViewer import GridViewer
from gui import GUI


class Data(dict):
    """ Used for application-layer storage of resources. """
    
    def __init__(self):
        dict.__init__(self)
        

class App(object):
    """ Main executable. Composed of
    - Data
    - GUI
    - GridViewer widget. """
    
    def __init__(self):
        pass
