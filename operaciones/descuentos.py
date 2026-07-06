import tkinter as tk
from tkinter import Menu
from PIL import Image, ImageTk
from operaciones import estilo

def abrir(parent, on_close):
    ventana = tk.Toplevel(parent)
    ventana.title("Calculadora de Descuentos")
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

    tk.Label(container, text="Calculadora de Descuentos", font=("Segoe UI", 14, "bold"), bg=estilo.COLOR_FONDO, fg=estilo.COLOR_AZUL).pack(pady=10)

    tk.Label(container, text="Valor del Producto:", bg=estilo.COLOR_FONDO, fg=estilo.COLOR_TEXTO).pack()
    entry_valor = tk.Entry(container, validate="key", validatecommand=vcmd, justify="center")
    entry_valor.pack(pady=5)

    tk.Label(container, text="Porcentaje de Descuento (%):", bg=estilo.COLOR_FONDO, fg=estilo.COLOR_TEXTO).pack()
    entry_desc = tk.Entry(container, validate="key", validatecommand=vcmd, justify="center")
    entry_desc.pack(pady=5)

    lbl_resultado = tk.Label(container, text="Resultado: ", font=("Segoe UI", 10, "bold"), bg=estilo.COLOR_FONDO, fg=estilo.COLOR_ROJO)

    def calcular_descuento():
        val_prod = entry_valor.get()
        val_desc = entry_desc.get()
        
        if not val_prod or not val_desc or val_prod == "." or val_desc == ".":
            lbl_resultado.config(text="Error: Ingrese valores válidos", fg="red")
            return
            
        prod = float(val_prod)
        pct = float(val_desc)
        
        if pct > 100:
            lbl_resultado.config(text="Error: Descuento no puede superar 100%", fg="red")
            return
            
        descuento = prod * (pct / 100)
        final = prod - descuento
        
        if descuento.is_integer():
            descuento = int(descuento)
        if final.is_integer():
            final = int(final)
            
        lbl_resultado.config(text=f"Descuento: {descuento}\nTotal a Pagar: {final}", fg="green")

    tk.Button(container, text="Calcular Descuento", command=calcular_descuento, bg=estilo.COLOR_AZUL, fg="white").pack(pady=10)
    lbl_resultado.pack(pady=5)

    # Si el usuario cierra con la X, también volvemos al menú
    ventana.protocol("WM_DELETE_WINDOW", lambda: cerrar(ventana, on_close))

    return ventana

def cerrar(ventana, on_close):
    ventana.destroy()
    on_close()