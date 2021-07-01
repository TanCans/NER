#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 6.0.1
#  in conjunction with Tcl version 8.6
#    Apr 28, 2021 02:08:02 PM CEST  platform: Windows NT

import sys
from PIL import Image, ImageTk

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import runModel3_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    runModel3_support.set_Tk_var()

    image1 = Image.open("IPK.png")
    image1 = image1.resize((201, 100), Image.ANTIALIAS)
    test = ImageTk.PhotoImage(image1)
    label1 = tk.Label(image=test)
    label1.image = test
    # Position image
    label1.place(relx=0, rely=0)

    from tkinter import Canvas, PhotoImage

    canvas = Canvas(root, width=150, height=150, highlightthickness=0)
    canvas.place(relx=0.74, rely=-0.04)
    img = Image.open("openNext.png")
    img = img.resize((153, 150), Image.ANTIALIAS)
    canvas.image = ImageTk.PhotoImage(img)
    canvas.create_image(75, 75, image=canvas.image)

    top = Toplevel1(root)
    runModel3_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    runModel3_support.set_Tk_var()
    top = Toplevel1 (w)
    runModel3_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '+'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("600x450+602+194")
        top.minsize(148, 1)
        top.maxsize(1924, 1030)
        top.resizable(1,  1)
        top.title("NER Application")
        top.configure(background="#2ca971")

        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.4, rely=0.7, height=53, relwidth=0.2)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(command=runModel3_support.urlButton)
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Run Model''')

        self.Entry3 = tk.Entry(top)
        self.Entry3.place(relx=0.1, rely=0.45, height=108, relwidth=0.8)
        self.Entry3.configure(background="white")
        self.Entry3.configure(disabledforeground="#a3a3a3")
        self.Entry3.configure(font="TkFixedFont")
        self.Entry3.configure(foreground="#000000")
        self.Entry3.configure(insertbackground="black")
        self.Entry3.configure(textvariable=runModel3_support.urlLabel)

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.275, rely=0.37, height=26, relwidth=0.45)
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''Enter an appropedia url or a corpus text below''')

if __name__ == '__main__':
    vp_start_gui()





