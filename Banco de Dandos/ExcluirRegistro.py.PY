import mysql.connector

mydb = mysql.connector.connect(
    host="localhost", 
    user="root", 
    password="",
    database="mydatabase"
)

mycursor = mydb.cursor()

sql = "DELETE FROM pessoas WHERE id = %s"
val = ('13',)

mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "Registro(s) excluido(s)")