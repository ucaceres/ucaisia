#!/usr/bin/env python
# -*- coding: ISO-8859-1 -*-
#########################################################################
# Script                : CnxDataBaseDB2.py                             #
# Author                : Ulises Cáceres Rui-Perez   UCAIsia S. A.      #
# Propiedad Intelectual : Inversiones UCAIsia S. A.                     #
# Derechos  de Uso      : Inversiones UCAIsia S. A.                     #
# Fecha                 : 09.10.2019 a las 15:25 Hrs.                   #
# Objetetivo            : Proceso que abre una conexion con la base de  #
#                         datos.                                        #
# Versi¦n               : 1.0.0.0                                       #
#########################################################################

from ibm_db import connect
# Cuidado con la puntuación aquí: tenemos 3 argumentos.
# El primero es una cadena grande con punto y coma.
# (Cadenas separadas solo por espacios en blanco, nuevas líneas incluidas,
# se unen automáticamente, en caso de que no lo supiera).
# Los dos últimos son cadenas vacías.
connection = connect('DATABASE=<database name>;'
                     'HOSTNAME=<database ip>;'  # 127.0.0.1 o localhost funciona si es local
                     'PORT=<database port>;'
                     'PROTOCOL=TCPIP;'
                     'UID=<database username>;'
                     'PWD=<username password>;', '', '')
					 
def results(command):
    from ibm_db import fetch_assoc

    ret = []
    result = fetch_assoc(command)
    while result:
         # Esto crea una lista en la memoria. Teóricamente, si hay muchas filas,
         # podríamos quedarnos sin memoria. En la práctica, nunca me ha pasado eso.
         # Si alguna vez es un problema, podría usar
         # resultado de rendimiento
         # Entonces esta función se convertiría en un generador. Pierdes la capacidad de acceder
         # resultados por índice o cortarlos o lo que sea, pero conserva
         # la capacidad de iterar sobre ellos.        ret.append(result)
        result = fetch_assoc(command)
    return ret  # Deshágase de esta línea si elige usar un generador.

from ibm_db import tables

t = results(tables(connection))

from ibm_db import exec_immediate

sql = 'LIST * FROM ' + t[170]['TABLE_NAME']  # Usando nuestra lista de tablas t de antes ...
rows = results(exec_immediate(connection, sql))

