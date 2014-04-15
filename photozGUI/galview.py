"""

Viewer for galaxy photo-z measurement
=====================================

"""
__author__ = 'jiayiliu'

import Tkinter as Tk

from sparameter import P_method, CMR_combination
from GUItools import PlotWindow


class GalViewer(Tk.Toplevel):
    """
    Viewer of MVC

    """

    def __init__(self, master):
        """
        initialize the viewer

        :param master: master window
        """
        Tk.Toplevel.__init__(self, master)
        self.title("Sketch and CMR viewer")
        # Data loading part
        ## Cluster information
        frame_data = Tk.Frame(self)
        frame_data.grid()
        Tk.Label(frame_data, text="ID:").grid(row=0, column=0, columnspan=2)
        self.entry_id = Tk.Entry(frame_data)
        self.entry_id.grid(row=0, column=2)
        self.button_load = Tk.Button(frame_data, text="Load")
        self.button_load.grid(row=0, column=3)
        ## FITS files
        self.button_fits_gri = Tk.Button(frame_data, text="FITS gri", state=Tk.DISABLED)
        self.button_fits_gri.grid(row=1, column=0)
        self.button_fits_riz = Tk.Button(frame_data, text="FITS riz", state=Tk.DISABLED)
        self.button_fits_riz.grid(row=1, column=1)
        self.button_fits_grz = Tk.Button(frame_data, text="FITS grz", state=Tk.DISABLED)
        self.button_fits_grz.grid(row=1, column=2)
        self.button_sketch = Tk.Button(frame_data, text="Sketch", state=Tk.DISABLED)
        self.button_sketch.grid(row=1, column=3)
        # Sketch part
        frame_sketch = Tk.Frame(self)
        frame_sketch.grid()
        self.button_cmr = dict()  # create button for cmr plot
        self.cmr_window = dict()  # hold cmr_window
        for ii, i in enumerate(CMR_combination):
            self.button_cmr[i] = Tk.Button(frame_sketch, state=Tk.DISABLED, text=i)
            self.button_cmr[i].grid(row=0, column=ii)
        # Selection part
        frame_select = Tk.Frame(self)
        frame_select.grid()
        self.button_select_sketch = Tk.Button(frame_select, text="Select sketch", state=Tk.DISABLED)
        self.button_select_sketch.grid(row=0, column=0)
        self.button_update_select = Tk.Button(frame_select, text="Update", state=Tk.DISABLED)
        self.button_update_select.grid(row=0, column=1)
        self.button_resample = Tk.Button(frame_select, text="Resample", state=Tk.DISABLED)
        self.button_resample.grid(row=0, column=2)
        self.redshift = Tk.DoubleVar()
        self.str_redshift = Tk.StringVar()
        Tk.Label(frame_select, textvariable=self.str_redshift).grid(row=1, column=0, columnspan=2)
        self.z_scale = Tk.Scale(frame_select, from_=0, to=1.6, orient=Tk.HORIZONTAL, resolution=0.01, length=320,
                                variable=self.redshift, showvalue=0)
        self.z_scale.grid(row=1, column=2, columnspan=4)

        # Saving part
        frame_save = Tk.Frame(self)
        frame_save.grid()
        self.button_save_reg = Tk.Button(frame_save, text="Save Region", state=Tk.DISABLED)
        self.button_save_reg.grid(row=0, column=0)
        self.button_clean = Tk.Button(frame_save, text="Clean Region", state=Tk.DISABLED)
        self.button_clean.grid(row=0, column=1)
        self.button_save_cat = Tk.Button(frame_save, text="Save Catalog", state=Tk.DISABLED)
        self.button_save_cat.grid(row=0, column=2)
        # cluster information panel
        frame_cluster = Tk.Frame(self)
        frame_cluster.grid()
        self.button_method = {}
        for j in range(len(P_method)):
            self.button_method[j] = Tk.Button(frame_cluster, text=P_method[j])
            self.button_method[j].grid(row=0, column=j)
        self.label_cluster_info = Tk.Label(frame_cluster)
        self.label_cluster_info.grid(row=1, column=0, columnspan=3)
        self.sketch = None
        self.multi_list = None
        self.button_save_reg_confirm = None
        self.window_save = None

    def close_save_window(self):
        """
        safely remove save window
        """
        self.window_save.destroy()
        del self.window_save
        self.window_save = None

    def create_cmr(self, color):
        """
        create figure to show galaxy color-magnitude relation

        :param color: color combination to create
        """
        self.cmr_window[color] = PlotWindow(master=self, title="CMR {0:s}".format(color))
        return self.cmr_window[color].axis

    def save_window(self):
        """
        create save region file window
        """
        if self.window_save is None:
            self.window_save = Tk.Toplevel(self)
            self.window_save.protocol("WM_DELETE_WINDOW", self.close_save_window)
        self.window_save.title("Save region files")
        NAMES = ["Sketch"] + CMR_combination
        self.multi_list = Tk.Listbox(self.window_save, selectmode=Tk.MULTIPLE)
        self.multi_list.pack()
        for i in range(6):
            self.multi_list.insert(Tk.END, NAMES[i])
        self.button_save_reg_confirm = Tk.Button(self.window_save, text="Save")
        self.button_save_reg_confirm.pack()


