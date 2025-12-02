import pandas as pd

def mostrarTabla(playlists):
    filas = []

    for pl in playlists:
        for c in pl["canciones"]:
            filas.append({
                "Playlist": pl["nombre"],
                "Genero": pl["genero"],
                "Cancion": c["nombre"],
                "Artista": c["artista"],
                "Duracion": c["duracion"],
                "Streams (En Millones)": c["streams (en millones)"],
            })

    df = pd.DataFrame(filas)
    print(df)