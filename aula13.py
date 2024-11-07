import mysql.connector # type: ignore

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "escola"
)
cursor = conn.cursor()