#!/usr/bin/env python
# -*- coding: ISO-8859-1 -*-
#########################################################################
# Script                : Pestañas.py                                   #
# Author                : Ulises Cáceres Rui-Perez   UCAIsia S. A.      #
# Propiedad Intelectual : Inversiones UCAIsia S. A.                     #
# Derechos  de Uso      : Inversiones UCAIsia S. A.                     #
# Fecha                 : 09.10.2019 a las 15:25 Hrs.                   #
# Objetetivo            : Pestañas del sistema principal.               #
# Versión               : 1.0.0.0                                       #
#########################################################################

import os, sys
import tkinter as tk
from tkinter import ttk

class Application(ttk.Frame):
    def __init__(self, main_window):
        super().__init__(main_window)
        main_window.title("Sistema de Procesamiento Automático")

        # Crear el panel de pestañas.
        self.notebook = ttk.Notebook(self)

        # Crear el contenido de cada una de las pestañas.
        self.web_label = ttk.Label(self.notebook, text="www.recursospython.com")
        self.forum_label = ttk.Label(self.notebook, text="foro.recursospython.com")

        # Añadirlas al panel con su respectivo texto.
        self.notebook.add(self.web_label, text="Web", padding=20)
        self.notebook.add(self.forum_label, text="Foro", padding=20)

        self.notebook.pack(padx=10, pady=10)
        self.pack()

main_window = tk.Tk()
app = Application(main_window)
app.mainloop()
