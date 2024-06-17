# Este script genera la base de datos y prueba la conexión
# Install MySQL on your computer
# httsp://dev.mysql.com/dowmnloads/installer
# pip install mysql
# pip install mysql-connector
# pip install mysql-connector-python

import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '',
)

# Prepare a cursor object
cursorObject = dataBase.cursor()

# Create a database
cursorObject.execute("CREATE DATABASE elderco")

print("Todo bien")