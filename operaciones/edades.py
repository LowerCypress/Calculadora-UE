import tkinter as tk
from tkinter import Menu
from PIL import Image, ImageTk
import datetime
from operaciones import estilo

def abrir(parent, on_close):
    ventana = tk.Toplevel(parent)
    ventana.title("Calculadora de Edad")
    ventana.geometry("400x300")
    estilo.aplicar_estilo_ventana(ventana)

    img_original = Image.open("img/logo_uni.png")
    img_redimensionada = img_original.resize((100, 100), Image.Resampling.LANCZOS)
    img = ImageTk.PhotoImage(img_redimensionada)
    lbl_img = tk.Label(ventana, image=img, bg=estilo.COLOR_FONDO)
    lbl_img.image = img
    lbl_img.pack(pady=10)

    # Barra de menú propia para esta ventana
    menu_bar = Menu(ventana)
    ventana.config(menu=menu_bar)

    fileMenu = Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Operaciones Especiales", menu=fileMenu)
    fileMenu.add_command(label="Volver al menú", command=lambda: cerrar(ventana, on_close))
    fileMenu.add_command(label="Salir", command=parent.quit)

    # Validar entrada (solo enteros positivos)
    def check_integer(new_val):
        if new_val == "":
            return True
        if " " in new_val:
            return False
        return new_val.isdigit()

    vcmd = (ventana.register(check_integer), '%P')

    # Contenedor centrado
    container = tk.Frame(ventana, bg=estilo.COLOR_FONDO)
    container.place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(container, text="Calculadora de Edad", font=("Segoe UI", 14, "bold"), bg=estilo.COLOR_FONDO, fg=estilo.COLOR_AZUL).pack(pady=10)

    tk.Label(container, text="Año de Nacimiento:", bg=estilo.COLOR_FONDO, fg=estilo.COLOR_TEXTO).pack()
    entry_anio = tk.Entry(container, validate="key", validatecommand=vcmd, justify="center")
    entry_anio.pack(pady=5)

    lbl_resultado = tk.Label(container, text="Edad: ", font=("Segoe UI", 10, "bold"), bg=estilo.COLOR_FONDO, fg=estilo.COLOR_ROJO)

    def calcular_edad():
        val = entry_anio.get()
        if not val:
            lbl_resultado.config(text="Error: Ingrese un año válido", fg="red")
            return
        
        anio_nac = int(val)
        anio_actual = datetime.datetime.now().year
        
        if anio_nac > anio_actual:
            lbl_resultado.config(text="Error: El año es posterior al actual", fg="red")
            return
        
        edad = anio_actual - anio_nac
        lbl_resultado.config(text=f"Edad: {edad} años", fg="green")

    tk.Button(container, text="Calcular Edad", command=calcular_edad, bg=estilo.COLOR_AZUL, fg="white").pack(pady=10)
    lbl_resultado.pack(pady=5)

    # Si el usuario cierra con la X, también volvemos al menú
    ventana.protocol("WM_DELETE_WINDOW", lambda: cerrar(ventana, on_close))

    return ventana

def cerrar(ventana, on_close):
    ventana.destroy()
    on_close()