import tkinter as tk
from tkinter import ttk

class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()
    
    def init_main(self):
        toolbar = tk.Frame(bg="#d7d8e0", bd=2)
        toolbar.pack(side=tk.TOP, fill=tk.X)
        
        self.add_img = tk.PhotoImage(file="image\\add.png")
        btn_open_dialog = tk.Button(toolbar, bg="#d7d8e0", bd=0, image=self.add_img, command=self.open_dialog)
        btn_open_dialog.pack(side=tk.LEFT)
        
        self.tree = ttk.Treeview(self, columns=("ID", "name", "tel", "email"), height=45, show="headings")
        self.tree.column("ID", width=30, anchor=tk.CENTER)
        self.tree.column("name", width=300, anchor=tk.CENTER)
        self.tree.column("tel", width=150, anchor=tk.CENTER)
        self.tree.column("email", width=150, anchor=tk.CENTER)
        
        self.tree.heading("ID", text="ID")
        self.tree.heading("name", text="ФИО")
        self.tree.heading("tel", text="Телефон")
        self.tree.heading("email", text="E-mail")
        
        self.tree.pack(side=tk.LEFT)
        
        #to do #####################################
             
    def init_child(self):
        # Загловок окна 
        self.title("Добавить")
        self.geometry("400x220")
        self.resizable(False, False)
        self.grab_set()
        self.focus_set()


    def open_dialog(self):
        Child()


class Child(tk.Toplevel, Main):
    def __init__(self):
        super().__init__(root)
        self.init_child()
        


if __name__ == "__main__":
    # создаем экран приложения
    root = tk.Tk()
    app = Main(root)
    app.pack()
            
    # Конфиг приложения
    root.title("Телефонная книга")
    root.resizable(False, False)
    root.geometry("1280x768+400+200")
    root.mainloop()
