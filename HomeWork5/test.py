import sqlite3

conn = sqlite3.connect("Blog.db")
cursor = conn.cursor()


cursor.execute("SELECT * FROM Users")
users = cursor.fetchall()
for user in users:
    print(user)
print()


cursor.execute("SELECT * FROM Categories")
categories = cursor.fetchall()
for category in categories:
    print(category)
print()


cursor.execute("SELECT * FROM Posts")
posts = cursor.fetchall()
for post in posts:
    print(post)


conn.close()