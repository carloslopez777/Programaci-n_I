from colorama import Fore, Style, init
import pandas as pd

print(Fore.RED + Style.RESET_ALL)
generos = ("Rap", "Reggaeton", "Pop", "Rock", "Corridos")

def agregarPlaylist():
    print(Fore.BLUE + "Agrega una nueva playlist" + Style.BRIGHT)
    nombre = input("Digíte el nombre de la playlist: ")
    descripcion = input("Descripción de la playlist: ")
    
    print("Género: ")
    for i, genero in enumerate(generos, 1):
        print(f"{i}. {genero}")       
    idGenero = int(input("Seleccione un género: ")) - 1
    genero = generos[idGenero]
    
    playlist = {
        "nombre": nombre,
        "descripcion": descripcion,
        "genero": genero,
        "canciones": []    
    }
    return playlist 

def eliminarPlaylist(playlists, idPlaylist):
    playlists.pop(idPlaylist)
    return playlists

def mostrarPlaylists(playlists):
    print(Fore.LIGHTCYAN_EX + "=== PLAYLISTS ===" + Style.RESET_ALL)
    for i, playlist in enumerate(playlists):
        print(
            f"ID:{i} - {playlist['nombre']} | " 
            f"Descripción: {playlist['descripcion']} | " 
            f"Género: {playlist['genero']}")