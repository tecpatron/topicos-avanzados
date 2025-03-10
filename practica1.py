import tkinter as tk
from tkinter import messagebox

app = tk.Tk()
app.title("Práctica 1")
app.geometry("600x300")
app.configure(bg="darkorange")

def mostrar_mensaje():
    texto = entrada.get()
    messagebox.showinfo("Aquí se muestra el mensaje", f"Has escrito: {texto}")

titulo = tk.Label(app, text="¡Hola, humano!", font=("Arial", 14), bg="darkorange", fg="white")
titulo.pack(pady=20)

entrada = tk.Entry(app, font=("Arial", 12), width=30)
entrada.pack(pady=10)

boton_mostrar = tk.Button(app, text="Mostrar Mensaje", font=("Arial", 12), command=mostrar_mensaje, bg="white", fg="black")
boton_mostrar.pack(pady=5)

boton_salir = tk.Button(app, text="Salir", font=("Arial", 12), command=app.quit, bg="white", fg="black")
boton_salir.pack(pady=5)

app.mainloop()
