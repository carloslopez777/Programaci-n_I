#Descripción del proyecto

#Spotrofy es una aplicación que permite crear, administrar y visualizar playlists musicales, 
#además de registrar canciones, generar estadísticas y reproducir archivos MP3 desde una interfaz gráfica.

#El proyecto está dividido en dos partes:

#Aplicación por consola: Permite crear playlists, agregar canciones y generar gráficas. Usa diccionarios, listas, tuplas, pandas y matplotlib.

#Interfaz gráfica (GUI): Simula un reproductor musical, muestra secciones de playlists, géneros, artistas, etc.
#Utiliza Tkinter y Pygame para la interfaz y sonido.

#Instrucciones de ejecución:
#1. Para usar la versión por consola

#Ejecuta:

#python main.py


#En la consola aparecerá el menú:

#1-. Agregar playlist
#2-. Mostrar playlists
#3-. Eliminar playlist
#4-. Agregar canción
#5-. Mostrar canciones
#6-. Eliminar canción
#7-. Mostrar gráfica
#-. Salir

#Funciones de consola:

#Registrar playlists con nombre, descripción y género.

#Añadir canciones con artista, duración y streams.

#Mostrar todo lo registrado.

#Eliminar playlists o canciones.

#Generar una gráfica por género basada en sus reproducciones.

#Crear tablas CSV automáticamente usando pandas.

#2. Para ejecutar la interfaz gráfica

#Ejecuta:

#python interfaz.py


#La interfaz incluye:

#Menú lateral (Inicio, Playlists, Favoritos, Géneros, Artistas, Radio).

#Barra superior con: Cargar canción, Play / Pausa / Stop, control de volumen


#Generación de gráficos

#El archivo graficas.py genera una gráfica de streams por género:

#from modelos.graficas import grafica_canciones_por_genero
#grafica_canciones_por_genero(playlists)


#Ejemplo de gráfico generado:

#Eje X → Géneros

#Eje Y → Reproducciones totales

#Muestra barras por género en millones de streams.

#Uso de Pandas: El sistema exporta automáticamente las playlists a un archivo:

#datos/playlists.csv


#Con columnas:

#| Playlist | Descripción | Género | Canción | Artista | Duración | Streams |

#Esto permite consultar las playlists registradas incluso después de cerrar el programa.

#Ejemplo de ejecución:
#Digite el nombre de la playlist: Rap Hits
#Descripción: Solo canciones de rap
#Género:
#1. Rap
#2. Reggaeton
#3. Pop
#Seleccione un género: 1
#Se ha agregado la playlist.

#1-. Agregar canción
#4

#Nombre de la canción: Hell of a Life
#Artista: Kanye West
#Duración: 6:36
#Streams (En Millones): 562
#Se ha agregado la canción correctamente

#7-. Mostrar gráfica
#→ Se muestra gráfica de streams por género