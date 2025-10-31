print("Analizador de textos")

texto = input("Ingresa texto:").lower()

letras = []
for i in range(3):
    letra = input("Ingrese la letra:").lower()
    
print ("Resultados")

for letra in letras:
    cantidad = texto.count(letra)
    print(f"La letra '{letra}' aparece {cantidad} veces en el texto.")
    
palabras = texto.split()
total_palabras = len(palabras)
print(f"La cantidad de palabras son: {total_palabras}")

primera_letra = texto [0]
ultima_letra = texto [-1]
print(f"Primera letra: {primera_letra}")
print(f"Ultima letra: {ultima_letra}")

texto_invetido = " ".join(palabras[::-1])
print(texto_invetido)

contiene_python = "python" in texto
if contiene_python:
    print("La palabra python se encuentra en el texto.")
else:
    print("La palabra python no se encuentra en el texto.")