import modelos.playlist
from modelos.playlist import agregarPlaylist, eliminarPlaylist, mostrarPlaylists
from modelos.cancion import agregarCancion, mostrarCanciones, eliminarCancion
from modelos.graficas import grafica_canciones_por_genero
from colorama import Fore, Style, init
import pandas as pd

playlists = []

while True:
    op1 = input("""Desea agregar una nueva playlist: """)
    if op1 == "no":
      break
  
    canciones = []
  
    while True:
        print(Fore.LIGHTGREEN_EX + Style.BRIGHT)
        op2 = int(input("""
            1-. Agregar playlist
            2-. Mostrar playlists          
            3-. Eliminar playlist
            4-. Agregar canción
            5-. Mostrar canciones 
            6-. Eliminar canción
            7-. Mostrar gráfica
            8-. Salir
            """))
        match op2:
            case 1:
               playlist = agregarPlaylist()
               playlists.append(playlist)
               print("Se ha agregado la playlist.")
               
            case 2:
               mostrarPlaylists(playlists)
               
            case 3:
                mostrarPlaylists(playlists)
                idPlaylist = int(input("Digíte el id de la playlist: "))
                eliminarPlaylist(playlists, idPlaylist)
                print("Se ha eliminado la playlist")
               
            case 4:
                mostrarPlaylists(playlists)
                idPlaylist = int(input("Digíte el id de la playlist: "))
                cancion = agregarCancion()
                playlists[idPlaylist]["canciones"].append(cancion)
                print("Se ha agregado la canción a la playlist correctamente")
                
            case 5:
                mostrarPlaylists(playlists)
                idPlaylist = int(input("Digíte el id de la playlist: ")) 
                mostrarCanciones(playlists[idPlaylist])
                
            case 6:
                mostrarPlaylists(playlists)
                idPlaylist = int(input("Digíte el id de la playlist: "))
                mostrarCanciones(playlists[idPlaylist])
                idCancion = int(input("Digíte el id de la canción a eliminar: "))
                playlists[idPlaylist]["canciones"] = eliminarCancion(playlists[idPlaylist]["canciones"], idCancion)
                print("Se ha eliminado la canción de la playlist")
                
            case 7:
                grafica_canciones_por_genero(playlists)

            case 8:
                break
                

