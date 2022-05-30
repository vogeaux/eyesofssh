# coding: utf-8
import mysql.connector

conn = mysql.connector.connect(host="sip.vogeaux.fr",user="root",password="password", database="data")
cursor = conn.cursor()
cursor.execute("""
SHOW DATABASES;
""")
conn.close()