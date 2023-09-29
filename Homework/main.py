import sqlite3

conn = sqlite3.connect("MyContacts.db")

cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS Contacts(
            Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            Name TEXT,
            Phone NUMBER TEXT,
            Email TEXT);""")

insert_data = [
    ("John Doe", "+123456789", "john.doe@gmail.com"),
    ("Jane Smith", "+145678901", "jane.smith@hotmail.com"),
    ("Bob Johnson", "+178945612", "bob.johnson@gmail.com"),
    ("Alice Brown", "+188888888", "alice.brown@yahoo.com"),
    ("Eve Wilson", "+199999999", "eve.wilson@gmail.com"),
]

cur.executemany("INSERT INTO Contacts (Name, Phone, Email) VALUES (?, ?, ?)", insert_data)

conn.commit()
conn.close()