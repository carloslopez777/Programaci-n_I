import tkinter as tk

#Ventana principal
root = tk.Tk()
root.title("Calculadora")
root.geometry("305x500")

#Agregar widgets
botones_texto = (
                "C", "/", "*", "-",
                "7", "8", "9", "+",
                "4", "5", "6", "",
                "1", "2", "3", "=",
                "0", ".", "", "")

historico = tk.Label(root, bg="#F2F2F2", font="Roboto 14"
                     , width= 15, bd= 0)

historico.pack(pady= 5, padx= 10, fill= "x")

resultado = tk.Entry(root, bg="#FFFFFF", bd= 1, 
                     font= "Roboto 24", width= 15, justify="right")

resultado.pack(padx= 10, fill= "x")

contenedor_botones = tk.Frame(root, bg="#898787")
contenedor_botones.pack(pady= 5, padx= 10, fill="both")

acumulador = 0
for row in range(5):
    contenedor_botones.rowconfigure(row, weight=1)
    for column in range(4):
        contenedor_botones.columnconfigure(column, weight=1)
        boton = tk.Button(contenedor_botones, text= botones_texto[acumulador]
                          , bg="#1661D1", fg="#FFFFFF"
                          , font="Roboto 20", bd= 2, width= 4, relief="solid"
                          , highlightbackground="#898787",  highlightthickness=2)
        
        if botones_texto[acumulador]== "C":
            boton.config(bg="#DA0F0F")
        elif botones_texto[acumulador] in ("/", "*", "-", "+"):
            boton.config(bg="#147899")
        elif botones_texto[acumulador] == "+": 
            boton.config(bg="#CF5F14") 
            boton.grid(row=row, column=column, padx= 1, pady= 5, sticky="nsew") 
        elif botones_texto[acumulador] == "=": 
            boton.grid(row=row, column=column, rowspan= 2, padx= 1, pady= 5, sticky="nsew") 
        elif botones_texto[acumulador] == "0": 
            boton.config(width=8) 
            boton.grid(row=row, column=column, rowspan= 2, padx= 1, pady= 5) 
        else:
           boton.grid(row=row, column=column, padx= 1, pady= 5) 
           
        boton.grid(row=row, column=column, padx=0, pady=0, sticky="nsew")
        acumulador +=1 
        
root.mainloop()