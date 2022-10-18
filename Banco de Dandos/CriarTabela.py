# OBJETO DE CONEXÃO COM O BANCO DE DADOS
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost", 
    user="root", 
    password="",
    database="mydatabase"
)
# OBJETO (CURSOR) PARA MANIPULAR A BANCO DE DADOS
mycursor = mydb.cursor()

# CONSULTAS SQL (CRIANDO A TABELA)
#sql = """CREATE TABLE pessoas (nome VARCHAR(255), idade INT(2))"""

# OBJETO (EXECUTE) PARA COM O BANCO DE DADOS
#mycursor.execute(sql)

# VISUALIZAR TODAS AS TABELAS
#mycursor.execute("SHOW TABLES")
#for x in mycursor:
    #print(x)
