#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.15
# In conjunction with Tcl version 8.6
#    Oct 02, 2018 10:20:38 PM

import sys
import dao
import matplotlib.pyplot as plt

try:
    from Tkinter import *
except ImportError:
    from tkinter import *
    from tkinter import messagebox

try:
    import ttk

    py3 = False
except ImportError:
    import tkinter.ttk as ttk

    py3 = True

import trips_support


def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = Trips(root)
    trips_support.init(root, top)
    root.mainloop()


w = None
plot = None


def create_Trips(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel(root)
    top = Trips(w)
    trips_support.init(w, top, *args, **kwargs)
    return (w, top)


def destroy_Trips():
    global w
    w.destroy()
    w = None


def plot_data(trips, distance, vd):
    global x, y1, y2
    y1 = trips
    y2 = distance
    x = vd


class Trips:
    def plot_graph(self):
        global plot, x, y2
        try:
            plt.bar(x, y2, label='Distance')
            plt.legend()
            plt.show()
        except Exception:
            messagebox.showerror("Plotting Graph", "First Select Drivers or Vehicles")

    def show_all_trips(self):
        self.Listbox.delete(0, self.Listbox.size())
        self.Listbox.insert(END,
                            "{:9s} {:20s} {:15s} {:7s} {:12s}".format('Trip Id', 'Date', 'Distance(kms)', 'Driver ID',
                                                                      'Vehicle'))
        for item in dao.get_trips():
            self.Listbox.insert(END,
                                "{:9s} {:20s} {:15s} {:7s} {:12s}".format(str(item[0]), item[1], str(item[2]),
                                                                          str(item[3]), item[4]))

    def show_vehicle_trips(self):
        global plot
        trips = []
        distance = []
        vehicle = []
        self.Listbox.delete(0, self.Listbox.size())
        self.Listbox.insert(END, "{:20s} {:20s} {:20s}".format('Total Trips', 'Total Distance(kms)', 'Vehicle'))
        for item in dao.get_trips_by_vehicle():
            self.Listbox.insert(END, "{:30s} {:30s} {:20s}".format(str(item[0]), str(item[1]), item[2]))
            trips.append(item[0])
            distance.append(item[1])
            vehicle.append(item[2])
        plot = 'V'
        plot_data(trips, distance, vehicle)

    def show_driver_trips(self):
        global plot
        trips = []
        distance = []
        driver = []
        self.Listbox.delete(0, self.Listbox.size())
        self.Listbox.insert(END, "{:20s} {:20s} {:20s}".format('Total Trips', 'Total Distance(kms)', 'Driver ID'))
        for item in dao.get_trips_by_driver():
            self.Listbox.insert(END, "{:30s} {:30s} {:20s}".format(str(item[0]), str(item[1]), str(item[2])))
            trips.append(item[0])
            distance.append(item[1])
            driver.append(str(item[2]))
        plot = 'D'
        plot_data(trips, distance, driver)

    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#d9d9d9'  # X11 color: 'gray85'
        font9 = "-family Roboto -size 24 -weight normal -slant roman " \
                "-underline 0 -overstrike 0"
        font8 = "-family Roboto -size 19 -weight normal -slant roman " \
                "-underline 0 -overstrike 0"

        top.geometry("896x816+604+87")
        top.title("Trips")
        top.configure(background="#bdafd8")

        self.Label1 = Label(top)
        self.Label1.place(relx=0.33, rely=0.0, height=125, width=302)
        self.Label1.configure(background="#bdafd8")
        self._img1 = PhotoImage(file="images/trips.png")
        self.Label1.configure(image=self._img1)
        self.Label1.configure(text='''Label''')

        self.Label2 = Label(top)
        self.Label2.place(relx=0.08, rely=0.16, height=53, width=132)
        self.Label2.configure(background="#bdafd8")
        self.Label2.configure(font=font9)
        self.Label2.configure(text='''Sort By:''')

        self.allButton = Button(top)
        self.allButton.place(relx=0.26, rely=0.16, height=61, width=69)
        self.allButton.configure(activebackground="#d9d9d9")
        self.allButton.configure(background="#736b84")
        self.allButton.configure(font=font9)
        self.allButton.configure(foreground="#ffffff")
        self.allButton.configure(text='''All''')
        self.allButton.configure(command=self.show_all_trips)

        self.driverButton = Button(top)
        self.driverButton.place(relx=0.38, rely=0.16, height=61, width=142)
        self.driverButton.configure(activebackground="#d9d9d9")
        self.driverButton.configure(background="#736b84")
        self.driverButton.configure(font=font9)
        self.driverButton.configure(foreground="#ffffff")
        self.driverButton.configure(text='''Drivers''')
        self.driverButton.configure(command=self.show_driver_trips)

        self.vehicleButton = Button(top)
        self.vehicleButton.place(relx=0.59, rely=0.16, height=61, width=167)
        self.vehicleButton.configure(activebackground="#d9d9d9")
        self.vehicleButton.configure(background="#736b84")
        self.vehicleButton.configure(font=font9)
        self.vehicleButton.configure(foreground="#ffffff")
        self.vehicleButton.configure(text='''Vehicles''')
        self.vehicleButton.configure(command=self.show_vehicle_trips)

        self.plotButton = Button(top)
        self.plotButton.place(relx=0.45, rely=0.86, height=61, width=92)
        self.plotButton.configure(activebackground="#d9d9d9")
        self.plotButton.configure(background="#7a00d8")
        self.plotButton.configure(font=font9)
        self.plotButton.configure(foreground="#ffffff")
        self.plotButton.configure(text='''Plot''')
        self.plotButton.configure(command=self.plot_graph)

        self.Listbox = Listbox(top)
        self.Listbox.place(relx=0.04, rely=0.25, relheight=0.59, relwidth=0.9)
        self.Listbox.configure(background="#e3d1ff")
        self.Listbox.configure(font=font8)
        self.Listbox.configure(width=804)

        self.scrollbar = Scrollbar(self.Listbox)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.scrollbar.config(command=self.Listbox.yview)


if __name__ == '__main__':
    vp_start_gui()
