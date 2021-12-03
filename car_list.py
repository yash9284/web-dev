#!/usr/bin/python3
import mysql.connector

print("Content-type: text/html")
print()
print("<link rel='stylesheet' href='bootstrap.min.css'>")
print("<body style='background-image:url(back5.jpg);background-size:cover'>")
print("<div class='container' >")
con=mysql.connector.connect(host='localhost',user='root',password='YASH99@ss',database='cars')
curs=con.cursor()

curs.execute("select car_name from car")
nms=curs.fetchall()

print("<br><br><h2 style='color:white'>Car List</h2>")
print("<hr>")

#print(nms)

print("<ul>")


for cnm in nms:
    print("<li style='color:green'>%s" %cnm)

print("</ul>")
print("<br><a href='control.html' style='color:red'>Home</a>")
print("</div>")
print("<br>")
print("</body)")
con.close()