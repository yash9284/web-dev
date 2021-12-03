#!/usr/bin/python3
import mysql.connector

print("Content-type: text/html")
print()
print("<link rel='stylesheet' href='bootstrap.min.css'>")
print("<div class='container'>")
con=mysql.connector.connect(host='localhost',user='root',password='YASH99@ss',database='spiderdb')
curs=con.cursor()

curs.execute("select custnm from customers")
nms=curs.fetchall()

print("<br><br><h2>Customer List</h2>")
print("<hr>")

#print(nms)

print("<ul>")


for cnm in nms:
    print("<li>%s" %cnm[0])

print("</ul>")
print("<br><a href='control.html'>Home</a>")
print("</div>")
con.close()