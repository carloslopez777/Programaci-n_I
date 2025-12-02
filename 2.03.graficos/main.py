import tkinter as tk
from tkinter import font, filedialog, messagebox
from config import TITULO, COLOR_BARRA_SUPERIOR, COLOR_MENU_LATERAL, COLOR_PANEL_PRINCIPAL
from util.util_ventana import centrar_ventana, resolver_ruta, cargar_fuente_memoria
from util.util_imagenes import leer_imagen
import pygame
import os

#python -m PyIntaller --noconsole --onefile --icon"./Imagenes/sales.ico"Mi punto de venta"
#--add data "Imagenes;Imagenes"
#--add data "fuentes;fuentes"
#main.py

ruta = ""
estado = ""
nombre_archivo = "<No se ha seleccionado un archivo>"

def bind_hover_events(button):
    button.bind("<Enter>", lambda event:on_enter(event, button))
    button.bind("<Leave>", lambda event:on_leave(event, button) )
    
def on_enter(event, button):
    button.config(bg="#0099CC")
    
def on_leave(event, button):
    button.config(bg=COLOR_MENU_LATERAL)
    
def toggle_panel():
    if menu_lateral.winfo_ismapped():
        menu_lateral.pack_forget()
    else:
        menu_lateral.pack(side=tk.LEFT, fill="y")
        
def limpiar_panel(panel):
    for widget in panel.winfo_children():
        widget.destroy()
        
def mostrar_inicio():
    limpiar_panel(panel_principal)
    label_imagen_principal = tk.Label(panel_principal, text="Inicio")
    label_imagen_principal.pack()
    
def mostrar_ventas():
    limpiar_panel(panel_principal)
    label_imagen_principal = tk.Label(panel_principal, text="Ventas")
    label_imagen_principal.pack()
    
def mostrar_productos():
    limpiar_panel(panel_principal)
    label_imagen_principal = tk.Label(panel_principal, text="Productos")
    label_imagen_principal.pack()
    
def mostrar_reportes():
    limpiar_panel(panel_principal)
    label_imagen_principal = tk.Label(panel_principal, text="Reportes")
    label_imagen_principal.pack()

def mostrar_usuarios():
    limpiar_panel(panel_principal)
    label_imagen_principal = tk.Label(panel_principal, text="Usuarios")
    label_imagen_principal.pack()
    
def mostrar_salir():
    limpiar_panel(panel_principal)
    label_imagen_principal = tk.Label(panel_principal, text="Salir")
    label_imagen_principal.pack()
    
def cargar_cancion():
    global ruta
    ruta = filedialog.askopenfile(title="Elige un mp3", filetypes=[("Archivo MP3", "*.mp3")])
    if ruta:
        global nombre_archivo
        nombre_archivo = os.path.basename(ruta)
    
def reproducir():
    global ruta
    global estado
    if ruta:
        try:
            if estado == "pause":
                pygame.mixer.music.unpause()
                estado = "play"
            else:
                pygame.mixer.music.load(ruta)
                pygame.mixer.music.play()
                
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo reproducir el archivo{e}")
            
    else:
        messagebox.showwarning("Atención", "Primero debes descargar una canción")
        
def pausar():
    pygame.mixer.music.pause()
    global estado
    estado = "pause"

def detener():
    pygame.mixer.music.stop()
    global estado
    estado = "stop"

def cambiar_volumen(valor):
    pygame.mixer.music.set_volume(float((valor/100)))
    return volumen
    
def salir():
    root.destroy()
    
cargar_fuente_memoria("./fuentes/Font Awesome 7 Brands-Regular-400.otf")
cargar_fuente_memoria("./fuentes/Font Awesome 7 Free-Regular-400.otf")
cargar_fuente_memoria("./fuentes/Font Awesome 7 Free-Solid-900.otf")
                
pygame.init()

root = tk.Tk()
root.title(TITULO)
rutaIcono = resolver_ruta("./imagenes/sales.png")
icon = tk.PhotoImage(file=rutaIcono)
root.iconphoto(False, icon)
centrar_ventana(root,1024,600)

barra_superior = tk.Frame(root, height=50, bg=COLOR_BARRA_SUPERIOR)
barra_superior.pack(side=tk.TOP, fill="both")

menu_lateral = tk.Frame(root, width=150, bg=COLOR_MENU_LATERAL)
menu_lateral.pack(side=tk.LEFT, fill= "both", expand=False)

panel_principal = tk.Frame(root, width=150, bg=COLOR_PANEL_PRINCIPAL)
panel_principal.pack(side= tk.RIGHT, fill= "both", expand=True)

#fuentes_disponibles = list(font.families())
#fa_fonts = {f for f in fuentes_disponibles if "Awesome" in f}
#print(fa_fonts)
fontawesome = font.Font(family= "Font Awesome 7 Free", size=20)

boton_menu = tk.Button(
    barra_superior, text="\uf0c9", font= fontawesome
    , bg= COLOR_BARRA_SUPERIOR, fg="#F2F2F2", bd=0, command= toggle_panel
)

boton_menu.pack(padx=10, pady=10, side=tk.LEFT)

label = tk.Label(barra_superior, text="Programación I", font= "Roboto 24"
                 , bg=COLOR_BARRA_SUPERIOR, fg="#F2F2F2")
label.pack(padx=10, pady=10, side=tk.LEFT)

label_musica = tk.Label(barra_superior, text=nombre_archivo, font="Roboto 16"
                        , bg=COLOR_BARRA_SUPERIOR, fg="#F2F2F2")

boton_open = tk.Button(
    barra_superior, text="\uf07c", font= fontawesome
    , bg= COLOR_BARRA_SUPERIOR, fg="#F2F2F2", bd=0, command= cargar_cancion
)

boton_stop = tk.Button(
    barra_superior, text="\uf04d", font= fontawesome
    , bg= COLOR_BARRA_SUPERIOR, fg="#F2F2F2", bd=0, command= detener
)

boton_play = tk.Button(
    barra_superior, text="\uf04b", font= fontawesome
    , bg= COLOR_BARRA_SUPERIOR, fg="#F2F2F2", bd=0, command= reproducir
)

boton_pause = tk.Button(
    barra_superior, text="\uf04c", font= fontawesome
    , bg= COLOR_BARRA_SUPERIOR, fg="#F2F2F2", bd=0, command= pausar
)

volumen = tk.Scale(barra_superior, from_=0, to=100, bg=COLOR_BARRA_SUPERIOR, fg="#F2F2F2"
                   , bd=0, border=0, resolution=1, orient="horizontal", length=200
                   , troughcolor="#95A5A6", activebackground="#0099CC", sliderrelief="flat"
                   , relief="flat", highlightthickness= 0)

volumen.set(50)
volumen.pack(padx=4, pady=10, side=tk.RIGHT)
boton_pause.pack(padx=4, pady=10, side=tk.RIGHT)
boton_play.pack(padx=4, pady=10, side=tk.RIGHT)
boton_stop.pack(padx=4, pady=10, side=tk.RIGHT)
boton_open.pack(padx=4, pady=10, side=tk.RIGHT)

ruta_perfil = resolver_ruta("./imagenes/profile.png")
imagen_perfil = leer_imagen(ruta_perfil, (100,100))
label_perfil = tk.Label(menu_lateral, bg=COLOR_MENU_LATERAL
                        ,image= imagen_perfil)
label_perfil.pack(side=tk.TOP, pady=20)

boton_inicio = tk.Button(
    menu_lateral, text="\uf015, Inicio", bg=COLOR_MENU_LATERAL
    , fg="#F2F2F2", bd=0, width= 12, font=fontawesome, anchor="w", command= mostrar_inicio
)

boton_ventas = tk.Button(
    menu_lateral, text="\uf788, Ventas", bg=COLOR_MENU_LATERAL
    , fg="#F2F2F2", bd=0, width= 12, font=fontawesome, anchor="w", command= mostrar_ventas
)

boton_productos = tk.Button(
    menu_lateral, text="\uf468, Productos", bg=COLOR_MENU_LATERAL
    , fg="#F2F2F2", bd=0, width= 12, font=fontawesome, anchor="w", command= mostrar_productos
)

boton_reportes = tk.Button(
    menu_lateral, text="\uf201, Reportes", bg=COLOR_MENU_LATERAL
    , fg="#F2F2F2", bd=0, width= 12, font=fontawesome, anchor="w", command= mostrar_reportes
)

boton_usuarios = tk.Button(
    menu_lateral, text="\uf007, Usuarios", bg=COLOR_MENU_LATERAL
    , fg="#F2F2F2", bd=0, width= 12, font=fontawesome, anchor="w", command= mostrar_usuarios
)

boton_salir = tk.Button(
    menu_lateral, text="\uf08b, Salir", bg=COLOR_MENU_LATERAL
    , fg="#F2F2F2", bd=0, width= 12, font=fontawesome, anchor="w", command= salir
)

boton_inicio.pack(side=tk.TOP)
boton_ventas.pack(side=tk.TOP)
boton_productos.pack(side=tk.TOP)
boton_reportes.pack(side=tk.TOP)
boton_usuarios.pack(side=tk.TOP)
boton_salir.pack(side=tk.BOTTOM)

bind_hover_events(boton_inicio)
bind_hover_events(boton_ventas)
bind_hover_events(boton_productos)
bind_hover_events(boton_reportes)
bind_hover_events(boton_usuarios)
bind_hover_events(boton_salir)

root.mainloop()