import mysql.connector

def conect():
    database = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "",
        database = "gmc_cm",
    )
    cursor = database.cursor(buffered = True)
    return [database, cursor]
