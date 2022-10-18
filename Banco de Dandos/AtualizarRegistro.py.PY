import mysql.connector

mydb = mysql.connector.connect(
    host="localhost", 
    user="root", 
    password="",
    database="mydatabase"
)

mycursor = mydb.cursor()
#sql = "UPDATE pessoas SET nome = 'Robson' WHERE id = '1'"
sql = "UPDATE pessoas SET nome = %s WHERE id = %s"
val = ('Robson', '1')
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "Registro(s) afetado(s)")