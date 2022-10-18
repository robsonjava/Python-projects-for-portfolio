# Página de download do XAMPP
# https://www.apachefriends.org/pt_br/index.html

# Comando PIP para instalar o driver de conexão
# python -m pip install mysql-connector-python

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost", 
    user="root", 
    password=""
)

print(mydb)