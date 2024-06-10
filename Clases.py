class Persona():
    def __init__(self):
        self.nombre = "Hella"
        self.edad = 20
persona1 = Persona()
print(persona1.nombre)
print(persona1.edad)
print('-----------------------------------')
class Personas():
    def __init__(self, nombre, apellidos, edad):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad
personas2 = Personas("Hella", "Garcia", 20)
print(personas2.nombre)
print(personas2.apellidos)
print(personas2.edad)