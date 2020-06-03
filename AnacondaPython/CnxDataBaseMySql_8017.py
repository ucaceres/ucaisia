#!/usr/bin/env python
# -*- coding: utf-8 -*-
#########################################################################
# Script                : CnxDataBaseMySql_8017.py                      #
# Author                : Ulises Cáceres Rui-Perez   UCAIsia S. A.      #
# Propiedad Intelectual : Inversiones UCAIsia S. A.                     #
# Derechos  de Uso      : Inversiones UCAIsia S. A.                     #
# Fecha                 : 09.10.2019 a las 15:25 Hrs.                   #
# Objetetivo            : Proceso que abre una conexion con la base de  #
#                         datos.                                        #
# Versión               : 1.0.0.0                                       #
#########################################################################

import pymysql
import sys

import argparse

DB_IPAD = "192.168.118.1"
DB_IPAD = "localhost"
DB_PORT = 3306
DB_NAME = "Automatizado"
DB_USER = "automata"
DB_PASS = "LadeSixbell2017"
Query = " Select * From Comandos "
Result = ""

#DB_IPAD = sys.argv[1]
#DB_PORT = sys.argv[2]
#DB_NAME = sys.argv[3]
#DB_USER = sys.argv[4]
#DB_PASS = sys.argv[5]
#DB_QRYS = sys.argv[6]
#Query = " Select * From Comandos Where CMDOSERVER = \'%s\' " % DB_QRYS

try:
    db_connection = pymysql.connect(DB_IPAD, DB_USER, DB_PASS, DB_NAME)
    my_cursor = db_connection.cursor()
    my_cursor.execute(Query)
    Result = my_cursor.fetchall()
    my_cursor.close()
    db_connection.close()
except pymysql.Error as mysql_error:
    print ("Error al conectarse a la Base de Datos: %s", str(mysql_error))

print ("Se encontraron :%d registros", len(Result))

if len(Result) > 0:
    for record in Result:
        print (record)
else:
    print (Result)
