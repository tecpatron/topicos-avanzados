import tkinter as tk
from tkinter import messagebox

class P4Editor:
    def __init__(self, root):
        self.root = root
        self.root.title("Editor de Texto Simple 0.1")
        self.root.geometry("700x500")

    # Área de texto
        self.text_area = tk.Text(self.root, font=("Comic Sans MS", 15))
        self.text_area.pack(expand=True, fill="both")

    # Parte del menú
        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)

    # Menú Archivo
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Open", accelerator="Ctrl+O", command=self.no_action)
        self.file_menu.add_command(label="Save", accelerator="Ctrl+S", command=self.no_action)
        self.file_menu.add_command(label="Delete", accelerator="Ctrl+D", command=self.no_action)
        self.file_menu.add_command(label="Exit", accelerator="Ctrl+Q", command=self.root.quit)

    # Menú Editar
        self.edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Edit", menu=self.edit_menu)
        self.edit_menu.add_command(label="Change text color", accelerator="Ctrl+T", command=self.no_action)
        self.edit_menu.add_command(label="Find and replace", accelerator="Ctrl+F", command=self.no_action)

    # Estos son los atajos
        self.root.bind("<Control-o>", lambda event: self.no_action())
        self.root.bind("<Control-s>", lambda event: self.no_action())
        self.root.bind("<Control-d>", lambda event: self.no_action())
        self.root.bind("<Control-t>", lambda event: self.no_action())
        self.root.bind("<Control-f>", lambda event: self.no_action())
        self.root.bind("<Control-q>", lambda event: self.root.quit())

    # Esta es la dichosa función para avisar que no están disponibles
    def no_action(self):
        messagebox.showinfo("Regla de la Práctica 4", "No disponible")

if __name__ == "__main__":
    root = tk.Tk()
    app = P4Editor(root)
    root.mainloop()