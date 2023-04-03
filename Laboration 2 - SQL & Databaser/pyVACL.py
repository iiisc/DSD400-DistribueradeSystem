#import sqlite3
import pymysql.cursors


con = pymysql.connect(
    user="pyVACL",
    password="lurigtpassword",
    host="dsd400.port0.org",
    port=3306,
    database="VA_CL"
    )

cur = con.cursor()
cur.execute("SELECT * FROM Spelare where SpelarID = 1 OR Namn = 'Viktor'")
res = cur.fetchall()
for row in res:
    print(row)


cur.execute("SELECT Namn FROM Spelare INNER JOIN _Match ON Vinnare = SpelarID WHERE Spel = 'Schack'")
for row in cur.fetchall():
    for item in row:
        print("Vinnare i schack:", item)

indata = input("VAD VILL DU GÖRA:")

sqlstatement = "SELECT Namn FROM Spelare INNER JOIN _Match ON Vinnare = SpelarID WHERE Spel = %s"
cur.execute(sqlstatement, ('schack'))
print("HÄR:",cur.fetchall())


#FARLIGT STATEMENT - Känsligt för SQL-injection
sql="SELECT Namn FROM Spelare INNER JOIN _Match ON Vinnare = SpelarID WHERE Spel = '"+indata+"'"
cur.execute(sql)
print(cur.fetchall())
