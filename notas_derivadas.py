import tkinter as tk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

def graficar_notas_y_derivada(notas):
    if len(notas) < 4:
        messagebox.showwarning("Advertencia", "Debes ingresar al menos 4 notas.")
        return

    tiempo = np.arange(1, len(notas) + 1)
    tiempo_suave = np.linspace(tiempo.min(), tiempo.max(), 300)

    spline = make_interp_spline(tiempo, notas, k=3)
    notas_suave = spline(tiempo_suave)
    derivada = spline.derivative()(tiempo_suave)

    fig, ax1 = plt.subplots()
    ax1.plot(tiempo_suave, notas_suave, color='blue', label='Notas')
    ax1.set_xlabel('Número de prueba')
    ax1.set_ylabel('Nota', color='blue')
    ax1.tick_params(axis='y', labelcolor='blue')
    ax1.set_ylim(1, 7.5)

    ax2 = ax1.twinx()
    ax2.plot(tiempo_suave, derivada, color='red', linestyle='--', label='Derivada')
    ax2.set_ylabel('Velocidad de cambio', color='red')
    ax2.tick_params(axis='y', labelcolor='red')

    plt.title('Notas y Derivada (Velocidad de Cambio)')
    fig.tight_layout()
    plt.grid(True)
    plt.show()

def procesar_entrada():
    entrada = entry.get()
    try:
        notas = [float(n.strip()) for n in entrada.split(",") if n.strip()]
        graficar_notas_y_derivada(notas)
    except ValueError:
        messagebox.showerror("Error", "Ingresa solo números separados por comas.")

# Interfaz gráfica con tkinter
ventana = tk.Tk()
ventana.title("Notas y Derivada")
ventana.geometry("400x150")

label = tk.Label(ventana, text="Ingresa las notas separadas por coma:")
label.pack(pady=10)

entry = tk.Entry(ventana, width=50)
entry.pack()

boton = tk.Button(ventana, text="Graficar", command=procesar_entrada)
boton.pack(pady=10)

ventana.mainloop()
# notas_derivadas.py
# Este script permite ingresar notas, graficarlas junto con su derivada y mostrar la velocidad de cambio.
# Requiere las bibliotecas tkinter, numpy, matplotlib y scipy.  