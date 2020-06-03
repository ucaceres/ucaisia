#!/usr/bin/env python
# -*- coding: ISO-8859-1 -*-
#########################################################################
# Script                : Inserta_Docto_MongoDB.py                      #
# Author                : Ulises C�ceres Rui-Perez   UCAIsia S. A.      #
# Propiedad Intelectual : Inversiones UCAIsia S. A.                     #
# Derechos  de Uso      : Inversiones UCAIsia S. A.                     #
# Fecha                 : 09.10.2019 a las 15:25 Hrs.                   #
# Objetetivo            : Proceso de mantenci�n en la base de detos que #
#                         por medio de un par�metro, deerminar� la man- #
#                         tenci�n en la base de datos espec�fica.       #
# Versi�n               : 1.0.0.0                                       #
#########################################################################

import pymongo
import csv
import json
import pandas as pd
import sys, getopt, pprint
from pymongo import MongoClient

############################
# Conversi�n de CSV a JSON #
############################

csvfile = open('F://Proyectos//Sixbell//Tmp//Piloto Pentaho//SLA_Base.csv', 'r')
reader = csv.DictReader( csvfile )
mongo_client=MongoClient()

MONGODB_HOST = "127.0.0.1"
MONGODB_PORT = 27017
MONGODB_TIMEOUT = 1000

Conn = MongoClient(MONGODB_HOST, MONGODB_PORT)
db = Conn.dabasename
Collection = db.collection_name
try:
    db=mongo_client.october_mug_talk
    db.segment.drop()
    header= [ "ID", "CASO", "NUM_MES", "SLA", "PROPIETARIO", "SLA_ATENCION", "SLA_SOLUCION", "FECHA", "MES", "A�O", "TIPO", "ESTADO", "AREA", "SLA_UPDATE", "CALENDARIO", "C_SLA_ATENCION", "C_SLA_UPDATE", "C_SLA_SOLUCION", "C_SLA_ACTUAL", "PIVOTE", "C_ATENCION", "C_UPDATE", "C_SOLUCION", "UN_SERVICIO", "AREA_SERVICIO", "UN_ORIGEN", "AREA_ORIGEN", "AREA_AJUSTE", "Q", "M", "A-M", "TIPS_SERVICIO", "SOL"]

    for each in reader:
        row={}
        for field in header:
            row[field]=each[field]
        db.segment.insert(row)
    db.close()
except pymongo.errors.ServerSelectionTimeoutError as error:

    print ("ERROR: Con la conexi�n MongoDB : %s" % error)
except pymongo.errors.ConnectionFailure as error:

    print ("ERROR: No se pudo conectar a MongoDB : %s" % error)
