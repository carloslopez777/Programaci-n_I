def agregarCancion():
    nombre = input("Nombre de la canción: ")
    artista = input("Nombre del artista: ")
    genero = input("Género: ")
    duracion = input("Duración: ")
    
    cancion = {
        "nombre": nombre,
        "artista": artista,
        "genero": genero,
        "duracion": duracion,
    }
    return cancion