import tkinter as tk


class Config():
    def __init__(self, root):
        root.title("Игра-кликер")
        root.geometry("1280x768+400+200")
        photo = tk.PhotoImage(file="photo.png")
        root.iconphoto(False, photo)


class Functionality():
    def __init__(self):
        self.counter = 0
        
    def increment(self):
        self.counter+=1