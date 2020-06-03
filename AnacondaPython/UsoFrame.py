#!/usr/bin/env python
# -*- coding: ISO-8859-1 -*-
#########################################################################
# Script                : UsoFrame.py                                   #
# Author                : Ulises Cáceres Rui-Perez   UCAIsia S. A.      #
# Propiedad Intelectual : Inversiones UCAIsia S. A.                     #
# Derechos  de Uso      : Inversiones UCAIsia S. A.                     #
# Fecha                 : 09.10.2019 a las 15:25 Hrs.                   #
# Objetetivo            : Programa para la utilización de diferentes    #
#                         Frames.                                       #
# Versión               : 1.0.0.0                                       #
#########################################################################

import os, sys
from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
import time
from tkinter import messagebox
root= tk.Tk()

root.title('Uso de Frames')
root.resizable(width=False, height=False)
root.overrideredirect(False)
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))

top_frame = tk.Frame(root, bg='cyan', width = 450, height=50, pady=3).grid(row=0, columnspan=3)
Label(top_frame, text = 'Uso de Frames').grid(row = 0, columnspan = 3)
Label(top_frame, text = 'Ancho:').grid(row = 1, column = 0)
Label(top_frame, text = 'Largo:').grid(row = 1, column = 2)
entry_W = Entry(top_frame).grid(row = 1, column = 1)
entry_L = Entry(top_frame).grid(row = 1, column = 3)
#Label(top_frame, text = '').grid(row = 2, column = 2)

center = Frame(root, bg='gray2', width=50, height=40, padx=3, pady=3).grid(row=1, columnspan=3)
ctr_left = Frame(center, bg='blue', width=100, height=190).grid(column = 0, row = 1, rowspan = 2)
ctr_mid = Frame(center, bg='yellow', width=250, height=190, padx=3, pady=3).grid(column = 1, row=1, rowspan=2)
ctr_right = Frame(center, bg='green', width=100, height=190, padx=3, pady=3).grid(column = 2, row=1, rowspan=2)

btm_frame = Frame(root, bg='white', width = 450, height = 45, pady=3).grid(row = 3, columnspan = 3)
btm_frame2 = Frame(root, bg='lavender', width = 450, height = 60, pady=3).grid(row = 4, columnspan = 3)

root.mainloop()
