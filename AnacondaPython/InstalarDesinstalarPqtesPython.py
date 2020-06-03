#!/usr/bin/env python
# -*- coding: ISO-8859-1 -*-
#########################################################################
# Script                : InstalarDesinstalarPqtesPython.py             #
# Author                : Ulises Cáceres Rui-Perez   UCAIsia S. A.      #
# Propiedad Intelectual : Inversiones UCAIsia S. A.                     #
# Derechos  de Uso      : Inversiones UCAIsia S. A.                     #
# Fecha                 : 09.10.2019 a las 15:25 Hrs.                   #
# Objetetivo            : Herramienta para instalar / desinstalar un    #
#                         paquete Python.                               #
# Versión               : 1.0.0.0                                       #
#########################################################################

import os, sys
import tkinter as tk
from PIL import ImageTk, Image
import time
from tkinter import messagebox
root= tk.Tk()

def installPackage ():
    global installPythonPackage
    installPythonPackage = 'pip install ' + Entry1.get()
    os.system('start cmd /k ' + installPythonPackage)

def uninstallPackage ():
    global uninstallPythonPackage
    uninstallPythonPackage = 'pip uninstall ' + Entry1.get()
    os.system('start cmd /k ' + uninstallPythonPackage)

def Minimizar():
    root.iconify()
    time.sleep(5)
    root.deiconify()

def Salir():
    root.quit()

def RegistrarServidor():
    messagebox.showinfo(message="Registrar Servidor !!!!!", title="Registrar Servidor")
def EspacioDisponibleDisco():
    messagebox.showinfo(message="Espacio Disponible en Disco !!!!!", title="Espacio Disponible en Disco")
def DisponibilidadBD():
    messagebox.showinfo(message="Disponibilidad de Base de Datos !!!!!", title="Disponibilidad de Base de Datos")
def TransmisionInterfaces():
    messagebox.showinfo(message="Transmisión de las Interfaces !!!!!", title="Transmisión de las Interfaces")
def CargaMasiva():
    messagebox.showinfo(message="Carga Masiva de Información !!!!!", title="Carga Masiva de Información")
def Calendarizacion():
    messagebox.showinfo(message="Calendarización de Procesos !!!!!", title="Calendarización de Procesos")
def EspacioDisponibleBD():
    messagebox.showinfo(message="Espacio Disponible en Base de Datos !!!!!", title="Espacio Disponible en Base de Datos")
def DisponibilidadWeb():
    messagebox.showinfo(message="Disponibilidad Web !!!!!", title="Disponibilidad Web")
def MenuConsultas():
    messagebox.showinfo(message="Menú de Consultas !!!!!", title="Menú de Consultas")
def MenuMantenedores():
    messagebox.showinfo(message="Menú de Mantenedores !!!!!", title="Menú de Mantenedores")
def Hola():
    messagebox.showinfo(message="Hola Compadre !!!!!", title="Hola")

root.title("Sistema de Procesamiento Automático")
MenuBarra = tk.Menu(root)

MenuArchivo = tk.Menu(MenuBarra, tearoff=0)
MenuArchivo.add_command(label="Minimizar", command=Minimizar)
MenuArchivo.add_command(label="Instalar", command=installPackage)
MenuArchivo.add_command(label="DesInstalar", command=uninstallPackage)
MenuArchivo.add_separator()
MenuArchivo.add_command(label="Salir", command=root.quit)
MenuBarra.add_cascade(label="Archivo", menu=MenuArchivo)

MenuEditar = tk.Menu(MenuBarra, tearoff=0)
MenuEditar.add_command(label="Cortar", command=Hola)
MenuEditar.add_command(label="Copiar", command=Hola)
MenuEditar.add_command(label="Pegar", command=Hola)
MenuBarra.add_cascade(label="Editar", menu=MenuEditar)

MenuAyuda = tk.Menu(MenuBarra, tearoff=0)
MenuAyuda.add_command(label="Acerca de...", command=Hola)
MenuBarra.add_cascade(label="Ayuda", menu=MenuAyuda)

MenuOperacion = tk.Menu(MenuBarra, tearoff=0)
MenuOperacion.add_command(label="Registrar un Servidor", command=RegistrarServidor)
MenuOperacion.add_command(label="Espacio Disponible en Disco", command=EspacioDisponibleDisco)
MenuOperacion.add_command(label="Disponibilidad de Base de Datos", command=DisponibilidadBD)
MenuOperacion.add_command(label="Transmisión de las Interfaces", command=TransmisionInterfaces)
MenuOperacion.add_command(label="Carga Masiva de Información", command=CargaMasiva)
MenuOperacion.add_command(label="Calendarización de Procesos", command=Calendarizacion)
MenuOperacion.add_command(label="Espacio Disponible en Base de Datos", command=EspacioDisponibleBD)
MenuOperacion.add_command(label="Disponibilidad Web", command=DisponibilidadWeb)
MenuOperacion.add_separator()
MenuOperacion.add_command(label="Sub. Menú de Consultas", command=MenuConsultas)
MenuOperacion.add_separator()
MenuOperacion.add_command(label="Sub. Menú de Mantenedores", command=MenuMantenedores)
MenuOperacion.add_separator()
MenuBarra.add_cascade(label="Operaciones", menu=MenuOperacion)

root.config(menu=MenuBarra)
root.overrideredirect(False)
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))

Path0 = r'''F:\Proyectos\UCaisia S.A\Img\UCAIsia S. A\Logo_UCAIsiaSA.gif'''
Path1 = r'''F:\Proyectos\UCaisia S.A\Img\UCAIsia S. A\Logo01.gif'''
ImgIzq = ImageTk.PhotoImage(Image.open(Path0))
ImgDer = ImageTk.PhotoImage(Image.open(Path1))
########################################################################################################
# Los valores posibles del parámetro anchor son: "n", "ne", "e", "se", "s", "sw", "w", "nw" y "center" #
########################################################################################################
w0 = tk.Canvas(root, width=300, height=300)
w0.place(relwidth=1, relheight=1)
w0.create_image(2, 5, image=ImgIzq, anchor="nw")

Lbl0 = tk.Label(root, text="Sistema de Procesamiento Automatizado", bd = 5, fg = 'black', font =('arial', 20, 'bold'), anchor="n", relief = 'raised')
Lbl0.pack()

#w1 = tk.Canvas(root, width=200, height=200)
#w1.create_image(200, 200, image=ImgDer, anchor="se")
#w1.pack()

#Cnv1 = tk.Canvas(root, width = 1350, height = 695, bg = 'gray90', relief = 'raised')
Cnv1 = tk.Canvas(root, width = 300, height = 400, bg = 'red', relief = 'raised')
Cnv1.pack()

Lbl1 = tk.Label(root, text='Tipo de Paquete:', bg = 'gray90')
Lbl1.config(font=('arial', 12))
Cnv1.create_window(1340, 690, window=Lbl1)

Entry1 = tk.Entry (root, width=27)
Cnv1.create_window(150, 120, window=Entry1)

Btn1 = tk.Button(text='Instalar Paquetes', command=installPackage, bg='green', fg='white', font=('arial', 12, 'bold'))
Cnv1.create_window(150, 180, window=Btn1)
Btn2 = tk.Button(text='DesInstalar Paquetes', command=uninstallPackage, bg='coral3', fg='white', font=('arial', 12, 'bold'))
Cnv1.create_window(150, 230, window=Btn2)
Btn3 = tk.Button(root, text='Minimizar', command=Minimizar, bg='blue', fg='white', font=('arial', 12, 'bold'))
Cnv1.create_window(150, 280, window=Btn3)
Btn4 = tk.Button(root, text='Salir', command=Salir, bg='red', fg='white', font=('arial', 12, 'bold'))
Cnv1.create_window(150, 330, window=Btn4)

root.iconbitmap(r'F:\Proyectos\UCaisia S.A\Iconos\DataTransformationsProject.ico')
root.mainloop()
