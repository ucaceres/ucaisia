#!/usr/bin/env python
# -*- coding: ISO-8859-1 -*-
#########################################################################
# Script                : CnxDataBaseMongoDb.py                         #
# Author                : Ulises Cáceres Rui-Perez   UCAIsia S. A.      #
# Propiedad Intelectual : Inversiones UCAIsia S. A.                     #
# Derechos  de Uso      : Inversiones UCAIsia S. A.                     #
# Fecha                 : 09.10.2019 a las 15:25 Hrs.                   #
# Objetetivo            : Proceso que abre una conexion con la base de  #
#                         datos.                                        #
# Versi¦n               : 1.0.0.0                                       #
#########################################################################

import pymongo

MONGODB_HOST = '192.168.0.169'
MONGODB_PORT = '27017'
MONGODB_TIMEOUT = 1000

URI_CONNECTION = "mongodb://" + MONGODB_HOST + ":" + MONGODB_PORT +  "/"

try:
    client = pymongo.MongoClient(URI_CONNECTION, serverSelectionTimeoutMS=MONGODB_TIMEOUT)
    client.server_info()
    print 'OK -- Connected to MongoDB at server %s' % (MONGODB_HOST)
    client.close()
except pymongo.errors.ServerSelectionTimeoutError as error:
    print 'Error with MongoDB connection: %s' % error
except pymongo.errors.ConnectionFailure as error:
    print 'Could not connect to MongoDB: %s' % error