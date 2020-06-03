#coding = utf-16
#########################################################################
# Script                : app.py                                        #
# Author                : Ulises Cáceres Rui-Perez   UCAIsia S. A.      #
# Propiedad Intelectual : Inversiones UCAIsia S. A.                     #
# Derechos  de Uso      : Inversiones UCAIsia S. A.                     #
# Fecha                 : 09.10.2019 a las 15:25 Hrs.                   #
# Objetetivo            : Proceso POST para insertar usuario en MySql.  #
# Versi¦n               : 1.0.0.0                                       #
#########################################################################

from flask import Flask, render_template, json, request
from flaskext.mysql import MySQL
from werkzeug import generate_password_hash, check_password_hash
import os, sys, io

USER = sys.argv[1]
PASS = sys.argv[2]
DBAS = sys.argv[3]
HOST = sys.argv[4]

app = Flask(__name__)
mysql = MySQL()

app.config['MYSQL_DATABASE_USER'] = USER
app.config['MYSQL_DATABASE_PASSWORD'] = PASS
app.config['MYSQL_DATABASE_DB'] = DBAS
app.config['MYSQL_DATABASE_HOST'] = HOST
mysql.init_app(app)

Conn = mysql.connect()
Cursor = Conn.cursor()

@app.route('/')
def main():
    return render_template('Index.html')

@app.route('/SignUp', methods=['GET', 'POST'])
def SignUp():
    if request.method == 'POST':
        try:
            ############################################################
            # Leer los valores publicados desde la interfaz de usuario #
            ############################################################
            _name = request.form['inputName']
            _email = request.form['inputEmail']
            _password = request.form['inputPassword']
            ################################
            # validate the received values #
            ################################
            if _name and _email and _password:
                _hashed_password = generate_password_hash(_password)
                Cursor.callproc('Prc_CreateUser',(_name,_email,_hashed_password))
                data = cursor.fetchall()
                if len(data) is 0:
                    Conn.commit()
               return json.dumps({'AVISO :':'Usuario creado con éxito !'})
                else:
                    return json.dumps({'ERROR :':str(data[0])})
            else:
                return json.dumps({'html':'<span>Ingrese los campos requeridos</span>'})
            return render_template('SignUp.html')
        except Exception as e:
            return json.dumps({'ERROR :':str(e)})
        finally:
            Cursor.close() 
            Conn.close()

@app.route('/ShowRegistrate', methods=['GET', 'POST'])
def ShowRegistrate():
    if request.method == 'POST':
        ############################################################
        # Leer los valores publicados desde la interfaz de usuario #
        ############################################################
        _name = request.form['inputName']
        _email = request.form['inputEmail']
        _password = request.form['inputPassword']

        ################################
        # validate the received values #
        ################################
        if _name and _email and _password:
            _hashed_password = generate_password_hash(_password)
            Cursor.callproc('Prc_CcreateUser',(_name, _email, _hashed_password))
            Data = Cursor.fetchall()
            if len(Data) is 0:
               Conn.commit()
               return json.dumps({'AVISO:':'Usuario creado con éxito !'})
            else:
               return json.dumps({'ERROR:':str(Data[0])})
        else:
            return json.dumps({'html':'<span>Ingrese los campos requeridos</span>'})
    return render_template('Registrate.html')

if __name__ == "__main__":
    app.debug=True
    app.run(port=5002)
