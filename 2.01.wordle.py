import random
palabras = ("abeto", "actor", "abril", "agudo", 
            "bicho", "busca", "boton", "cerdo", 
            "carro", "campo", "costa", "dejar", 
            "error", "fallo", "feria", "gusto")

while True:
    palabra = palabras[random.randint(0,len(palabras)-1)]
    wordle = list(palabra)
    print("""\033[3;37;41m]
======================================[WORDLE]======================================        
    Bienvenido, ya he elegido la palabra secreta: Tienes 5 intentos para adivinarla.
====================================================================================\033[0;30;47m]""")

    for i in range(5):
        intento = input("Ingrese una palabra de 5 letras: ").lower()[:5]
        indice = 0   
        resultado = " "
        correctas = 0
        for letra in intento:
            if letra == wordle[indice]:
                correctas += 1
                resultado += "\033[1;32m" + letra +"\033[0;30m"
            elif letra in wordle:
                resultado += "\033[1;33m" + letra + "\033[0;30m"
            else:
                resultado += "\033[1;31]" + letra + "\033[0;30m"
            indice += 1
        print(resultado)
        if correctas == 5:
           break
       
    if correctas == 5:
        print(f"Felicidades, la palabra \033[1;31m{palabra}\033[0;30m, has acertado")
    else:
        print(f"Lo siento, has fallado. La palabra era: \033[1;31m{palabra}\033[0;30m ")
        
    opcion = input("¿Quieres jugar otra ronda?: ").lower()
    if opcion == "no":
        break
    