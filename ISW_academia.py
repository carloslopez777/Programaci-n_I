def agregarCurso():
    nombre = input("Digíte el nombre del curso: ").title()
    aula = input("Digíte el nombre del aula: ")
    instructor = input("Digíte el nombre del instructor: ")
    alumnos = []
    curso = [nombre, aula, instructor, alumnos]
    return curso

def eliminarCurso(cursos, idCurso):
    cursos.pop(idCurso)
    return cursos
    
def modificarCurso(nombre, aula, instructor):
    print("Lista modificada: ")
    
def agregarAlumno():
    alumno = input("Dime el nombre del alumno: ")
    return alumno
 
def darBajaAlumno(curso,idAlumno):
    curso.pop(idAlumno)
    return curso

def mostrarAlumnos(curso):
    alumnos = curso[-1]
    print(f"====({curso[0]})====")
    for i in range (len(alumnos)): 
       print(f"ID:{i} - {alumnos[i]}")

def mostrarCursos(cursos):
    for i in range (len(cursos)):
        print(f"ID:{i}-{cursos[i][0]}")
        
def revisarAlumnos(cursos):
    for curso in cursos:
        print(f"curso: {curso[0]} = alumnos: {curso[-1]}")
        
cursos = []

while True:
    op1 = input("""Desea agregar un curso?: """).lower()
    if op1 == "no":
      break
    
    alumnos = []
    
    while True:
       op2 = int(input("""
            1-. Agregar curso
            2-. Eliminar curso
            3-. Modificar curso, aula o instructor           
            4-. Agregar alumno
            5-. Dar baja alumno
            6-. Mostrar lista alumnos
            7-. Mostrar cursos
            8-. Revisar alumnos
            9-. Salir
            """))
       match op2:
            case 1:
                curso = agregarCurso()
                cursos.append(curso)
                print("Se ha agregado el curso correctamente")
                
            case 2:
                mostrarCursos(cursos)
                idCurso = int(input("Digíte el id del curso" ))
                cursoEditado = eliminarCurso(cursos, idCurso)
                cursos[0] = cursoEditado
                print("Se ha eliminado el curso")
                
            case 3:
                nombre = input("Dame el nombre del curso: ")
                aula = input("Dame el nombre del aula: ")
                instructor = input("Dame el nombre del instructor: ")
                curso = modificarCurso(nombre, aula, instructor)
                nuevo_nombre = input("Ingrese el nuevo nombre del curso: ")
                nueva_aula = input("Ingrese el nuevo nombre de la aula: ")
                nuevo_instructor = input("Ingrese el nuevo nombre del isntructor: ")
                print("Curso actualizado")
            
            case 4:
                mostrarCursos(cursos)
                idCurso = int(input("Digíte el id del curso: "))
                alumno = agregarAlumno()
                cursos[idCurso][-1].append(alumno)
                print("Se ha agregado el alumno correctamente")
            
            case 5:
                mostrarCursos(cursos)
                idCurso = int(input("Digíte el id del curso: "))
                mostrarAlumnos(cursos[idCurso])
                idAlumno = int(input("Digíte el id del alumno a dar de baja: "))
                cursos[idCurso][-1] = darBajaAlumno(cursos[idCurso][-1], idAlumno)
                print("Se ha dado de baja al alumno")
            
            case 6:
                mostrarCursos(cursos)
                idCurso = int(input("Digíte el id del curso: ")) 
                mostrarAlumnos(cursos[idCurso])
                
            case 7:
                mostrarCursos(cursos)
                
            case 8:
                for i in cursos:
                   print(f"{i[0]} (Aula: {i[1]}, Instructor: {i[2]}) → Alumnos: {i[-1]}")
                
            case 9:
                print("===Saliendo del sistema===")
                break
       






