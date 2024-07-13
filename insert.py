import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",password="1910",database="ajay")
if con:
    print("connect")

res=con.cursor()
qry="INSERT INTO student(name,city) VALUES(%s,%s)"
val=("ganesh","simizhi")
res.execute(qry,val)
con.commit()
