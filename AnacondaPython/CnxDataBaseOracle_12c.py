#!/usr/bin/env python
# -*- coding: ISO-8859-1 -*-
#########################################################################
# Script                : CnxDataBaseOracle_12c.py                      #
# Author                : Ulises Cáceres Rui-Perez   UCAIsia S. A.      #
# Propiedad Intelectual : Inversiones UCAIsia S. A.                     #
# Derechos  de Uso      : Inversiones UCAIsia S. A.                     #
# Fecha                 : 09.10.2019 a las 15:25 Hrs.                   #
# Objetetivo            : Proceso que abre una conexion con la base de  #
#                         datos.                                        #
# Versión               : 1.0.0.0                                       #
#########################################################################

import cx_Oracle

Dsn_Tns = cx_Oracle.makedsn('192.168.118.1', '1521', service_name='UCRP.ucaisia.cl')
Conn = cx_Oracle.connect(user=r'System', password='ULadelMaestro', dsn=Dsn_Tns)

c = Conn.cursor()
c.execute('Select * From COFISA.MD_ADDITIONAL_PROPERTIES')

for Row in c:
    print (Row[0], '-', Row[1], '-', Row[3], '-', Row[4], '-', Row[5], '-', Row[6], '-', Row[7], '-', Row[8], '-', Row[9], '-', Row[10], '-', Row[11])

Conn.close()