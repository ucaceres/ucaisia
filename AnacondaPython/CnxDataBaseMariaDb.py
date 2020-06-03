#!/usr/bin/env python
# -*- coding: ISO-8859-1 -*-
#########################################################################
# Script                : CnxDataBaseMariaDb.py                         #
# Author                : Ulises Cáceres Rui-Perez   UCAIsia S. A.      #
# Propiedad Intelectual : Inversiones UCAIsia S. A.                     #
# Derechos  de Uso      : Inversiones UCAIsia S. A.                     #
# Fecha                 : 09.10.2019 a las 15:25 Hrs.                   #
# Objetetivo            : Proceso que abre una conexion con la base de  #
#                         datos.                                        #
# Versi¦n               : 1.0.0.0                                       #
#########################################################################

import mysql.connector as mariadb

# decodigo.com
mariadb_conexion = mariadb.connect(host='localhost', port='3306', user='root', password='LadelMaestro', database='Pruebas')
cursor = mariadb_conexion.cursor()
try:
    cursor.execute("SELECT ID, NOMBRE FROM MiTabla")
    for id, nombre in cursor:
        print("id: " + str(id))
        print("nombre: " + nombre)
except mariadb.Error as error:
    print("Error: {}".format(error))

    mariadb_conexion.close()