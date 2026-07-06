import tkinter as tk
from tkinter import Menu
from PIL import Image, ImageTk
from operaciones import estilo

def abrir(parent, on_close):
    ventana = tk.Toplevel(parent)
    ventana.title("Conversor de Temperatura")
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

    tk.Label(container, text="Conversor de Temperatura", font=("Segoe UI", 14, "bold"), bg=estilo.COLOR_FONDO, fg=estilo.COLOR_AZUL).pack(pady=10)

    tk.Label(container, text="Temperatura a convertir:", bg=estilo.COLOR_FONDO, fg=estilo.COLOR_TEXTO).pack()
    entry_temp = tk.Entry(container, validate="key", validatecommand=vcmd, justify="center")
    entry_temp.pack(pady=5)

    lbl_resultado = tk.Label(container, text="Resultado: ", font=("Segoe UI", 10, "bold"), bg=estilo.COLOR_FONDO, fg=estilo.COLOR_ROJO)

    def convertir_c_a_f():
        val = entry_temp.get()
        if not val or val in ("-", ".", "-."):
            lbl_resultado.config(text="Error: Ingrese un valor válido", fg="red")
            return
        celsius = float(val)
        fahrenheit = (celsius * 9/5) + 32
        # Remove trailing .00 if integer
        res_str = f"{fahrenheit:.2f}".rstrip('0').rstrip('.') if '.' in f"{fahrenheit:.2f}" else f"{fahrenheit:.2f}"
        lbl_resultado.config(text=f"{celsius}°C = {res_str}°F", fg="green")

    def convertir_f_a_c():
        val = entry_temp.get()
        if not val or val in ("-", ".", "-."):
            lbl_resultado.config(text="Error: Ingrese un valor válido", fg="red")
            return
        fahrenheit = float(val)
        celsius = (fahrenheit - 32) * 5/9
        # Remove trailing .00 if integer
        res_str = f"{celsius:.2f}".rstrip('0').rstrip('.') if '.' in f"{celsius:.2f}" else f"{celsius:.2f}"
        lbl_resultado.config(text=f"{fahrenheit}°F = {res_str}°C", fg="green")

    btn_frame = tk.Frame(container)
    btn_frame.pack(pady=10)

    tk.Button(btn_frame, text="Celsius a Fahrenheit", command=convertir_c_a_f, bg=estilo.COLOR_AZUL, fg="white").grid(row=0, column=0, padx=5)
    tk.Button(btn_frame, text="Fahrenheit a Celsius", command=convertir_f_a_c, bg=estilo.COLOR_AZUL, fg="white").grid(row=0, column=1, padx=5)

    lbl_resultado.pack(pady=5)

    # Si el usuario cierra con la X, también volvemos al menú
    ventana.protocol("WM_DELETE_WINDOW", lambda: cerrar(ventana, on_close))

    return ventana

def cerrar(ventana, on_close):
    ventana.destroy()
    on_close()