#!/usr/bin/python3
import cgi
import mysql.connector

print("Content-type: text/html")
print()

request=cgi.FieldStorage()
com=request.getvalue("comp")
typ=request.getvalue("ctyp")
nm=request.getvalue("cname")
cap=request.getvalue("Ecap")
pr=int(request.getvalue("price"))



con=mysql.connector.connect(host='localhost',user='root',password='YASH99@ss',database='cars')
curs=con.cursor()

try:
    curs.execute("insert into car values('%s','%s','%s','%s',%d);" %(com,typ,nm,cap,pr))
    
    print("<h3>Car Registration Successful</h3>")
except:
    print("<h3>Registration failed...</h3>")

con.close()
print("<br><br><a href='index.html'>Home</a>")
