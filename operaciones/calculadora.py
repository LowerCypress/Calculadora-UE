import tkinter as tk
from tkinter import Menu
from PIL import Image, ImageTk
from operaciones import estilo

def abrir(parent, on_close):
    ventana = tk.Toplevel(parent)
    ventana.title("Calculadora")
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

    # Validar entrada (solo números decimales/enteros)
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

    tk.Label(container, text="Calculadora Aritmética", font=("Segoe UI", 14, "bold"), bg=estilo.COLOR_FONDO, fg=estilo.COLOR_AZUL).pack(pady=10)

    tk.Label(container, text="Número 1:", bg=estilo.COLOR_FONDO, fg=estilo.COLOR_TEXTO).pack()
    entry1 = tk.Entry(container, validate="key", validatecommand=vcmd, justify="center")
    entry1.pack(pady=5)

    tk.Label(container, text="Número 2:", bg=estilo.COLOR_FONDO, fg=estilo.COLOR_TEXTO).pack()
    entry2 = tk.Entry(container, validate="key", validatecommand=vcmd, justify="center")
    entry2.pack(pady=5)

    lbl_resultado = tk.Label(container, text="Resultado: ", font=("Segoe UI", 10, "bold"), bg=estilo.COLOR_FONDO, fg=estilo.COLOR_ROJO)

    def calcular(operacion):
        val1 = entry1.get()
        val2 = entry2.get()
        if not val1 or not val2 or val1 in ("-", ".", "-.") or val2 in ("-", ".", "-."):
            lbl_resultado.config(text="Error: Ingrese valores numéricos válidos", fg="red")
            return
        
        try:
            num1 = float(val1)
            num2 = float(val2)
        except ValueError:
            lbl_resultado.config(text="Error: Ingrese valores numéricos válidos", fg="red")
            return

        if operacion == "+":
            res = num1 + num2
        elif operacion == "-":
            res = num1 - num2
        elif operacion == "*":
            res = num1 * num2
        elif operacion == "/":
            if num2 == 0:
                lbl_resultado.config(text="Error: División por cero", fg="red")
                return
            res = num1 / num2
        
        if res.is_integer():
            res = int(res)
        lbl_resultado.config(text=f"Resultado: {res}", fg="green")

    # Botones
    btn_frame = tk.Frame(container, bg=estilo.COLOR_FONDO)
    btn_frame.pack(pady=10)

    tk.Button(btn_frame, text="+", width=5, command=lambda: calcular("+"), bg=estilo.COLOR_AZUL, fg="white").grid(row=0, column=0, padx=5)
    tk.Button(btn_frame, text="-", width=5, command=lambda: calcular("-"), bg=estilo.COLOR_AZUL, fg="white").grid(row=0, column=1, padx=5)
    tk.Button(btn_frame, text="*", width=5, command=lambda: calcular("*"), bg=estilo.COLOR_AZUL, fg="white").grid(row=0, column=2, padx=5)
    tk.Button(btn_frame, text="/", width=5, command=lambda: calcular("/"), bg=estilo.COLOR_AZUL, fg="white").grid(row=0, column=3, padx=5)

    lbl_resultado.pack(pady=10)

    ventana.protocol("WM_DELETE_WINDOW", lambda: cerrar(ventana, on_close))

    return ventana

def cerrar(ventana, on_close):
    ventana.destroy()
    on_close()