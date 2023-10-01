import sqlite3


conn = sqlite3.connect("Blog.db")
cursor = conn.cursor()

# Создание таблиц
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Posts (
        id INTEGER NOT NULL PRIMARY KEY,
        Category TEXT,
        User_id INTEGER,
        Text TEXT
    );
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Categories (
        id INTEGER NOT NULL PRIMARY KEY,
        Name TEXT
    );
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Users (
        id INTEGER NOT NULL PRIMARY KEY,
        Full_name TEXT,
        Date_of_birth DATE,
        Role TEXT,
        Date_of_registration DATE
    );
""")

#  Вставка в таблицу Users
cursor.executemany("INSERT INTO Users (id, Full_name, Date_of_birth, Role, Date_of_registration) VALUES (?, ?, ?, ?, ?)",
                   [(1, 'Иван Иванов', '1990-01-15', 'автор', '2023-09-28'),
                    (2, 'Мария Петрова', '1985-05-20', 'читатель', '2023-09-28'),
                    (3, 'Алексей Сидоров', '1982-11-10', 'админ', '2023-09-28'),
                    (4, 'Елена Козлова', '1995-03-03', 'читатель', '2023-09-28'),
                    (5, 'Петр Новиков', '1978-07-25', 'автор', '2023-09-28')])


#  Вставка в таблицу Categories
cursor.executemany("INSERT INTO Categories (id, Name) VALUES (?, ?)",
                   [(1, 'Политика'), (2, 'Наука'), (3, 'Искусство'), (4, 'Технологии'), (5, 'Спорт')])


#  Вставка в таблицу Posts
cursor.executemany("INSERT INTO Posts (id, Category, User_id, Text) VALUES (?, ?, ?, ?)",
                   [(1, 'Политика', 1, 'Сегодня обсудим последние политические новости.'),
                    (2, 'Наука', 2, 'Новое открытие в физике.'),
                    (3, 'Искусство', 5, 'Рецензия на новый фильм.'),
                    (4, 'Технологии', 3, 'Обзор последних гаджетов.'),
                    (5, 'Спорт', 4, 'Спортивные новости и обзор матча.')])


conn.commit()
conn.close()


