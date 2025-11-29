import os
import sys
import ctypes

def centrar_ventana (ventana, ancho, alto):
    pantalla_ancho = ventana.winfo_screenwidth()
    pantalla_largo = ventana.winfo_screenheight()
    x = int( (pantalla_ancho/2) - (ancho/2) )
    y = int( (pantalla_largo/2) - (alto/2) )
    return ventana.geometry(f"{ancho}x{alto}+{x}+{y}")

def resolver_ruta(ruta_relativa):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, ruta_relativa)
    
    return os.path.join(os.path.abspath("."), ruta_relativa)

def cargar_fuente_memoria(ruta_fuente):
    path_fuente = resolver_ruta(ruta_fuente)
    
    gdi32 = ctypes.windll.gdi32
    ret = gdi32.AddFontResourceExW(path_fuente, "8x10", 0)
    
    if ret == 0:
       print(f"Error cargando la fuente: {ruta_fuente}")
    else:
        print(f"Error") 