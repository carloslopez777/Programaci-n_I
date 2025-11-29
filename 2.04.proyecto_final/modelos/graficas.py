import matplotlib.pyplot as plt
from collections import defaultdict

def grafica_canciones_por_genero(playlists):

    streams_por_genero = defaultdict(float)

    for pl in playlists:
        genero = pl["genero"]
        for c in pl["canciones"]:
            streams_por_genero[genero] += c["streams"]  

    if not streams_por_genero:
        print("No hay datos para graficar.")
        return

    generos = list(streams_por_genero.keys())
    totals = list(streams_por_genero.values())

    plt.bar(generos, totals)
    plt.title("Número de reproducciones por género")
    plt.xlabel("Género")
    plt.ylabel("Reproducciones (En millones)")
    plt.tight_layout()
    plt.show()