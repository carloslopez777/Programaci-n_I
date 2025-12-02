import matplotlib.pyplot as plt
from collections import defaultdict

def graficaCanciones(playlists):

    streams_por_genero = defaultdict(float)

    for pl in playlists:
        genero = pl["genero"]
        for c in pl["canciones"]:
            streams_por_genero[genero] += c["streams (en millones)"]  

    generos = list(streams_por_genero.keys())
    totals = list(streams_por_genero.values())

    plt.bar(generos, totals)
    plt.title("Número de streams por género")
    plt.xlabel("Género")
    plt.ylabel("Streams (En millones)")
    plt.tight_layout()
    plt.show()