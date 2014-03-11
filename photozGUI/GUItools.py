"""

Quick Tools for GUI purpose
============================

"""

import Tkinter as Tk
from matplotlib import figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg

__author__ = 'jiayiliu'


class Message(Tk.Toplevel):
    """
    pop warning message

    :param master: master window
    :param text: message to show
    """

    def __init__(self, text, master=None, title="Warning"):
        Tk.Toplevel.__init__(master)
        self.title(title)
        self.config(width=300)
        Tk.Message(self, text=text, width=300).pack()
        Tk.Button(self, text="OK", command=self.destroy).pack()


class PlotWindow(Tk.Toplevel):
    """
    individual plot window

    :param master: the master window
    """

    def __init__(self, master=None, title="Plotting"):
        """ Initialize a plotting window

        :param master: the master window
        """
        Tk.Toplevel.__init__(self, master)
        self.title(title)
        self.figure = figure.Figure(figsize=(8, 8))
        self.canvas = FigureCanvasTkAgg(self.figure, master=self)
        self.axis = self.figure.add_subplot(111)
        self.canvas.show()
        self.canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)
        NavigationToolbar2TkAgg(self.canvas, self).update()
        self.canvas._tkcanvas.pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)

    def clf(self):
        """
        Clean current plot
        """
        self.figure.clf()
        self.axis = self.figure.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.figure, master=self)
        self.canvas.show()

    def update_canvas(self):
        """
        Update the figure
        """
        self.canvas.show()
