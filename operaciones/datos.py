import tkinter as tk
from tkinter import Menu
from PIL import Image, ImageTk

def abrir(parent, on_close):
    ventana = tk.Toplevel(parent)
    ventana.title("IMC")
    ventana.geometry("400x550")

    img_original = Image.open("img/logo_uni.png")
    img_redimensionada = img_original.resize((100, 100))
    img = ImageTk.PhotoImage(img_redimensionada)
    lbl_img = tk.Label(ventana, image=img)
    lbl_img.image = img
    lbl_img.pack(pady=10)

    # Barra de menú propia para esta ventana
    menu_bar = Menu(ventana)
    ventana.config(menu=menu_bar)

    fileMenu = Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Operaciones Especiales", menu=fileMenu)
    fileMenu.add_command(label="Volver al menú", command=lambda: cerrar(ventana, on_close))
    fileMenu.add_command(label="Salir", command=parent.quit)

    # Contenido de la ventana
    tk.Label(ventana, text="Datos de Estudiantes", font=("Arial", 14)).pack(pady=20)
    tk.Label(ventana, text="Juan Pablo Diaz", font=("Arial", 12)).pack(pady=10)
    tk.Label(ventana, text="Edad: 19 años", font=("Arial", 10)).pack(pady=5)
    tk.Label(ventana, text="Universidad: La Fundación \nUniversitaria Empresarial Uniempresarial", font=("Arial", 10)).pack(pady=5)
    tk.Label(ventana, text="Carrera: Ingeniería de Software", font=("Arial", 10)).pack(pady=5)
    tk.Label(ventana, text="Correo Institucional: jdiaz@uniempresarial.edu.co", font=("Arial", 10)).pack(pady=5)
    tk.Label(ventana, text="", font=("Arial", 12)).pack(pady=10)
    tk.Label(ventana, text="David Silva Ninco", font=("Arial", 12)).pack(pady=10)
    tk.Label(ventana, text="Edad: 19 años", font=("Arial", 10)).pack(pady=5)
    tk.Label(ventana, text="Universidad: La Fundación \nUniversitaria Empresarial Uniempresarial", font=("Arial", 10)).pack(pady=5)
    tk.Label(ventana, text="Carrera: Ingeniería de Software", font=("Arial", 10)).pack(pady=5)
    tk.Label(ventana, text="Correo Institucional: jdsilva@uniempresarial.edu.co", font=("Arial", 10)).pack(pady=5)

    # Si el usuario cierra con la X, también volvemos al menú
    ventana.protocol("WM_DELETE_WINDOW", lambda: cerrar(ventana, on_close))

    return ventana

def cerrar(ventana, on_close):
    ventana.destroy()
    on_close()