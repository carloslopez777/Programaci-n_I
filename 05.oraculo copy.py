import datetime

def calcular_elemento(año):
    ultimo_digito = año % 10
    if ultimo_digito in [0, 1]:
        elemento = "Metal"
    elif ultimo_digito in [2, 3]:
        elemento = "Agua"
    elif ultimo_digito in [4, 5]:
        elemento = "Madera"
    elif ultimo_digito in [6, 7]:
        elemento = "Fuego"
    else:
        elemento = "Tierra"
    return elemento

def generar_prediccion(nombre, elemento, numero_suerte):
    match numero_suerte:
        case 1:
            mensaje = f"{nombre}, tu conexión con el elemento {elemento} te traerá gran sabiduría. ¡Es un buen momento para aprender algo nuevo!"
        case 2:
            mensaje = f"Veo que el elemento {elemento} guía tu camino, {nombre}. La fortuna sonríe a los valientes, ¡atrévete a tomar ese riesgo que tienes en mente!"
        case 3:
            mensaje = f"{nombre}, el poder del {elemento} te rodea. Pronto recibirás buenas noticias."
        case 4:
            mensaje = f"{nombre}, tu energía vinculada al elemento {elemento} atraerá prosperidad."
    return mensaje

def iniciar_oraculo():
    while True:
        desea = input("¿Deseas conocer tu destino?").lower()
        if desea != "si":
            print("Saliendo del oráculo")
            break

        nombre = input("Ingresa tu nombre: ")
        año = int(input("Ingresa tu año de nacimiento: "))
        numero_suerte = int(input("Elige un número del 1 al 4: "))

        año_actual = datetime.datetime.now().year
        edad = año_actual - año

        elemento = calcular_elemento(año)
        prediccion = generar_prediccion(nombre, elemento, numero_suerte)
        
        print("*" * 60)
        print(f"{nombre}, tienes {edad} años. Tu elemento es {elemento}.")
        print(prediccion)
        print("*" * 60)

iniciar_oraculo()
