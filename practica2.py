import tkinter as tk

def on_mouse_click(event):
    label.config(text=f"Clic en ({event.x}, {event.y})")

def on_mouse_double_click(event):
    colors = ["red", "green", "blue"]
    current_color = root.cget("bg")
    new_color = colors[(colors.index(current_color) + 1) % len(colors)] if current_color in colors else colors[0]
    root.config(bg=new_color)
    label.config(text=f"Doble clic en ({event.x}, {event.y}) - Color cambiado a {new_color}")

def on_mouse_move(event):
    label.config(text=f"Movimiento en ({event.x}, {event.y})")

def on_key_press(event):
    if event.keysym == "space":
        label.config(text="")
    else:
        label.config(text=f"Tecla presionada: {event.keysym}")

root = tk.Tk()
root.title("Practica 2")
root.geometry("400x300")

label = tk.Label(root, text="Eventos capturados aparecerán aquí", font=("Arial", 12))
label.pack(pady=20)

root.bind("<Button-1>", on_mouse_click)
root.bind("<Double-Button-1>", on_mouse_double_click)
root.bind("<Motion>", on_mouse_move)

root.bind("<KeyPress>", on_key_press)

root.mainloop()