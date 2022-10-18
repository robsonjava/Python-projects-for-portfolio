import mysql.connector

mydb = mysql.connector.connect(
    host="localhost", 
    user="root", 
    password="",
    database="mydatabase"
)

mycursor = mydb.cursor()
sql = """
SELECT 
    usuarios.nome AS nome, produtos.nome AS favorito
    FROM usuarios
    INNER JOIN produtos ON usuarios.fav = produtos.id
"""
# USAR O (LEFT) NO LUGAR DO INNER, MOSTRA TODOS USUARIOS DA TABELA
# USAR O (RIGHT) NO LUGAR DO INNER, MOSTRA TODOS PRODUTOS DA TABELA
mycursor.execute(sql)
myresult = mycursor.fetchall()

for x in myresult:
    print(x)