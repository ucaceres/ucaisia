#!/usr/bin/env python
# -*- coding: ISO-8859-1 -*-
#########################################################################
# Script                : CnxDataBaseMSSQLServer2016.py                 #
# Author                : Ulises Cáceres Rui-Perez   UCAIsia S. A.      #
# Propiedad Intelectual : Inversiones UCAIsia S. A.                     #
# Derechos  de Uso      : Inversiones UCAIsia S. A.                     #
# Fecha                 : 09.10.2019 a las 15:25 Hrs.                   #
# Objetetivo            : Proceso que abre una conexion con la base de  #
#                         datos.                                        #
# Versión               : 1.0.0.0                                       #
#########################################################################

import pymssql

Conn = pymssql.connect(server='UCAISIA0000\MSSQLSERVER', user='sa', password='LadelMaestro', database='PortalCliente')

cursor = Conn.cursor()
cursor.execute('Select * From PORTAL_PAR_PAISES;')
Row = cursor.fetchone()
while Row:
    print (str(Row[0]) + " " + str(Row[1]) + " " + str(Row[2]) + " " + str(Row[3]) + " " + str(Row[4]) + " " + str(Row[5]))     
    Row = cursor.fetchone()
Conn.close()
