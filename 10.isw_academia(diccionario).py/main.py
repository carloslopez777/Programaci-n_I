import modelos.curso
from modelos.curso import agregarCurso, modificarCurso, mostrarCursos
from modelos.alumno import agregarAlumno, mostrarAlumnos, darBajaAlumno

cursos = {}

while True:
    op1 = input("""Desea agregar un curso?: """)
    if op1 == "no":
      break
    
    alumnos = []
    
    while True:
       op2 = int(input("""
            1-. Agregar curso
            2-. Modificar curso          
            3-. Agregar alumno
            4-. Dar baja alumno
            5-. Mostrar lista alumnos
            6-. Salir
            """))
       match op2:
            case 1:
               nombre = input("Ingrese el nombre del curso: ")
               curso = agregarCurso()
               cursos[nombre] = curso
               print("Se ha agregado el curso.")
        
            case 2:
               mostrarCursos(cursos)
               idCurso = int(input("Digíte el id del curso: ")) 
               nombre = list(cursos.keys())[idCurso]
               cursos[nombre] = modificarCurso(cursos[nombre])
               print("Curso actualizado")
        
            case 3:
               mostrarCursos(cursos) 
               idCurso = int(input("Digíte el id del curso: "))
               nombre = list(cursos.keys())[idCurso]
               idAlumno, alumno = agregarAlumno()
               cursos[nombre]["Alumnos"][idAlumno] = alumno
               print("Se ha agregado el alumno correctamente")
            
            case 4:
               mostrarCursos(cursos)
               idCurso = int(input("Digíre el ID del curso: "))
               nombre = list(cursos.keys())[idCurso]
               mostrarAlumnos(cursos[nombre])
               idAlumno = int(input("ID del alumno a dar de baja: "))
               cursos[nombre] = darBajaAlumno(cursos[nombre], idAlumno)
               print("Se ha dado de baja al alumno")
        
            case 5:
               mostrarCursos(cursos)
               idCurso = int(input("Digíte el id del curso: ")) 
               nombre = list(cursos.keys())[idCurso]
               mostrarAlumnos(cursos[nombre])
        
            case 6:
               break