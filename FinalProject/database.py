import sqlite3


conn = sqlite3.connect("Jokes.db")
cursor = conn.cursor()


cursor.execute("""
    CREATE TABLE IF NOT EXISTS Jokes (
        id INTEGER PRIMARY KEY,
        joke TEXT
    );
""")


jokes_data = [
    "Как программист встречает Новый год? 01011000 01001001 01011000",
    "Зачем программистам жить до ста лет? Чтобы умереть по-собственному желанию.",
    "Если вы не можете объяснить это шестилетнему ребенку, значит, ваш код плох.",
    "Какие программисты самые лучшие? Те, кто учится на своих ошибках. А какие худшие? Те, кто учится на ошибках других.",
    "Если бы бог был программистом, мир был бы создан за 7 дней и еще бы 3 дня было бы исправление ошибок."
]

cursor.executemany("INSERT INTO Jokes (joke) VALUES (?)", [(joke,) for joke in jokes_data])


conn.commit()
conn.close()