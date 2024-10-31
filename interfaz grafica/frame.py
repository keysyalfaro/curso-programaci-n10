import tkinter as tk
from tkinter import messagebox

def abrir_archivo():
    messagebox.showinfo("Abrir", "Función para abrir archivos")

def salir_app():
    root.quit()

root = tk.Tk()

# Crear el menú
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Crear una opción de menú
archivo_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Archivo", menu=archivo_menu)
archivo_menu.add_command(label="Abrir", command=abrir_archivo)
archivo_menu.add_separator()
archivo_menu.add_command(label="Salir", command=salir_app)

root.mainloop()