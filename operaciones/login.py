import sqlite3
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk  # Importamos la extensión de temas y estilos modernos
from PIL import Image, ImageTk

def conectar_db():
    conn = sqlite3.connect("usuarios.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario TEXT UNIQUE NOT NULL,
            clave TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def iniciar_login(window, al_conectar_exitoso):
    conectar_db()
    
    def validar_login():
        usuario = entrada_usuario.get().strip()
        clave = entrada_clave.get().strip()
        
        if not usuario or not clave:
            messagebox.showwarning("Campos vacíos", "Por favor, llena ambos campos.")
            return

        conn = sqlite3.connect("usuarios.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE usuario = ? AND clave = ?", (usuario, clave))
        resultado = cursor.fetchone()
        conn.close()
        
        if resultado:
            messagebox.showinfo("Acceso permitido", f"Bienvenido, {usuario}")
            ventana_login.destroy()
            al_conectar_exitoso()    
        else:
            messagebox.showerror("Acceso denegado", "Usuario o clave incorrectos")

    def registrar_cuenta():
        usuario = entrada_usuario.get().strip()
        clave = entrada_clave.get().strip()
        
        if not usuario or not clave:
            messagebox.showwarning("Campos vacíos", "Escribe un usuario y contraseña para registrarlos.")
            return
            
        conn = sqlite3.connect("usuarios.db")
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO usuarios (usuario, clave) VALUES (?, ?)", (usuario, clave))
            conn.commit()
            messagebox.showinfo("Éxito", f"¡Cuenta de '{usuario}' creada!\nYa puedes iniciar sesión.")
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "Este nombre de usuario ya existe. Elige otro.")
        finally:
            conn.close()

    # --- Configuración de la Ventana ---
    ventana_login = tk.Toplevel(window)
    ventana_login.title("Inicio de Sesión")
    ventana_login.geometry("440x390") 
    ventana_login.resizable(False, False)
    ventana_login.configure(bg="#f5f6fa")  # Fondo gris claro moderno
    
    ventana_login.protocol("WM_DELETE_WINDOW", window.quit)

    # --- Estilos Personalizados (TTK) ---
    style = ttk.Style()
    style.theme_use('clam') # Usamos un tema base limpio para poder personalizarlo

    # Configuración de fuentes y etiquetas
    style.configure("TLabel", background="#f5f6fa", foreground="#2f3640", font=("Segoe UI", 10))
    style.configure("Header.TLabel", background="#f5f6fa", foreground="#2f3640", font=("Segoe UI", 16, "bold"))
    
    # Configuración de los campos de entrada
    style.configure("TEntry", fieldbackground="white", borderwidth=1, font=("Segoe UI", 10))

    # Botón Principal (Ingresar) - Color Azul/Llamativo
    style.configure("Accent.TButton", font=("Segoe UI", 10, "bold"), foreground="white", background="#4a69bd", borderwidth=0)
    style.map("Accent.TButton", background=[("active", "#3b5998")])

    # Botón Secundario (Registrar) - Color Neutro/Bordeado
    style.configure("Secondary.TButton", font=("Segoe UI", 10), foreground="#4a69bd", background="#e1e8f0", borderwidth=0)
    style.map("Secondary.TButton", background=[("active", "#dcdde1")])

    # --- Contenedor Principal (Padding interno) ---
    contenedor = ttk.Frame(ventana_login, padding=30, style="TLabel")
    contenedor.pack(fill=tk.BOTH, expand=True)

    # --- Elementos de la Interfaz ---
    img_original = Image.open("img/logo_uni.png")
    img_redimensionada = img_original.resize((90, 90), Image.Resampling.LANCZOS)
    img = ImageTk.PhotoImage(img_redimensionada)
    lbl_img = tk.Label(contenedor, image=img, bg="#f5f6fa")
    lbl_img.image = img
    lbl_img.grid(row=0, column=0, columnspan=2, pady=(0, 10))

    # Título
    titulo = ttk.Label(contenedor, text="Bienvenido", style="Header.TLabel")
    titulo.grid(row=1, column=0, columnspan=2, sticky="w", pady=(0, 5))
    
    subtitulo = ttk.Label(contenedor, text="Ingresa tus credenciales para continuar", foreground="#7f8c8d", font=("Segoe UI", 9))
    subtitulo.grid(row=2, column=0, columnspan=2, sticky="w", pady=(0, 20))

    # Campo Usuario
    ttk.Label(contenedor, text="Usuario").grid(row=3, column=0, columnspan=2, sticky="w", pady=(0, 5))
    entrada_usuario = ttk.Entry(contenedor, width=35)
    entrada_usuario.grid(row=4, column=0, columnspan=2, sticky="we", pady=(0, 15))
    entrada_usuario.focus() # Auto-foco en el usuario al abrir

    # Campo Contraseña
    ttk.Label(contenedor, text="Contraseña").grid(row=5, column=0, columnspan=2, sticky="w", pady=(0, 5))
    entrada_clave = ttk.Entry(contenedor, show="*", width=35)
    entrada_clave.grid(row=6, column=0, columnspan=2, sticky="we", pady=(0, 25))

    # Botones (Distribuidos proporcionalmente en columnas)
    boton_ingresar = ttk.Button(contenedor, text="Ingresar", command=validar_login, style="Accent.TButton", cursor="hand2")
    boton_ingresar.grid(row=7, column=0, sticky="we", padx=(0, 5), ipady=4)

    boton_registrar = ttk.Button(contenedor, text="Registrar cuenta", command=registrar_cuenta, style="Secondary.TButton", cursor="hand2")
    boton_registrar.grid(row=7, column=1, sticky="we", padx=(5, 0), ipady=4)

    # Configurar pesos de las columnas para que los botones tengan el mismo tamaño
    contenedor.columnconfigure(0, weight=1)
    contenedor.columnconfigure(1, weight=1)


if __name__ == "__main__":
    def funcion_exito():
        print("¡El login fue exitoso!")
        ventana_principal = tk.Tk()
        ventana_principal.title("Ventana Principal")
        ventana_principal.geometry("400x300")
        
        # También le damos un toque limpio a la ventana principal
        ventana_principal.configure(bg="#f5f6fa")
        ttk.Label(ventana_principal, text="¡Estás dentro del sistema!", font=("Segoe UI", 14, "bold"), background="#f5f6fa").pack(pady=50)
        ventana_principal.mainloop()

    raiz = tk.Tk()
    raiz.withdraw() 
    
    iniciar_login(raiz, funcion_exito)
    raiz.mainloop()