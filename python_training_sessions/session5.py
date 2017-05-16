import MySQLdb

conn_db = MySQLdb.connect("localhost","root","root","connect_db")
cursor.execute("select version")

db_data = cursor.fetchone()

print db_data
conn_db.close()