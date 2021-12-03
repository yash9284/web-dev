#!/usr/bin/python3
import cgi
import mysql.connector

print("Content-type: text/html")
print()

form=cgi.FieldStorage()
id=form.getvalue("userid")
ps=form.getvalue("pswd")

con=mysql.connector.connect(host='localhost',user='root',password='YASH99@ss',database='cars')
curs=con.cursor()

curs.execute("select * from users where userid='%s' and password='%s';" %(id,ps))
rec=curs.fetchone()


if rec:
    #print("<h2 style='color:green'>welcome to python on the server</h2>")
    print("<html>")
    print("<head>")
    print("<meta http-equiv='refresh' content='0;url=control.html'/>")
    print("</head>")
    print("</html>")
else:
    print("<h2 style='color:red'>sorry authentication failed</h2>")
    print("<br><a href='index.html'>Home</a>")

con.close()