import modelos.playlist
from modelos.playlist import agregarPlaylist, eliminarPlaylist, mostrarPlaylists
from modelos.cancion import agregarCancion, mostrarCanciones, eliminarCancion
from modelos.graficas import graficaCanciones
from modelos.pandas import mostrarTabla
from colorama import Fore, Style, init
from modelos.datos import playlists

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
            8-. Mostrar tabla
            9-. Salir
            """))
        match op2:
            case 1:
               playlist = agregarPlaylist()
               playlists.append(playlist)
               print(Fore.GREEN + "Se ha agregado la playlist." + Style.RESET_ALL)
               
            case 2:
               mostrarPlaylists(playlists)
               
            case 3:
                mostrarPlaylists(playlists)
                idPlaylist = int(input("Digíte el id de la playlist: "))
                eliminarPlaylist(playlists, idPlaylist)
                print(Fore.RED + "Se ha eliminado la playlist" + Style.RESET_ALL)
               
            case 4:
                mostrarPlaylists(playlists)
                idPlaylist = int(input("Digíte el id de la playlist: "))
                cancion = agregarCancion()
                playlists[idPlaylist]["canciones"].append(cancion)
                print(Fore.GREEN + "Se ha agregado la canción a la playlist correctamente" + Style.RESET_ALL)
                
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
                print(Fore.RED + "Se ha eliminado la canción de la playlist" + Style.BRIGHT)
                
            case 7:
                graficaCanciones(playlists)
                
            case 8:
                mostrarTabla(playlists)
                
            case 9:
                break
                
