#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.15
# In conjunction with Tcl version 8.6
#    Aug 22, 2018 07:30:09 PM

import sys
import login

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk

    py3 = False
except ImportError:
    import tkinter.ttk as ttk

    py3 = True

import OnlineCarRentalSystem_support


def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = Online_Car_Rental_System(root)
    OnlineCarRentalSystem_support.init(root, top)
    root.mainloop()


w = None


def create_Online_Car_Rental_System(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel(root)
    top = Online_Car_Rental_System(w)
    OnlineCarRentalSystem_support.init(w, top, *args, **kwargs)
    return (w, top)


def destroy_Online_Car_Rental_System():
    global w
    w.destroy()
    w = None


class Online_Car_Rental_System:
    def onClickUser(self):
        login.create_Login(root)
        login.get_root(root)
        # controller.showFrame(Login)

    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#d9d9d9'  # X11 color: 'gray85'
        font9 = "-family Roboto -size 20 -weight normal -slant roman " \
                "-underline 0 -overstrike 0"

        top.geometry("600x450+671+220")
        top.title("Online Car Rental System")
        top.configure(background="#d85600")

        self.selectUserLabel = Label(top)
        self.selectUserLabel.place(relx=0.35, rely=0.18, height=58, width=175)
        self.selectUserLabel.configure(background="#d85600")
        self.selectUserLabel.configure(font=font9)
        self.selectUserLabel.configure(foreground="#a5f7dc")
        self.selectUserLabel.configure(text='''Select User''')
        self.selectUserLabel.configure(width=175)

        self.userButton = Button(top)
        self.userButton.place(relx=0.3, rely=0.36, height=56, width=241)
        self.userButton.configure(activebackground="#d9d9d9")
        self.userButton.configure(background="#000000")
        self.userButton.configure(font=font9)
        self.userButton.configure(foreground="#fcfcfc")
        self.userButton.configure(text='''Customer''')
        self.userButton.configure(width=241)
        self.userButton.configure(command=self.onClickUser)

        self.adminButton = Button(top)
        self.adminButton.place(relx=0.3, rely=0.53, height=56, width=241)
        self.adminButton.configure(activebackground="#d9d9d9")
        self.adminButton.configure(background="#000000")
        self.adminButton.configure(font=font9)
        self.adminButton.configure(foreground="#f9f9f9")
        self.adminButton.configure(text='''Admin''')
        self.adminButton.configure(width=241)


if __name__ == '__main__':
    vp_start_gui()
