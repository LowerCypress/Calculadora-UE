import tkinter as tk
from tkinter import Menu
from PIL import Image, ImageTk
from operaciones import estilo

def abrir(parent, on_close):
    ventana = tk.Toplevel(parent)
    ventana.title("Calculadora de IMC")
    ventana.geometry("400x350")
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

    # Validar entrada (solo números reales positivos)
    def check_positive_numeric(new_val):
        if new_val == "":
            return True
        if " " in new_val:
            return False
        if "-" in new_val:
            return False
        if new_val == ".":
            return True
        try:
            float(new_val)
            return True
        except ValueError:
            return False

    vcmd = (ventana.register(check_positive_numeric), '%P')

    # Contenedor centrado
    container = tk.Frame(ventana, bg=estilo.COLOR_FONDO)
    container.place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(container, text="Calculadora de IMC", font=("Segoe UI", 14, "bold"), bg=estilo.COLOR_FONDO, fg=estilo.COLOR_AZUL).pack(pady=10)

    tk.Label(container, text="Peso (kg):", bg=estilo.COLOR_FONDO, fg=estilo.COLOR_TEXTO).pack()
    entry_peso = tk.Entry(container, validate="key", validatecommand=vcmd, justify="center")
    entry_peso.pack(pady=5)

    tk.Label(container, text="Estatura (m):", bg=estilo.COLOR_FONDO, fg=estilo.COLOR_TEXTO).pack()
    entry_estatura = tk.Entry(container, validate="key", validatecommand=vcmd, justify="center")
    entry_estatura.pack(pady=5)

    lbl_resultado = tk.Label(container, text="IMC: ", font=("Segoe UI", 10, "bold"), bg=estilo.COLOR_FONDO, fg=estilo.COLOR_ROJO)

    def calcular_imc():
        val_peso = entry_peso.get()
        val_est = entry_estatura.get()
        
        if not val_peso or not val_est or val_peso == "." or val_est == ".":
            lbl_resultado.config(text="Error: Ingrese valores válidos", fg="red")
            return
        
        peso = float(val_peso)
        estatura = float(val_est)
        
        if estatura <= 0 or peso <= 0:
            lbl_resultado.config(text="Error: Valores deben ser mayores a 0", fg="red")
            return
            
        imc_val = peso / (estatura * estatura)
        
        # Clasificación del IMC
        if imc_val < 18.5:
            clasif = "Bajo peso"
            color = "orange"
        elif 18.5 <= imc_val < 25:
            clasif = "Normal"
            color = "green"
        elif 25 <= imc_val < 30:
            clasif = "Sobrepeso"
            color = "orange"
        else:
            clasif = "Obesidad"
            color = "red"
            
        lbl_resultado.config(text=f"IMC: {imc_val:.2f} ({clasif})", fg=color)

    tk.Button(container, text="Calcular IMC", command=calcular_imc, bg=estilo.COLOR_AZUL, fg="white").pack(pady=10)
    lbl_resultado.pack(pady=5)

    # Si el usuario cierra con la X, también volvemos al menú
    ventana.protocol("WM_DELETE_WINDOW", lambda: cerrar(ventana, on_close))

    return ventana

def cerrar(ventana, on_close):
    ventana.destroy()
    on_close()