import tkinter as tk
from tkinter import Menu
from PIL import Image, ImageTk
from operaciones import estilo

def abrir(parent, on_close):
    ventana = tk.Toplevel(parent)
    ventana.title("Simulador del Clima")
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

    # Validar entrada (números reales, pueden ser negativos)
    def check_numeric(new_val):
        if new_val == "":
            return True
        if " " in new_val:
            return False
        if new_val in ("-", ".", "-."):
            return True
        try:
            float(new_val)
            return True
        except ValueError:
            return False

    vcmd = (ventana.register(check_numeric), '%P')

    # Contenedor centrado
    container = tk.Frame(ventana, bg=estilo.COLOR_FONDO)
    container.place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(container, text="Simulador del Clima", font=("Segoe UI", 14, "bold"), bg=estilo.COLOR_FONDO, fg=estilo.COLOR_AZUL).pack(pady=10)

    tk.Label(container, text="Temperatura (°C):", bg=estilo.COLOR_FONDO, fg=estilo.COLOR_TEXTO).pack()
    entry_temp = tk.Entry(container, validate="key", validatecommand=vcmd, justify="center")
    entry_temp.pack(pady=5)

    lbl_resultado = tk.Label(container, text="Clima: ", font=("Segoe UI", 10, "bold"), bg=estilo.COLOR_FONDO, fg=estilo.COLOR_ROJO)

    def evaluar_clima():
        val = entry_temp.get()
        if not val or val in ("-", ".", "-."):
            lbl_resultado.config(text="Error: Ingrese un valor válido", fg="red")
            return
            
        temp = float(val)
        
        if temp < 15:
            categoria = "Frío"
            color = "#1f77b4" # Blue
        elif 15 <= temp <= 25:
            categoria = "Templado"
            color = "#2ca02c" # Green
        else:
            categoria = "Caluroso"
            color = "#d62728" # Red
            
        lbl_resultado.config(text=f"El clima es: {categoria}", fg=color)

    tk.Button(container, text="Evaluar Clima", command=evaluar_clima, bg=estilo.COLOR_AZUL, fg="white").pack(pady=10)
    lbl_resultado.pack(pady=5)

    # Si el usuario cierra con la X, también volvemos al menú
    ventana.protocol("WM_DELETE_WINDOW", lambda: cerrar(ventana, on_close))

    return ventana

def cerrar(ventana, on_close):
    ventana.destroy()
    on_close()