#! /usr/bin/python2.7

import mysql.connector
import time
stime = time.strftime('%Y-%m-%d %H:%M:%S')


mydb = mysql.connector.connect(
  host="localhost",
  user="pi",
  passwd="raspberry",
  database="temper"
)

mycursor = mydb.cursor()

#mycursor.execute("CREATE DATABASE mydatabase")
#mycursor.execute("SHOW DATABASES")
#for x in mycursor:
#  print(x)
#sql = "SELECT * FROM \'temper\'"
#print (sql)
#print(mycursor.execute(sql))



mycursor.execute("SELECT * FROM temper")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)



sql = "INSERT INTO temper (temp,location) VALUES (%s,%s);"
val = (22.5,'xxx')
mycursor.execute(sql,val)
mydb.commit()

print(sql)
