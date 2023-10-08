import tkinter as tk

def mostrar_mensaje():
    mensaje_label.config(text="¡Hola, mundo!")

ventana = tk.Tk()
ventana.title("Mi Aplicación Tkinter")
ventana.geometry("800x600+0+0")  # Establece las dimensiones y la posición

mensaje_label = tk.Label(ventana, text="", font=("Arial", 16))
mensaje_label.pack(pady=20)

boton = tk.Button(ventana, text="Mostrar Mensaje", command=mostrar_mensaje)
boton.pack()

ventana.mainloop()
