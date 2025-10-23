playlist_musica = ["Bohemian Rhapsody", "Hotel California", "Stairway to Heaven"]
print("Lista original :", playlist_musica)

print("El DJ dice que Hotel California está muy vieja")

playlist_musica.remove("Hotel California")
playlist_musica[1] = "Shape of You"
print("Lista modificada: ", playlist_musica)

playlist_musica.insert(0, "Watermelon Sugar")
print("Lista modificada :", playlist_musica)

playlist_musica.pop()
print("Después de remove :", playlist_musica)

print("Cantidad de canciones :", len(playlist_musica))