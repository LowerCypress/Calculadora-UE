import tkinter as tk
from tkinter import Menu
from PIL import Image, ImageTk
from operaciones import estilo

def abrir(parent, on_close):
    ventana = tk.Toplevel(parent)
    ventana.title("Calculadora de Promedio")
    ventana.geometry("400x380")
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

    tk.Label(container, text="Calculadora de Promedio", font=("Segoe UI", 14, "bold"), bg=estilo.COLOR_FONDO, fg=estilo.COLOR_AZUL).pack(pady=10)

    tk.Label(container, text="Nota 1:", bg=estilo.COLOR_FONDO, fg=estilo.COLOR_TEXTO).pack()
    entry1 = tk.Entry(container, validate="key", validatecommand=vcmd, justify="center")
    entry1.pack(pady=3)

    tk.Label(container, text="Nota 2:", bg=estilo.COLOR_FONDO, fg=estilo.COLOR_TEXTO).pack()
    entry2 = tk.Entry(container, validate="key", validatecommand=vcmd, justify="center")
    entry2.pack(pady=3)

    tk.Label(container, text="Nota 3:", bg=estilo.COLOR_FONDO, fg=estilo.COLOR_TEXTO).pack()
    entry3 = tk.Entry(container, validate="key", validatecommand=vcmd, justify="center")
    entry3.pack(pady=3)

    lbl_resultado = tk.Label(container, text="Promedio: ", font=("Segoe UI", 10, "bold"), bg=estilo.COLOR_FONDO, fg=estilo.COLOR_ROJO)

    def calcular_promedio():
        val1 = entry1.get()
        val2 = entry2.get()
        val3 = entry3.get()
        
        if not val1 or not val2 or not val3 or val1 == "." or val2 == "." or val3 == ".":
            lbl_resultado.config(text="Error: Ingrese todas las notas válidas", fg="red")
            return
            
        n1 = float(val1)
        n2 = float(val2)
        n3 = float(val3)
        
        promedio_val = (n1 + n2 + n3) / 3
        
        res_str = f"{promedio_val:.2f}".rstrip('0').rstrip('.') if '.' in f"{promedio_val:.2f}" else f"{promedio_val:.2f}"
        lbl_resultado.config(text=f"Promedio: {res_str}", fg="green")

    tk.Button(container, text="Calcular Promedio", command=calcular_promedio, bg=estilo.COLOR_AZUL, fg="white").pack(pady=10)
    lbl_resultado.pack(pady=5)

    # Si el usuario cierra con la X, también volvemos al menú
    ventana.protocol("WM_DELETE_WINDOW", lambda: cerrar(ventana, on_close))

    return ventana

def cerrar(ventana, on_close):
    ventana.destroy()
    on_close()