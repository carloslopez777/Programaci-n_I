import tkinter as tk

#Ventana principal
root = tk.Tk()
root.title("Calculadora")
root.geometry("305x480")

#Agregar widgets
botones_texto = (
                "C", "/", "*", "-",
                "7", "8", "9", "+",
                "4", "5", "6", "",
                "1", "2", "3", "=",
                "0", ".", "", "")

def click_botones(valor):
    if valor == "=":
        try:
            expresion = resultado.get() 
            evaluacion = eval(expresion)
            resultado.delete(0,tk.END)   
            resultado.insert(tk.END,str(evaluacion))
            historico.config(text=expresion + "=")
        except Exception as e:
            resultado.delete(0,tk.END)
            resultado.insert(tk.END, "Error")
            resultado.config(text="")
    elif valor == "C":
          resultado.delete(0,tk.END)
          resultado.insert(tk.END)
          historico.config(text="")
    else:
        current_text = resultado.get()
        resultado.delete(0,tk.END)
        resultado.insert(tk.END, current_text + valor)

historico = tk.Label(root, bg="#F2F2F2", font="Roboto 14"
                     , width= 15, bd= 0, justify="right")

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
                          , font="Roboto 20", bd= 0, width= 4, 
                          command= lambda b = botones_texto[acumulador]:click_botones(b))
        
        if botones_texto[acumulador] != "":    
        
            if botones_texto[acumulador]== "C":
                boton.config(height=2, bg="#DA0F0F")
            elif botones_texto[acumulador] in ("/", "*", "-", "+"):
                boton.config(height=2, bg="#147899")
            
            if botones_texto[acumulador] == "+": 
                boton.config(height=3) 
                boton.grid(row=row, column=column, padx= 1, pady= 1, sticky="nsew") 
            elif botones_texto[acumulador] == "=": 
                boton.config(height=3, bg="#CF5F14")
                boton.grid(row=row, column=column, rowspan= 2, padx= 1, pady= 1, sticky="nsew") 
            elif botones_texto[acumulador] == "0": 
                boton.config(width=8) 
                boton.grid(row=row, column=column, rowspan= 2, padx= 1, pady= 1) 
            else:
                boton.grid(row=row, column=column, padx= 1, pady= 1) 
            
        #boton.grid(row=row, column=column, padx=0, pady=0, sticky="nsew")
        acumulador +=1 
        
root.mainloop()