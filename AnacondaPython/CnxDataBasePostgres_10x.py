#!/usr/bin/env python
# -*- coding: ISO-8859-1 -*-
#########################################################################
# Script                : CnxDataBasePostgres_10x.py                    #
# Author                : Ulises Cáceres Rui-Perez   UCAIsia S. A.      #
# Propiedad Intelectual : Inversiones UCAIsia S. A.                     #
# Derechos  de Uso      : Inversiones UCAIsia S. A.                     #
# Fecha                 : 09.10.2019 a las 15:25 Hrs.                   #
# Objetetivo            : Proceso que abre una conexion con la base de  #
#                         datos.                                        #
# Versi¦n               : 1.0.0.0                                       #
#########################################################################

import psycopg2
import sys

PSQL_HOST = "localhost"
PSQL_PORT = "5432"
PSQL_USER = "postres"
PSQL_PASS = "LadelMaestro"
PSQL_DB   = "postgres"
Query = "Select Id, Nombre, Edad From Public.Mascotas;"
Cnx = ""
Cur = ""
Result = ""

#PSQL_HOST = sys.argv[1]
#PSQL_PORT = sys.argv[2]
#PSQL_USER = sys.argv[3]
#PSQL_PASS = sys.argv[4]
#PSQL_DB   = sys.argv[5]
#DB_QRYS   = sys.argv[6]
#Query     = "Select * From Mascotas Where ID = %d;" % DB_QRYS

try:
#    ConnStr = "dbname=%s user=%s password=%s host=%s port=%s" % (PSQL_DB, PSQL_USER, PSQL_PASS, PSQL_HOST, PSQL_PORT)
    Conn = psycopg2.connect("dbname=postgres user=postgres password=UCAIsiaSA2016 host=192.168.118.1 port=5432")
#    Conn = psycopg2.connect(ConnStr)
    Cur = Conn.cursor()
    SqlQuery = "Select Id, Nombre, Edad From Public.Mascotas;"
    Cur.execute(SqlQuery)
    Result = Cur.fetchall()
    Cur.close()
    Conn.close()
    for mascota in Result:
        print(mascota)
except psycopg2.Error as e:
    print("Ocurrió un error al editar: ", e)
#   print ("Error al conectarse a la Base de Datos: %s", str(e))
