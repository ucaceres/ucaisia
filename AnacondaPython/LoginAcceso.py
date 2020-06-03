#!/usr/bin/env python
# -*- coding: ISO-8859-1 -*-
#########################################################################
# Script                : LoginAcceso.py                                #
# Author                : Ulises Cáceres Rui-Perez   UCAIsia S. A.      #
# Propiedad Intelectual : Inversiones UCAIsia S. A.                     #
# Derechos  de Uso      : Inversiones UCAIsia S. A.                     #
# Fecha                 : 09.10.2019 a las 15:25 Hrs.                   #
# Objetetivo            : Acceso controlado a una aplicación por medio  #
#                         de un login.                                  #
# Versión               : 1.0.0.0                                       #
#########################################################################

from tkinter import *
from tkinter.messagebox import *
from LogInAvanzado.UserF import * 

#########################################################################
# En Python 3.X, para poder llamar una "clase" es necesario usar 'from' #
# Y escribir el nombre de nuestro Paquete/Directorio y con punto '.'    #
# llamamas nuestro archivofrom LogInAvanzado.PassF import clave #Tambien#
# podemos definir que queremos importar de ese archivo, en este caso la #
#funcion "clave"                                                        #
#########################################################################

def checkUser(): 
    #########################################################################
    # Esta Funcion se encarga de verificar que la Entrada del Usuario sea   #
    # valida de acuerdo a los parametros requeridos (más de 8 caracteres,   #
    # menos de 12, Alfanumerico)                                            #
    #########################################################################
    if nickname(CatchUser.get()) == True:
        showinfo("Exito!","Nombre de Usuario Valido!")
        confirm_user.config(fg="Green")
        TUser.config(fg="Green")
        TPassword.grid()
        #########################################################################
        # Teniendo ya definido el Grid de nuestra etiqueta, poner solo .grid()  #
        # lo hara visible de nuevo, esto es valido para la mayoria de los       #
        # objetos que se hayan puesto en el grid()                              #
        #########################################################################
        CatchPsswd.grid()
        confirm_pssw.grid()
        ready_req.grid()
        CatchUser.config(state="disabled")
        #########################################################################
        # Con la funcion .config y el parametro 'State' en "Disabled" nosotros  #
        # deshabilitamos este elemento grafico, asi impedimos que el Usuario    #
        # pueda alterar el valor ingresado y capturado                          #
        #########################################################################
    else:
        confirm_user.config(fg="Red")
        TUser.config(fg="Red")

def checkPssw():
    if clave(CatchPsswd.get())==True:
        showinfo("Exito!","Contraseña Valida!")
        confirm_pssw.config(fg="Green")
        TPassword.config(fg="Green")
    else:
        confirm_pssw.config(fg="Red")
        TPassword.config(fg="Red")

def CompleteRequest():
    if nickname(CatchUser.get()) == True and clave(CatchPsswd.get()) == True:
        TUser.config(fg="Green")
        TPassword.config(fg="Green")
        CatchUser.config(bg="Green", fg="White")
        CatchPsswd.config(bg="Green", fg="White")
        showinfo("Felicidades!","Usuario y Contraseña creados exitosamente!")
    else:
        TUser.config(fg="Red")
        TPassword.config(fg="Red")

def reiniciar():
    #########################################################################
    # Esta función se encarga de limpiar la interfaz, es decir volver la    #
    # interfaz al principio                                                 #
    #########################################################################
    TUser.config(fg="black")
    TPassword.config(fg="black")
    CatchUser.config(bg="white", fg="black")
    CatchUser.delete(0, END)
    #########################################################################
    # la Función .delete() se encarga de "Borrar" el contenido de los       #
    # elementos, en este caso, nuestro Entry quedara vacio pero conserva sus#
    # caracteristicas                                                       #
    #########################################################################
    CatchPsswd.config(bg="white", fg="black")
    CatchPsswd.delete(0,END)
    confirm_user.config(fg="black")
    confirm_pssw.config(fg="black")
    TPassword.grid_remove()
    CatchPsswd.grid_remove()
    confirm_pssw.grid_remove()
    ready_req.grid_remove()
    CatchUser.config(state="normal")

app = Tk()
app.title("Control de Acceso")
app.geometry("600x400")
app.config(bg="Crimson")

vp = Frame(app)
vp.grid(column=0, row=0, padx=(50,50), pady=(10,10))
vp.rowconfigure(0, weight=1)
vp.columnconfigure(0, weight=1)
vp.config(bg="#F0F0F0")

TUser = Label(vp, text="Usuario: ")
TUser.grid(column=1, row=1, sticky=E, padx=(10,10),pady=(10,10))

TPassword = Label(vp, text="Contraseña: ")
TPassword.grid(column=1, row=2, sticky=E, padx=(10,10), pady=(10,10))
TPassword.grid_remove()
#########################################################################
# La Función .grid_remove() "remueve" el elemento Grafico, pero conserva#
# sus datos tales como Columna, Renglon, etc. Esto es Valido para la    #
# mayoria de los elementos de Tkinter                                   #
#########################################################################
field1 = CatchUser = Entry(vp, width=20, textvariable=field1)
CatchUser.grid(column=2, row=1, padx=(10,10))

field2 = CatchPsswd = Entry(vp, width=20, show='•', textvariable=field2)
CatchPsswd.grid(column=2, row=2, padx=(10,10))
CatchPsswd.grid_remove()

confirm_user = Button(vp, text="Verificar Usuario", command=checkUser)
confirm_user.grid(column=3, row=1, padx=(10,10), pady=(10,10))

confirm_pssw = Button(vp, text="Comprobar Contraseña", command=checkPssw)
confirm_pssw.grid(column=3, row=2, padx=(10,10), pady=(10,10))
confirm_pssw.grid_remove()

ready_req = Button(vp, text="Listo", command=CompleteRequest)
ready_req.grid(column=1, row=3, padx=(10,10), pady=(10,10))
ready_req.grid_remove()

resetGUI = Button(vp, text="Limpiar Registro", command=reiniciar)
resetGUI.grid(column=2,row=3, padx=(10,10), pady=(10,10), sticky=E)

app.mainloop()
