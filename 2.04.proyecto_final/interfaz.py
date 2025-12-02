import tkinter as tk
from tkinter import font, filedialog, messagebox
from config import TITULO,COLOR_BARRA_INFERIOR,COLOR_MENU_LATERAL,COLOR_PANEL_PRINCIPAL
from util.util_ventana import centrar_ventana, cargar_fuente_memoria, resolver_ruta
from util.util_imagenes import leer_imagen
import pygame
import os

#python -m PyIntaller --noconsole --onefile --icon" --icon="./imagenes/musicaa.png" --name="Spotrofy
# --add-data "imagenes;imagenes"
# --add-data "fuentes:fuentes"
# interfaz.py

ruta=""
estado=""
nombre_archivo="<No se ha seleccionado un archivo>"


def bind_hover_events(button):
    button.bind("<Enter>", lambda event:on_enter(event,button))
    button.bind("<Leave>", lambda event:on_leave(event,button))

def on_enter(event,button):
    button.config(bg="#02465D")

def on_leave(event,button):
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
    label_imagen_principal = tk.Label(panel_principal,text="Inicio")
    label_imagen_principal.pack()

def mostrar_playlists():
    limpiar_panel(panel_principal)
    label_imagen_principal = tk.Label(panel_principal,text="Playlists")
    label_imagen_principal.pack()    

def mostrar_favoritos():
    limpiar_panel(panel_principal)
    label_imagen_principal = tk.Label(panel_principal,text="Favoritos")
    label_imagen_principal.pack()    

def mostrar_generos():
    limpiar_panel(panel_principal)
    label_imagen_principal = tk.Label(panel_principal,text="Generos")
    label_imagen_principal.pack() 

def mostrar_artistas():
    limpiar_panel(panel_principal)
    label_imagen_principal = tk.Label(panel_principal,text="Artistas")
    label_imagen_principal.pack() 

def mostrar_radio():
    limpiar_panel(panel_principal)
    label_imagen_principal = tk.Label(panel_principal,text="Radio Potro")
    label_imagen_principal.pack() 

def cargar_cancion():
    global ruta
    ruta = filedialog.askopenfilename(title="Elige un mp3", filetypes=[("Archivos MP3","*.mp3")])

    if ruta:
        global nombre_archivo
        nombre_archivo = os.path.basename(ruta)
        label_musica.config(text=nombre_archivo)

#Si estaba pausado, se quita el pause    
def reproducir():
    global ruta
    global estado
    if ruta:
        try:
            if estado=="pause":
                pygame.mixer.music.unpause()
                estado="play"
            else:
                estado="play"
                pygame.mixer.music.load(ruta)
                pygame.mixer.music.play()
        except Exception as e:
            messagebox.showerror("Error",f"No se pudo reproducir el archivo {e}")
    else:
        messagebox.showwarning("Atención", "Primero debes cargar una canción")        

def pausar():
    pygame.mixer.music.pause()
    global estado
    estado = "pause"

def detener():
    global estado
    estado = "stop"

#volumen de 0 a 1
def cambiar_volumen(valor):
    return "volumen"
    pygame.mixer.music.set_volume(float(valor)/100)

def salir():
    root.destroy()

#Cargar las fuentes.
cargar_fuente_memoria("C:/Users/rafay/OneDrive/Documents/Programación I/Programacion1/Proyecto final/fuentes/Font Awesome 7 Brands-Regular-400.otf")
cargar_fuente_memoria("C:/Users/rafay/OneDrive/Documents/Programación I/Programacion1/Proyecto final/fuentes/Font Awesome 7 Free-Regular-400.otf")
cargar_fuente_memoria("C:/Users/rafay/OneDrive/Documents/Programación I/Programacion1/Proyecto final/fuentes/Font Awesome 7 Free-Solid-900.otf")

pygame.mixer.init()

root = tk.Tk()
root.title(TITULO)
rutaIcono = resolver_ruta("./imagenes/musicaa.png")
icon = tk.PhotoImage(file=rutaIcono)
root.iconphoto(False,icon)

centrar_ventana(root,1024,700)

barra_inferior = tk.Frame(root,height=50,bg=COLOR_BARRA_INFERIOR)
barra_inferior.pack(side=tk.BOTTOM, fill="both")

menu_lateral = tk.Frame(root,width=150,bg=COLOR_MENU_LATERAL)
menu_lateral.pack(side=tk.LEFT, fill="both",expand=False)

panel_principal = tk.Frame(root,width=150,bg=COLOR_PANEL_PRINCIPAL)
panel_principal.pack(side=tk.RIGHT, fill="both",expand=True)


fontawesome = font.Font(family="Font Awesome 7 Free",size=20)

btn_menu= tk.Button(barra_inferior, text="\uf0ca", font=fontawesome,bg=COLOR_BARRA_INFERIOR, fg="#f2f2f2",bd=0, command=toggle_panel)
btn_menu.pack(padx=10, pady=10, side=tk.LEFT)

label = tk.Label(barra_inferior,text="Proyecto Final Interfaz",font="Gabriola 18",bg=COLOR_BARRA_INFERIOR,fg="#f2f2f2")

label_musica = tk.Label(barra_inferior,text= nombre_archivo, font="Roboto 14", bg=COLOR_BARRA_INFERIOR, fg="#f2f2f2", padx=20)

btn_open= tk.Button(barra_inferior, text="\uf07c", font=fontawesome,bg=COLOR_BARRA_INFERIOR, fg="#f2f2f2",bd=0, command=cargar_cancion)

btn_stop= tk.Button(barra_inferior, text="\uf28d", font=fontawesome,bg=COLOR_BARRA_INFERIOR, fg="#f2f2f2",bd=0, command=detener)

btn_play= tk.Button(barra_inferior, text="\uf144", font=fontawesome,bg=COLOR_BARRA_INFERIOR, fg="#f2f2f2",bd=0, command=reproducir)

btn_pause= tk.Button(barra_inferior, text="\uf28b", font=fontawesome,bg=COLOR_BARRA_INFERIOR, fg="#f2f2f2",bd=0, command=pausar)

btn_backward= tk.Button(barra_inferior,font=fontawesome,bg=COLOR_BARRA_INFERIOR, fg="#f2f2f2",bd=0)

btn_forward= tk.Button(barra_inferior, font=fontawesome,bg=COLOR_BARRA_INFERIOR, fg="#f2f2f2",bd=0)
volumen = tk.Scale(barra_inferior, from_=0, to=100, resolution=1, orient="horizontal", bd=0, bg=COLOR_BARRA_INFERIOR, fg="#f2f2f2", length=150, troughcolor="#95a5a6", activebackground="#0099cc", sliderrelief="flat", relief="flat", highlightthickness=0)
volumen.set(50)


volumen.pack(padx=4, pady=10, side=tk.RIGHT)
label.pack(padx=10, pady=10, side=tk.RIGHT)
btn_backward.pack(padx=2, pady=10, side=tk.LEFT)
btn_stop.pack(padx=2, pady=10, side=tk.LEFT)
btn_play.pack(padx=2, pady=10, side=tk.LEFT)
btn_pause.pack(padx=2, pady=10, side=tk.LEFT)
btn_forward.pack(padx=2, pady=10, side=tk.LEFT)
btn_open.pack(padx=2, pady=10, side=tk.LEFT)
label_musica.pack(padx=2, pady=10, side=tk.LEFT)

ruta_perfil = resolver_ruta("./imagenes/pperfil.png")
imagen_perfil = leer_imagen(ruta_perfil, (100,100))
label_perfil = tk.Label(menu_lateral,image=imagen_perfil, bg=COLOR_MENU_LATERAL)
label_perfil.pack(side=tk.TOP, pady=30)

ruta_principal = resolver_ruta("C:/Users/rafay/OneDrive/Documents/Programación I/Programacion1/Proyecto final/imagenes/potros.png")
imagen_principal = leer_imagen(ruta_perfil, (100,100))
label_principal = tk.Label()

btn_inicio = tk.Button(menu_lateral, text="\ue1b0 Inicio", bg=COLOR_MENU_LATERAL, width=12, fg="#f2f2f2", bd=0, font="Pristina 24", command=mostrar_inicio)
btn_inicio.pack(side=tk.TOP)

btn_playlist = tk.Button(menu_lateral, text="\uf1c7 Playlists", bg=COLOR_MENU_LATERAL, width=12, fg="#f2f2f2", bd=0, font="Pristina 20", command=mostrar_playlists)
btn_playlist.pack(side=tk.TOP)

btn_favoritos = tk.Button(menu_lateral, text="\uf005 Favoritos", bg=COLOR_MENU_LATERAL, width=12, fg="#f2f2f2", bd=0, font="Pristina 20", command=mostrar_favoritos)
btn_favoritos.pack(side=tk.TOP)

btn_generos = tk.Button(menu_lateral, text="\uf51f Generos", bg=COLOR_MENU_LATERAL, width=12, fg="#f2f2f2", bd=0, font="Pristina 20", command=mostrar_generos)
btn_generos.pack(side=tk.TOP)

btn_artistas = tk.Button(menu_lateral, text="\uf3d2 Artistas", bg=COLOR_MENU_LATERAL, width=12, fg="#f2f2f2", bd=0, font="Pristina 20", command=mostrar_artistas)
btn_artistas.pack(side=tk.TOP)

btn_radio = tk.Button(menu_lateral, text="\uf8d7 Potro Radio", bg=COLOR_MENU_LATERAL, width=12, fg="#f2f2f2", bd=0, font="Pristina 20", command=mostrar_radio)
btn_radio.pack(side=tk.TOP)

btn_salir = tk.Button(menu_lateral, text="\uf08b Salir", bg=COLOR_MENU_LATERAL, width=12, fg="#f2f2f2", bd=0, font="Roboto 20", command=salir)
btn_salir.pack(side=tk.BOTTOM)

bind_hover_events(btn_inicio)
bind_hover_events(btn_playlist)
bind_hover_events(btn_favoritos)
bind_hover_events(btn_generos)
bind_hover_events(btn_artistas)
bind_hover_events(btn_radio)
bind_hover_events(btn_salir)


root.mainloop()