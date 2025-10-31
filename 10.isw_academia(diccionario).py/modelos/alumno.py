def agregarAlumno():
    idAlumno = int(input("Digíte el ID del alumno: "))
    nombre = input("Nombre del alumno: ")
    edad = int(input("Edad: "))
    semestre = int(input("Semestre: "))
    carrera = input("Carrera: ")
    
    alumno = {
        "IdAlumno": idAlumno,
        "Nombre": nombre,
        "Edad": edad,
        "Semestre": semestre,
        "Carrera": carrera
    }
    return idAlumno, alumno
    
def mostrarAlumnos(curso):
    print("=== Lista de alumnos ===")
    alumnos = curso["Alumnos"]
    for i, (idAlumno, datos) in enumerate(alumnos.items()):
        print(f"{i}. ID: {idAlumno} - Nombre: {datos["Nombre"]}, Edad: {datos["Edad"]}, Semestre: {datos["Semestre"]}, Carrera: {datos["Carrera"]}")
    return
          
def darBajaAlumno(curso, idAlumno):
    del curso["Alumnos"][idAlumno]
    print("Alumno dado de baja.")
    return curso
    