import tkinter as tk
from tkinter import filedialog, messagebox, colorchooser
from practica5 import FileManager

class E2Editor:
    def __init__(self, root):
        self.root = root
        self.root.title("Editor de Texto Simple")
        self.root.geometry("700x500")
        self.file_manager = None

        # Área de texto
        self.text_area = tk.Text(self.root, font=("Comic Sans MS", 15))
        self.text_area.pack(expand=True, fill="both")

        # Parte del menú
        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)

        # Menú Archivo
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Open", accelerator="Ctrl+O", command=self.open_file)
        self.file_menu.add_command(label="Save", accelerator="Ctrl+S", command=self.save_file)
        self.file_menu.add_command(label="Delete", accelerator="Ctrl+D", command=self.clear_text)
        self.file_menu.add_command(label="Exit", accelerator="Ctrl+Q", command=self.root.quit)

        # Menú Editar
        self.edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Edit", menu=self.edit_menu)
        self.edit_menu.add_command(label="Change text color", accelerator="Ctrl+T", command=self.change_text_color)
        self.edit_menu.add_command(label="Find and replace", accelerator="Ctrl+F", command=self.find_and_replace)

        # Atajos de teclado
        self.root.bind("<Control-o>", lambda event: self.open_file())
        self.root.bind("<Control-s>", lambda event: self.save_file())
        self.root.bind("<Control-d>", lambda event: self.clear_text())
        self.root.bind("<Control-t>", lambda event: self.change_text_color())
        self.root.bind("<Control-f>", lambda event: self.find_and_replace())
        self.root.bind("<Control-q>", lambda event: self.root.quit())

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Archivo de texto", "*.txt")])
        if file_path:
            self.file_manager = FileManager(file_path)
            try:
                content = self.file_manager.open_file()
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, content)
            except FileNotFoundError:
                messagebox.showerror("Error", "No se pudo abrir el archivo")

    def save_file(self):
        if self.file_manager:
            try:
                content = self.text_area.get(1.0, tk.END)
                self.file_manager.save_file(content)
                messagebox.showinfo("Guardado", "Archivo guardado correctamente")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo guardar el archivo: {e}")
        else:
            file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Archivo de texto", "*.txt")])
            if file_path:
                self.file_manager = FileManager(file_path)
                self.save_file()

    def clear_text(self):
        if self.file_manager:
            try:
                self.file_manager.delete_file()
                self.text_area.delete(1.0, tk.END)
                messagebox.showinfo("Eliminado", "Se ha borrado todo")
            except FileNotFoundError:
                messagebox.showerror("Error", "No se encontró el archivo para eliminar")
        else:
            self.text_area.delete(1.0, tk.END)

    def change_text_color(self):
        color = colorchooser.askcolor(title="Selecciona un color")[1]
        if color:
            self.text_area.config(fg=str(color))

    def find_and_replace(self):
        def replace_text():
            find_text = find_entry.get()
            replace_text = replace_entry.get()
            content = self.text_area.get(1.0, tk.END)
            new_content = content.replace(find_text, replace_text)
            self.text_area.delete(1.0, tk.END)
            self.text_area.insert(1.0, new_content)

        find_window = tk.Toplevel(self.root)
        find_window.title("Find and Replace")
        find_window.geometry("300x150")

        tk.Label(find_window, text="Find:").pack()
        find_entry = tk.Entry(find_window)
        find_entry.pack()

        tk.Label(find_window, text="Replace with:").pack()
        replace_entry = tk.Entry(find_window)
        replace_entry.pack()

        tk.Button(find_window, text="Replace", command=replace_text).pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = E2Editor(root)
    root.mainloop()