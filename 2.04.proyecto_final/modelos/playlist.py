from colorama import Fore, Style, init
import pandas as pd

def agregarPlaylist():
    nombre = input("Digíte el nombre de la playlist: ")
    descripcion = input("Descripción de la playlist: ")
    canciones= []
    playlist = [nombre, descripcion, canciones]
    return playlist 

def eliminarPlaylist(playlists, idPlaylist):
    playlists.pop(idPlaylist)
    return playlists

def mostrarPlaylists(playlists):
    for i in range (len(playlists)):
        print(f"ID:{i}-{playlists[i][0]}")