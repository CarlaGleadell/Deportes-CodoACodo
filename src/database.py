import mysql.connector

database = mysql.connector.connect(
    host='localhost',
    user = 'root',
    password = '123456789',
    database = 'equipos'
)

database.autocommit=True