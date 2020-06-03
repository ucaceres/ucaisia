#!/usr/bin/env python
# -*- coding: ISO-8859-1 -*-
#########################################################################
# Script                : Mantenedor_CRUD.py                            #
# Author                : Ulises Cáceres Rui-Perez   UCAIsia S. A.      #
# Propiedad Intelectual : Inversiones UCAIsia S. A.                     #
# Derechos  de Uso      : Inversiones UCAIsia S. A.                     #
# Fecha                 : 09.10.2019 a las 15:25 Hrs.                   #
# Objetetivo            : Proceso de mantención en la base de detos que #
#                         por medio de un parámetro, deerminará la man- #
#                         tención en la base de datos específica.       #
# Versión               : 1.0.0.0                                       #
# Parámetro             : MBD = $1 (Motor de base de Datos)             #
#                         1   = Oracle                                  #
#                         2   = MsSql Server                            #
#                         3   = MySql                                   #
#                         4   = PostgreSQL                              #
#                         5   = MongoDB                                 #
#                         6   = MariaDB                                 #
#                         7   = DB2                                     #
# Parámetro             : TdC = $2 (Tipo de CRUD)                       #
#                         1   = Insertar                                #
#                         2   = Consultar                               #
#                         3   = Actualizar                              #
#                         4   = Eliminar                                #
#########################################################################

from subprocess import call
from platform import system
import os, sys, io
import shutil
import subprocess

MBD = sys.argv[1]
TdC = sys.argv[2]
HOST = sys.argv[3]
PORT = sys.argv[4]
DBAS = sys.argv[5]
USER = sys.argv[6]
PASS = sys.argv[7]
QRY = sys.argv[8]

#print ("MBD  = ", MBD)
#print ("TdC  = ", TdC)
#print ("HOST = ", HOST)
#print ("PORT = ", PORT)
#print ("DBAS = ", DBAS)
#print ("USER = ", USER)
#print ("PASS = ", PASS)
#print ("QRY  = ", QRY)

if len(sys.argv) != 9:
    print ("ERROR: Se requieren 9 argumentos, usted introdujo %d" % (len(sys.argv) - 1))
    print ("1 = Motor de base de Datos")
    print ("2 = Tipo se Sentencia SQL")
    print ("3 = Nombre o IP del Servidor de la Bases de datos")
    print ("4 = Puerto de conexión hacia la base de datos")
    print ("5 = Nombre de la Base dedatos o el servicio asociado")
    print ("6 = Usuario de conexión a la base de datos")
    print ("7 = Clve de acceso del usuario de conexión")
    print ("8 = Senetencia SQL a realizar en la base de datos")
    print (" ")
    print ("Ejemplos de Ejecución :")
    print ("        python Mantenedor_CRUD.py 1 2 UCAISIA0000.ucaisia.cl  1521 UCRP.ucaisia.cl COFISA   LadelMaestro 'Select * From MD_ADDITIONAL_PROPERTIES;'")
    print ("        python Mantenedor_CRUD.py 2 1 UCAISIA0000\MSSQLSERVER 1433 PortalCliente   Portal   LadeSiempre  'Insert [dbo].[PORTAL_PAR_GIROSECONOMICOS] ([COD_GIROSECONOMICOS], [DESCRIPCION], [AUDITORIA_FEC_CREACION], [AUDITORIA_FEC_MODIF], [AUDITORIA_FEC_EXPIRACION]) VALUES (1000, N'Agricultura', Cast(0x00009CAB00CB3D68 AS DateTime), NULL, NULL)'")
    print ("        python Mantenedor_CRUD.py 3 3 localhost               3306 Automatizado    Automata Noteladoy    'Update MallaProceso Set CMDOSERVER = 'Get-PSDrive -PSProvider FileSystem | Sort-Object Free | Format-Table -AutoSize' Where IDTICKET = 1 And RUTEMP = 97036000 And IPSERVER = '180.123.18.140' And IDPLANTILLA = 1 And IDSISTEMA = 2 And IDTITULO = 1 And IDSECCION = 1 And IDSUBSECC = 1 And SECCMDOS = 1;")
    print (" ")
    sys.exit()

if (TdC != "1" and TdC != "2" and TdC != "3" and TdC != "4"):
    print ("ERROR: Se requieren los siguientes argumentos")
    print ("Parámetro 2 : Tipo de CRUD")
    print ("            1 = Insertar")
    print ("            2 = Consultar")
    print ("            3 = Actualizar")
    print ("            4 = Eliminar")
    sys.exit()

if (MBD == "1"):
    import cx_Oracle
    try:
        from collections.abc import defaultdict, Mapping, namedtuple
    except ImportError:
        from collections import defaultdict, Mapping, namedtuple
    try:
        Dsn_Tns = cx_Oracle.makedsn(HOST, PORT, service_name=DBAS)
        Conn = cx_Oracle.connect(user=USER, password=PASS, dsn=Dsn_Tns)
        c = Conn.cursor()
        c.execute(QRY)
        if (TdC != "2"):
            c.commit()
        else:
            for Row in c:
                print (Row)
        Conn.close()
    except cx_Oracle.DatabaseError as e:
        err, = e.args
        print ("\nERROR:".join([str(err.code),err.message,err.context]))
elif (MBD == "2"):
    import pymssql
    try:
        from collections.abc import defaultdict, Mapping, namedtuple
    except ImportError:
        from collections import defaultdict, Mapping, namedtuple
    Conn = pymssql.connect(server=HOST, user=USER, password=PASS, database=DBAS)
    cursor = Conn.cursor()
    cursor.execute(QRY)
    if (TdC == "2"):
        Row = cursor.fetchone()
        while Row:
            print (str(Row))
            Row = cursor.fetchone()
    Conn.close()
elif (MBD == "3"):
    import pymysql
    try:
        from collections.abc import defaultdict, Mapping, namedtuple
    except ImportError:
        from collections import defaultdict, Mapping, namedtuple
    DB_IPAD = HOST
    DB_PORT = PORT
    DB_NAME = DBAS
    DB_USER = USER
    DB_PASS = PASS
    Query = QRY
    try:
        db_connection = pymysql.connect(DB_IPAD, DB_USER, DB_PASS, DB_NAME)
        c = db_connection.cursor()
        c.execute(Query)
        if (TdC != "2"):
            try:
                c.commit()
            except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
	            print ("ERROR: Ha Ocurrido un error al procesar la sentencia : ", e)
        else:
            Result = c.fetchall()
            print ("Se encontraron :%d registros", len(Result))
            if len(Result) > 0:
                for Record in Result:
                    print (Record)
            else:
                print (Result)
        c.close()
        db_connection.close()
    except pymysql.Error as mysql_error:
        print ("ERROR:  al conectarse a la Base de Datos: %s", str(mysql_error))
elif (MBD == "4"):
    import psycopg2
    PSQL_HOST = HOST
    PSQL_PORT = PORT
    PSQL_USER = USER
    PSQL_PASS = PASS
    PSQL_DB   = DBAS
    try:
        Conn = psycopg2.connect(dbname=DBAS, user=USER, password=PASS, host=HOST, port=PORT)
        Cur = Conn.cursor()
        try:
            Cur.execute(QRY)
            if (TdC == "2"):
                Result = Cur.fetchall()
                for Mascota in Result:
                    print(Mascota)
        except psycopg2.OperationalError as e:
            print("ERROR: Ha ocurrido un error al realizar sentencia : \n{0}").format(e)
        Cur.close()
        Conn.close()
    except psycopg2.Error as e:
        print("ERROR: Ha ocurrido un error al conectarse : ", e)
elif (MBD == "5"):
    import pymongo
    MONGODB_HOST = HOST
    MONGODB_PORT = PORT
    MONGODB_TIMEOUT = 1000
    URI_CONNECTION = "mongodb://" + MONGODB_HOST + ":" + MONGODB_PORT +  "/"
    Conn = MongoClient(MONGODB_HOST, MONGODB_PORT)
    db = Conn.dabasename
    Collection = db.collection_name
    try:
        Client = pymongo.MongoClient(URI_CONNECTION, serverSelectionTimeoutMS=MONGODB_TIMEOUT)
        if (TdC == "2"):
            Cursor = Collection.find() 
            for Record in Cursor: 
                print(Record)
        elif (TdC == "1"):
            Rec = Collection.insert_one(QRY)
#            Rec = db.Collection.insert_one(QRY)
        elif (TdC == "3"):
             Result = collection.update_many(QRY)
             print ("Datos actualizados : ", Result)
        else:
             Result = db.DBAS.remove(QRY)
             print ("Registros Eliminados : ", Result)
        Client.server_info()
        print ("OK -- Connectado a MongoDB en el servidor %s" % (MONGODB_HOST))
        Client.close()
    except pymongo.errors.ServerSelectionTimeoutError as error:
         print ("ERROR: Con la conexión MongoDB : %s" % error)
    except pymongo.errors.ConnectionFailure as error:
         print ("ERROR: No se pudo conectar a MongoDB : %s" % error)
elif (MBD == "6"):
    import mysql.connector as mariadb
    MariaDB_Cnx = mariadb.connect(host=HOST, port=PORT, user=USER, password=PASS, database=DBAS)
    Cursor = MariaDB_Cnx.cursor()
    try:
        Cursor.execute(QRY)
        for Row in Cursor:
            print (Row)
    except mariadb.Error as error:
        print ("ERROR: No se pudo conectar a MongoDB :".format(error))
    MariaDB_Cnx.close()
elif (MBD == "7"):
    import ibm_db
    ################################################
    # Conexión con una base de datos no catalogada #
    ################################################
    # ibm_db.connect("DATABASE=DBAS; HOSTNAME=HOST; PORT=PORT; PROTOCOL=TCPIP; UID=USER; PWD=PASS;", "", "")
    # Conn = ibm_db.connect(DBAS, USER, PASS)

    #####################################################
    # Conexión con una base de datos local o catalogada #
    #####################################################
    try:
        Conn = ibm_db.connect(DBAS, USER, PASS)
        Sql = QRY
        Stmt = ibm_db.exec_immediate(Conn, Sql)
        if Conn:
            if (TdC != "2"):
                print ("Número de filas afectadas : ", ibm_db.num_rows(Stmt))
            else:
                Result = ibm_db.fetch_both(Stmt)
                while (Result):
                    print (Result)
                    Result = ibm_db.fetch_both(Stmt)
    except:     
        print ("ERROR: No se pudo realizar la conecxión :", ibm_db.conn_errormsg())
    else:
        print ("AVISO: La conexión se realizó de manera existosa.....")
else:
    print ("ERROR: Se requieren los siguientes argumentos")
    print ("Parámetro 1 : Motor de base de Datos")
    print ("            1 = Oracle")
    print ("            2 = MsSql Server")
    print ("            3 = MySql")
    print ("            4 = PostgreSQL")
    print ("            5 = MongoDB")
    print ("            6 = MariaDB")
    print ("            7 = DB2")
sys.exit()
