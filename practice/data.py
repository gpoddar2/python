import mysql.connector
try:
    mydb = mysql.connector.connect(host="localhost", username="root", passwd="23")
    print("connection successful")
except:
    print("connection unsucssful password wrong")    
"""
mycursor = mydb.cursor()
mycursor.execute("show databases")
for i in mycursor:
    print(i)
"""
