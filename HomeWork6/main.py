import tkinter as tk
from game_utils import Config, Functionality

root = tk.Tk()
config = Config(root)
func = Functionality()


def update_label():
    func.increment()
    label.config(text=f"Количество нажатий: {func.counter}")


label = tk.Label(root, text=f"Количество нажатий: {func.counter}")
label.pack(pady=10)


button = tk.Button(root, text="Нажми меня!", command=update_label)
button.pack()


if __name__ == "__main__":
    root.mainloop()
