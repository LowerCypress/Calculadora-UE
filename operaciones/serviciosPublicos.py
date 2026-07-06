import tkinter as tk
from tkinter import Menu
from PIL import Image, ImageTk
from operaciones import estilo

def abrir(parent, on_close):
    ventana = tk.Toplevel(parent)
    ventana.title("Calculadora de Servicios Públicos")
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

    tk.Label(container, text="Factura de Energía", font=("Segoe UI", 14, "bold"), bg=estilo.COLOR_FONDO, fg=estilo.COLOR_AZUL).pack(pady=10)

    tk.Label(container, text="Consumo de Energía (kWh):", bg=estilo.COLOR_FONDO, fg=estilo.COLOR_TEXTO).pack()
    entry_consumo = tk.Entry(container, validate="key", validatecommand=vcmd, justify="center")
    entry_consumo.pack(pady=5)

    lbl_resultado = tk.Label(container, text="Total a pagar: ", font=("Segoe UI", 10, "bold"), bg=estilo.COLOR_FONDO, fg=estilo.COLOR_ROJO)

    # Tarifa: 650 COP por kWh
    TARIFA_KWH = 650.0

    def calcular_factura():
        val = entry_consumo.get()
        if not val or val == ".":
            lbl_resultado.config(text="Error: Ingrese un consumo válido", fg="red")
            return
            
        consumo = float(val)
        total = consumo * TARIFA_KWH
        
        if total.is_integer():
            total = int(total)
            
        lbl_resultado.config(text=f"Total a pagar: ${total} COP\n(Tarifa: ${int(TARIFA_KWH)} COP/kWh)", fg="green")

    tk.Button(container, text="Calcular Factura", command=calcular_factura, bg=estilo.COLOR_AZUL, fg="white").pack(pady=10)
    lbl_resultado.pack(pady=5)

    # Si el usuario cierra con la X, también volvemos al menú
    ventana.protocol("WM_DELETE_WINDOW", lambda: cerrar(ventana, on_close))

    return ventana

def cerrar(ventana, on_close):
    ventana.destroy()
    on_close()