import modelos.playlist
from modelos.playlist import agregarPlaylist, eliminarPlaylist, mostrarPlaylists
from modelos.cancion import agregarCancion
from colorama import Fore, Style, init
import pandas as pd

while True:
    op1 = input("""Desea agregar una nueva playlist: """)
    if op1 == "no":
      break
  
    while True:
        op2 = int(input("""
            1-. Agregar playlist
            2-. Mostrar playlists          
            3-. Eliminar playlist
            4-. Agregar canción
            5-. Mostrar canciones 
            6-. Eliminar canción
            7-. Salir
            """))
        match op2:
            case 1:
               nombre = ("Ingrese nombre de la playlist:")
               playlist = agregarPlaylist()
               playlist[nombre] = playlist
               print("Se ha agregado la playlist.")
               
            case 2:
               mostrarPlaylists(playlist)
               

