import mysql.connector

mydb = mysql.connector.connect(
    host="localhost", 
    user="root", 
    password="",
    database="mydatabase"
)

mycursor = mydb.cursor()

# ADICIONAR COLUNAS NA TABELA (NO FINAL)
#sql = """ALTER TABLE pessoas ADD sobrenome VARCHAR(255)"""

# EXCLUIR COLUNAS NA TABELA
#sql = """ALTER TABLE pessoas DROP sobrenome"""

# ADICIONAR COLUNAS NA TABELA (NO INICIO)
#sql = """ALTER TABLE pessoas ADD sobrenome VARCHAR(255) FIRST"""

# ADICIONAR COLUNAS NA TABELA E POSICIONAR (NO LUGAR DESEJADO)
sql = """ALTER TABLE pessoas ADD sobrenome VARCHAR(255) AFTER nome"""

mycursor.execute(sql)