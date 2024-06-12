class Persona:
    def __init__(self, nombre, apellidos, edad):
        self._nombre = nombre
        self.apellidos = apellidos
        self.edad = edad
    #getters
    @property
    def get_nombre(self):
        return self._nombre
    #setters
    @get_nombre.setter
    def set_nombre(self, nombre):
        self._nombre = nombre

    def __str__(self):
        return f'Nombre: {self.nombre}, Edad: {self.edad}'
Persona1 = Persona('Juan', 'Perez', 28)
#Ingresamos el valor de nombre en setter
Persona1.set_nombre = 'Alena Ivanova'
print(Persona1.get_nombre)
