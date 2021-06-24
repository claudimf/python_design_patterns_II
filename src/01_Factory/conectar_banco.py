# -*- coding: utf-8 -*-
import mysql.connector
import os

# cria uma conexão com o banco
connection = mysql.connector.connect(
    host=os.getenv('MYSQL_HOST'),
    user=os.getenv('MYSQL_USER'),
    password=os.getenv('MYSQL_ROOT_PASSWORD'),
    db=os.getenv('MYSQL_DATABASE')
    )

cursor = connection.cursor()

# executa a query
cursor.execute('SELECT * from curso')

# itera sobre o resultado
for linha in cursor:
    print(linha)

# fecha a conexão
connection.close()
