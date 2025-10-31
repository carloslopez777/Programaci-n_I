def agregarCurso():
    instructor = input("Nombre del instructor: ")
    titulo = input("Título del instructor: ")
    edad = int(input("Edad del instructor: "))
    aula = input("Aula del curso: ")
    
    curso = {
        "Instructor": instructor,
        "Título": titulo,
        "Edad": edad,
        "Aula": aula,
        "Alumnos": {}
    }
    return curso

    
def modificarCurso(curso):
    nuevo_instructor = input("Nuevo instructor: ")
    nuevo_titulo = input("Título del nuevo instructor: ")
    nueva_edad = int(input("Edad del nuevo instructor: "))
    nueva_aula = input("Nueva aula: ")
    
    curso["Instructor"] = nuevo_instructor
    curso["Aula"] = nueva_aula
    curso["Título"] = nuevo_titulo
    curso["Edad"] = nueva_edad
    return curso

def mostrarCursos(cursos):
    print("Lista de cursos: ")
    for i, (nombre, datos) in enumerate(cursos.items()):
        print(f"{i}. {nombre} - {datos}")

