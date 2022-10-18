import mysql.connector

mydb = mysql.connector.connect(
    host="localhost", 
    user="root", 
    password="",
    database="mydatabase"
)

mycursor = mydb.cursor()
#sql = "DELETE FROM `pessoas` WHERE `pessoas`.`id` = 3"

# SELECIONAR TODOS REGISTROS DA TABELA
#sql = "SELECT * FROM pessoas"

sql = "SELECT nome, idade FROM pessoas"


mycursor.execute(sql)


# O METODO FETCHALL RETORNA TODOS RESULTADOS
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

# O METODO FETHONE RETORNA UM RESULTADO
#myresult = mycursor.fetchone()
#print(myresult)