import mysql.connector

mydb = mysql.connector.connect(
    host="localhost", 
    user="root", 
    password="",
    database="mydatabase"
)

mycursor = mydb.cursor()
# LIMITANDO O RESULTADO
#sql = "SELECT * FROM pessoas LIMIT 5"
# Ordem crescente
sql = "SELECT * FROM pessoas ORDER BY idade"
# Ordem crescente
#sql = "SELECT * FROM pessoas ORDER BY idade DESC"
mycursor.execute(sql)
myresult = mycursor.fetchall()

for x in myresult:
    print(x)