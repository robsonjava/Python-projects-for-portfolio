import mysql.connector

mydb = mysql.connector.connect(
    host="localhost", 
    user="root", 
    password="",
    database="mydatabase"
)

mycursor = mydb.cursor()


#sql = """CREATE TABLE pessoas(id INT AUTO_INCREMENT PRIMARY KEY nome VARCHAR(255), idade INT(2)"""

# adicionar a chave primaria (id INT AUTO_INCREMENT PRIMARY KEY)
sql = "ALTER TABLE pessoas ADD id INT AUTO_INCREMENT PRIMARY KEY FIRST"

mycursor.execute(sql)