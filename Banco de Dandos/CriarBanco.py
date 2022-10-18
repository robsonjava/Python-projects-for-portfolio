import mysql.connector

# Criar a conexao
mydb = mysql.connector.connect(
    host="localhost", 
    user="root", 
    password=""
)
#---------------------------------------------------
# Criando o banco
mycursor = mydb.cursor()

#mycursor.execute("CREATE DATABASE mydatabase")

#----------------------------------------------------

# VISUALIZAR TODOS OS BANCOS QUE TEM NO SERVIDOR
mycursor.execute("SHOW DATABASES")

for x in mycursor:
    print(x)
#----------------------------------------------------

print("Fim do programa!")