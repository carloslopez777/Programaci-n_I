from colorama import Fore, Style, init
import pandas as pd

def agregarPlaylist():
    nombre = input("Nombre de la playlist: ").title()
    descripcion = input("Descripción de la playlist: ")
    
    playlist = {
        "Nombre": nombre,
        "Descripcion": descripcion,
        "Canciones": {}
    }
    return playlist

def eliminarPlaylist(playlists, idPlaylist):
    playlists.pop(idPlaylist)
    print("Playlist eliminada")
    return playlists

def mostrarPlaylists(playlists):
    df = pd.DataFrame(playlists)
    print(Fore.BLUE + "\n--- PLAYLIST COMPLETA ---")
    print(df)