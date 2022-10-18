import mysql.connector

mydb = mysql.connector.connect(
    host="localhost", 
    user="root", 
    password="",
    database="mydatabase"
)

mycursor = mydb.cursor()

# INSERIR DADOS NA TABELA
#sql = "INSERT INTO pessoas (id, nome, sobrenome, idade) VALUES (NULL, 'Robson', 'Bento', 30)"

# INSERIR COM TUPLA
sql = "INSERT INTO pessoas (id, nome, sobrenome, idade) VALUES (NULL, %s, %s, %s)"

#val = ("Danny", "Logan", "35")
#mycursor.execute(sql, val)

# INSERIR COM LISTA
val =   [("Danny", "Lima", "35"),
        ("Alexandra", "Amorin", "35"),
        ("Alexandre", "Amorin", "55"),
        ("Ilma", "Bento", "59"),
        ("Deolino", "Francisco", "70"),
]

mycursor.executemany(sql, val)

mydb.commit()
print(mycursor.rowcount, "Registros inseridos!")
print(mycursor.lastrowid)