from clases.universidad import Universidad
from clases.profesor import Profesor
from clases.curso import Curso
from clases.estudiante import Estudiante

universidad = Universidad("Universidad de El Salvador")

profesor_juan = Profesor("Juan Perez", 30, "Masculino",2024811 , "Matematicas")
profesor_maria = Profesor("Maria Lopez",35, "Femenino", 2024922, "Fisica")
profesor_pedro = Profesor("Pedro Ramirez",40, "Masculino", 202433, "Quimica")

curso_matematicas = Curso("Matematicas", "MAT101", profesor_juan)
curso_fisica = Curso("Fisica", "FIS101", profesor_maria)
curso_quimica = Curso("Quimica", "QUI101", profesor_pedro)

universidad.agregar_curso(curso_matematicas)
universidad.agregar_curso(curso_fisica)
universidad.agregar_curso(curso_quimica)

estudiante_carlos = Estudiante("Carlos Perez", 20, "Masculino", 202010101, "Ingenieria en sistemas infomaticos")

print(universidad)
print("-------------------------------------------------------------------------------------------------------------------------------------------------------")
print(estudiante_carlos)
print("-------------------------------------------------------------------------------------------------------------------------------------------------------")
print(profesor_juan)
print("-------------------------------------------------------------------------------------------------------------------------------------------------------")
print(curso_fisica)

curso_nuevo_fisica = Curso("Fisica", 20224012, profesor_maria)
universidad.agregar_curso(curso_nuevo_fisica)