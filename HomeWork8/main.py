import tkinter as tk
import sqlite3
import random


class JokeApp:
    def __init__(self, root):
        self.root = root 
        
        #взаимодействие с БД
        
        self.root.title("Генератор анекдотов")

        self.conn = sqlite3.connect("Jokes.db")
        self.cursor = self.conn.cursor()

        # разрешение окна
        self.root.geometry("400x300")

        # Добавляем изображение на кнопку
        self.image = tk.PhotoImage(file="img\\refresh.png")
        self.button_generate = tk.Button(
            self.root, image=self.image, command=self.generate_joke
        )
        self.button_generate.pack(pady=10)

        self.text_joke = tk.Text(self.root, width=40, height=10)
        self.text_joke.pack()

    #  метод генерации шутки
    def generate_joke(self):
        self.text_joke.delete(1.0, tk.END)  # Очистить текстовое поле

        self.cursor.execute("SELECT joke FROM Jokes ORDER BY RANDOM() LIMIT 1;")
        joke = self.cursor.fetchone()
        if joke:
            joke_text = joke[0]
            self.text_joke.insert(tk.END, joke_text)
        else:
            self.text_joke.insert(tk.END, "Анекдоты закончились!")


if __name__ == "__main__":
    root = tk.Tk()
    app = JokeApp(root)
    root.mainloop()
