import mysql.connector

mydb = mysql.connector.connect(host='b9llcrzvoxm6pbhe5xxn-mysql.services.clever-cloud.com',
                             database='b9llcrzvoxm6pbhe5xxn',
                             user='uijhoo8snd9qskzr',
                             password='svU4GQlGrl0KVHDf7cLQ')

mycursor = mydb.cursor()

sql = "INSERT INTO Laptop (Id, Name, Price, Purchase_date) VALUES (%s, %s, %s, %s)"
val = ("1", "Highway 21", "0.32", "as")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")