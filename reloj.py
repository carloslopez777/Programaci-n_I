import time

for horas in range(24):
    for minutos in range(60):
        for segundos in range(60):
         hora_formateada = f"{horas:02d}:{minutos:02d}:{segundos:02d}"  
         print(hora_formateada)
time.sleep(1)
    
    
