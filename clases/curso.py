class Curso :
    def __init__(self, nombre, codigo, profesor):
        self.nombre = nombre
        self.codigo = codigo
        self.profesor = profesor

    def __str__(self):
        return f"Nombre: {self.nombre}, Codigo: {self.codigo}, Profesor {self.profesor}"