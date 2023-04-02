import sqlite3

myConnection = sqlite3.connect("testdb.db") #Steg 1. Connecta/skapa en .db fil

myCursor = myConnection.cursor() #Steg 2. Skapa en cursor, delen som skickar statements

#resultat = myCursor.execute("SELECT * FROM sqlite_master") #Gör en query mot databasen
#if resultat.fetchone() is None: #Om resultat inte får något svar körs if-satsen

myCursor.execute("CREATE TABLE IF NOT EXISTS spelare(Namn, Ålder, Rank)")

data = [("Carl", 32, 1),("Anders", 40, 2), ("Malin", 33, 5)]
data1 = [("Ett", "One", 1), ("Två", "Two", 2), ("Tre", "Three", 3)]

myCursor.executemany("INSERT INTO spelare VALUES(?,?,?)", data)

print("PRINT 1: ", myCursor.execute("SELECT * FROM spelare").fetchall())

for row in myCursor.execute("SELECT * from spelare"):
    print("PRINT 2: ", row)
    for item in row:
        print("PRINT 3: ", item)

myCursor.execute("DROP TABLE spelare")
myConnection.commit() #Skriver allt man gjort till db
myConnection.close() #Stänger connection till db