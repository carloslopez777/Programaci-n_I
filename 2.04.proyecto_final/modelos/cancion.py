from colorama import Fore, Style, init
import pandas as pd

def agregarCancion():
    nombre = input("Nombre de la canción: ")
    artista = input("Nombre del artista: ")
    duracion = input("Duración: ")  
    cancion = {
        "nombre": nombre,
        "artista": artista,
        "duracion": duracion
    }
    return cancion

def mostrarCanciones(playlist):
    print(Fore.LIGHTMAGENTA_EX + " ===Lista de canciones=== " + Style.BRIGHT)
    for i, cancion in enumerate(playlist["canciones"]):
        print(f"ID:{i} - {cancion["nombre"]} by ({cancion["artista"]}), [{cancion["duracion"]}]")

def eliminarCancion(playlist, idPlaylist):
    playlist.pop(idPlaylist)
    print(Fore.GREEN + "Canción eliminada de la playlist." + Style.RESET_ALL)
    return playlist
    