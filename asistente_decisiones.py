print("Asistente de decisiones del día")

día = input("El día de hoy es: ")
clima = input("El clima de hoy está: ")

match día:
    case "lunes":
        if clima == "soleado":
            print("Hoy es lunes y está soleado")
        elif clima == "lluvioso":
            print("Hoy es lunes y está lluvioso")
        elif clima == "nublado":
            print("Hoy es lunes y está nublado")
        else:
            print("Clima no reconocido")
            
    case "martes":
        if clima == "soleado":
            print("Hoy es martes y está soleado")
        elif clima == "lluvioso":
            print("Hoy es martes y está lluvioso")
        elif clima == "nublado":
            print("Hoy es martes y está nublado")
        else:
            print("Clima no reconocido")
            
    case "miércoles":
        if clima == "soleado":
            print("Hoy es miércoles y está soleado")
        elif clima == "lluvioso":
            print("Hoy es miércoles y está lluvioso")
        elif clima == "nublado":
            print("Hoy es miércoles y está nublado")
        else:
            print("Clima no reconocido")
            
    case "jueves":
        if clima == "soleado":
            print("Hoy es jueves y está soleado")
        elif clima == "lluvioso":
            print("Hoy es jueves y está lluvioso")
        elif clima == "nublado":
            print("Hoy es jueves y está nublado")
        else:
            print("Clima no reconocido")
            
    case "viernes":
        if clima == "soleado":
            print("Hoy es viernes y está soleado")
        elif clima == "lluvioso":
            print("Hoy es viernes y está lluvioso")
        elif clima == "nublado":
            print("Hoy es viernes y está nublado")
        else:
            print("Clima no reconocido")
            
    case "sábado":
        if clima == "soleado":
            print("Hoy es sábado y está soleado")
        elif clima == "lluvioso":
            print("Hoy es sábado y está lluvioso")
        elif clima == "nublado":
            print("Hoy es sábado y está nublado")
        else:
            print("Clima no reconocido")
            
    case "domingo":
        if clima == "soleado":
            print("Hoy es domingo y está soleado")
        elif clima == "lluvioso":
            print("Hoy es domingo y está lluvioso")
        elif clima == "nublado":
            print("Hoy es domingo y está nublado")
        else:
            print("Clima no reconocido")
            
print("Fin")