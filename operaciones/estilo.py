import tkinter as tk
from tkinter import ttk

COLOR_FONDO = "#f7f8fb"
COLOR_BLANCO = "#ffffff"
COLOR_AZUL = "#2c6df2"
COLOR_ROJO = "#d83b3b"
COLOR_TEXTO = "#2f3640"
COLOR_GRIS = "#7f8c8d"


def aplicar_estilo_ventana(ventana):
    ventana.configure(bg=COLOR_FONDO)

    style = ttk.Style()
    try:
        style.theme_use("clam")
    except tk.TclError:
        pass

    style.configure("TFrame", background=COLOR_FONDO)
    style.configure("Card.TFrame", background=COLOR_BLANCO)
    style.configure("TLabel", background=COLOR_FONDO, foreground=COLOR_TEXTO, font=("Segoe UI", 10))
    style.configure("Header.TLabel", background=COLOR_FONDO, foreground=COLOR_AZUL, font=("Segoe UI", 16, "bold"))
    style.configure("Subtitle.TLabel", background=COLOR_FONDO, foreground=COLOR_GRIS, font=("Segoe UI", 9))
    style.configure("TEntry", fieldbackground=COLOR_BLANCO, foreground=COLOR_TEXTO, borderwidth=1, font=("Segoe UI", 10))
    style.configure("Accent.TButton", font=("Segoe UI", 10, "bold"), foreground=COLOR_BLANCO, background=COLOR_AZUL, borderwidth=0)
    style.map("Accent.TButton", background=[("active", COLOR_ROJO)])
    style.configure("Secondary.TButton", font=("Segoe UI", 10), foreground=COLOR_AZUL, background="#eef2ff", borderwidth=0)
    style.map("Secondary.TButton", background=[("active", "#dcdde1")])
    style.configure("Result.TLabel", background=COLOR_FONDO, foreground=COLOR_ROJO, font=("Segoe UI", 10, "bold"))
