import random

print("===Bienvenidos a la bola mágica===")

def iniciar_bola_magica():

  while True:
    pregunta = input("Hazme una pregunta y te responderé: ")
    if pregunta == 'salir':
       print("===Saliendo de la bola mágica===")
       break 
    else:
        respuestas=[
            "Sí.",
            "No.",
            "Probablemente.",
            "Tal vez.",
            "Puede ser.",
            "No hay imposibles.",
            "No lo creo.",
            "Sin duda.",
            "No puedo responder tu pregunta.",
            "Dejame pensarlo.",
            "Es muy probable.",
            "Es cierto.",
        ] 
    respuesta_aleatoria = random.choice(respuestas) 
    
    print(f"Mi respuesta es: {respuesta_aleatoria}")
    
iniciar_bola_magica()
    
        

