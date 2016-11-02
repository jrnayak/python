#!/usr/bin/python
import json
import mysql.connector
from mysql.connector import errorcode
db = mysql.connector.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     password="root",  # your password
                     database="dimensions")        # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor()

# Use all the SQL you like
cur.execute("SELECT * FROM dim_email")

#Open a file for each record
#f = open('pytest.txt', 'w')
for row in cur.fetchall():
    d = {
        'id': row[0],
        'email': row[1]
    }
    f = open("file_"+`row[0]`+".json","w")
    f.write(json.dumps(d))
    f.close 
db.close()
