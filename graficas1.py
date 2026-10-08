import tkinter as tk

def cambiar_texto():
    etiqueta.config(text="¡Hola! Has hecho clic 👋")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Mi primera ventana gráfica")
ventana.geometry("400x250")

# Crear elementos
etiqueta = tk.Label(ventana, text="Presiona el botón", font=("Arial", 14))
etiqueta.pack(pady=20)

boton = tk.Button(ventana, text="Haz clic aquí", command=cambiar_texto)
boton.pack(pady=10)

# Iniciar el bucle de la ventana
ventana.mainloop()