import MySQLdb

conn_db = MySQLdb.connect("localhost","root","root","connect_db")
cursor = conn_db.cursor()

sql_query = """"create table company (
company_name(char 20),
revenue (int 5))"""

# db_data = cursor.fetchone()

# print 'FL_insurance_sample (1).csv'

conn_db.close()
