import subprocess
import sys
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

from operaciones import calculadora, clima, datos, edades, imc, promedio, salario, serviciosPublicos, temperatura, descuentos, combustible, login

window = tk.Tk()
window.withdraw()  

def login_exitoso():
    window.deiconify()

login.iniciar_login(window, login_exitoso)

menu_bar = Menu(window)
window.config(menu=menu_bar)
window.title("CALCULADORA UNIEMPRESARIAL - Menú Principal")
window.geometry("500x500")

img_original = Image.open("img/logo_uni.png")
img_redimensionada = img_original.resize((100, 100), Image.Resampling.LANCZOS)
img = ImageTk.PhotoImage(img_redimensionada)
lbl_img = tk.Label(window, image=img)
lbl_img.image = img  
lbl_img.pack(pady=10)

ventana_actual = None

def abrir_ventana(archivo):
    global ventana_actual
    if ventana_actual is not None and ventana_actual.winfo_exists():
        ventana_actual.destroy()
    window.withdraw()  
    ventana_actual = archivo.abrir(window, volver_al_menu)

def volver_al_menu():
    global ventana_actual
    ventana_actual = None
    window.deiconify() 

menu_bar = Menu(window)
window.config(menu=menu_bar)

fileMenu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Operaciones Especiales", menu=fileMenu)

fileMenu.add_command(label="Calculadora", command=lambda: abrir_ventana(calculadora))
fileMenu.add_command(label="IMC", command=lambda: abrir_ventana(imc))
fileMenu.add_command(label="Edad", command=lambda: abrir_ventana(edades))
fileMenu.add_command(label="Clima", command=lambda: abrir_ventana(clima))
fileMenu.add_command(label="Promedio", command=lambda: abrir_ventana(promedio))
fileMenu.add_command(label="Salario", command=lambda: abrir_ventana(salario))
fileMenu.add_command(label="Temperatura", command=lambda: abrir_ventana(temperatura))
fileMenu.add_command(label="Servicios Públicos", command=lambda: abrir_ventana(serviciosPublicos))
fileMenu.add_command(label="Descuentos", command=lambda: abrir_ventana(descuentos))
fileMenu.add_command(label="Combustible", command=lambda: abrir_ventana(combustible))
fileMenu.add_separator()
fileMenu.add_command(label="Datos Estudiantes", command=lambda: abrir_ventana(datos))
fileMenu.add_separator()
fileMenu.add_command(label="Salir", command=window.quit)

tk.Label(window, text="Bienvenido a la Calculadora \nde Operaciones Especiales", font=("Arial", 14, "bold")).pack(pady=20)
tk.Label(window, text="Seleccione una operación \ndel menú 'Operaciones Especiales' para continuar.", font=("Arial", 12)).pack(pady=10)

window.mainloop()