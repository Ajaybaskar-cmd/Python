import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",password="1910",database="ajay")
if con:
    print("connect")
else:
    print("not connect")
    
res=con.cursor()
qry="select *from student"
res.execute(qry)
result=res.fetchall()

for x in result:
    print(x)