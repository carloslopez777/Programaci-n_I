from colorama import Fore, Style, init
import pandas as pd

def agregarCancion():
    print(Fore.LIGHTGREEN_EX + " === Añade una canción para tu playlist: === " + Style.NORMAL)
    nombre = input("Nombre de la canción: ")
    artista = input("Nombre del artista: ")
    duracion = input("Duración: ") 
    streams = int(input("Streams (En Millones): "))
    
    cancion = {
        "nombre": nombre,
        "artista": artista,
        "duracion": duracion,
        "streams (en millones)": streams
    }
    return cancion

def mostrarCanciones(playlist):
    print(Fore.LIGHTMAGENTA_EX + " ===Lista de canciones=== " + Style.BRIGHT)
    for i, cancion in enumerate(playlist["canciones"]):
        print(f"ID:{i} - {cancion["nombre"]} by {cancion["artista"]}, [{cancion["duracion"]}], [{cancion["streams (en millones)"]}]")

def eliminarCancion(playlist, idPlaylist):
    playlist.pop(idPlaylist)
    return playlist
    