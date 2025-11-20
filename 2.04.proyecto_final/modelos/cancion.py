def agregarCancion():
    nombre = input("Nombre de la canción: ")
    artista = input("Nombre del artista: ")
    duracion = input("Duración: ")  
    cancion = [nombre, artista, duracion]
    return cancion

def mostrarCanciones(playlist):
    print(" ===Lista de canciones=== ")
    canciones = playlist[-1]
    print(f"====({playlist[0]})====")
    for i in range (len(canciones)): 
       print(f"ID:{i} - {canciones[i]}")

def eliminarCancion(playlist, idPlaylist):
    playlist.pop(idPlaylist)
    return playlist
    