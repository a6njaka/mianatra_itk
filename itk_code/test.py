import sqlite3

conn = sqlite3.connect('test.db')
print("Opened database successfully")

conn.execute('''CREATE TABLE "vola_miditra_mivoaka" (
	"ID"	INTEGER NOT NULL UNIQUE,
	"Daty"	TEXT NOT NULL DEFAULT CURRENT_DATE,
	"Antony"	TEXT,
	"Miditra"	INTEGER,
	"Mivoaka"	INTEGER,
	"Fanazavana"	INTEGER,
	PRIMARY KEY("ID" AUTOINCREMENT)
)''')
print("Table created successfully")

conn.close()
