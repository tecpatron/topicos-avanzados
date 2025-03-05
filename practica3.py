import tkinter as tk
from tkinter import messagebox

def validar():
    nombre = entrada_nombre.get().strip()
    correo = entrada_correo.get().strip()
    edad = entrada_edad.get().strip()

    if not nombre:
        messagebox.showerror("Error", "Este campo no puede estar vacio")
        return
    if "@" not in correo or "." not in correo:
        messagebox.showerror("Error", "Correo no válido")
        return
    if not edad.isdigit():
        messagebox.showerror("Error", "No es un número")
        return

    escolaridad = escolaridad_var.get()
    messagebox.showinfo("Lo siguientes datos han sido capturados:",
    f"Se ha capturado los siguiente datos:\nNombre: {nombre}\nCorreo: {correo}\nEdad: {edad}\nEscolaridad: {escolaridad}")


def limpiar():
    entrada_nombre.delete(0, tk.END)
    entrada_correo.delete(0, tk.END)
    entrada_edad.delete(0, tk.END)
    escolaridad_var.set("Seleccione")


ventana = tk.Tk()
ventana.title("Formulario con Validaciones")
ventana.geometry("350x300")
ventana.configure(bg="darkorange")

tk.Label(ventana, text="Nombre:", bg="darkorange").pack(pady=2)
entrada_nombre = tk.Entry(ventana)
entrada_nombre.pack(pady=2)

tk.Label(ventana, text="Correo:", bg="darkorange").pack(pady=2)
entrada_correo = tk.Entry(ventana)
entrada_correo.pack(pady=2)

tk.Label(ventana, text="Edad:", bg="darkorange").pack(pady=2)
entrada_edad = tk.Entry(ventana)
entrada_edad.pack(pady=2)

tk.Label(ventana, text="Escolaridad:", bg="darkorange").pack(pady=2)
escolaridad_var = tk.StringVar(ventana)
escolaridad_var.set("Seleccione")
escolaridad_menu = tk.OptionMenu(ventana, escolaridad_var, "Primaria", "Secundaria", "Preparatoria", "Universidad")
escolaridad_menu.pack(pady=2)

tk.Button(ventana, text="Enviar", command=validar).pack(pady=5)
tk.Button(ventana, text="Limpiar", command=limpiar).pack(pady=5)

ventana.mainloop()
