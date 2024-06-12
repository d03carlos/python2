class Persona:
    def __init__(self, nombre, apellidos, edad):
        self._nombre = nombre
        self._apellidos = apellidos
        self._edad = edad
    #getters
    @property
    def get_nombre(self):
        return self._nombre
    @property
    def get_apellidos(self):
        return self._apellidos
    @property
    def get_edad(self):
        return self._edad
    
    #setters
    @get_nombre.setter
    def set_nombre(self, nombre):
        self._nombre = nombre
    @get_apellidos.setter
    def set_apellidos(self, apellidos):
        self._apellidos = apellidos
    @get_edad.setter
    def set_edad(self, edad):
        self._edad = edad


    def __str__(self):
        return f'Nombre: {self.nombre}, Edad: {self.edad}'
Persona1 = Persona('Juan', 'Perez', 28)
#Ingresamos el valor de nombre en setter
Persona1.set_nombre = 'Alena'
#Ingresamos el valor de apellidos en setter
Persona1.set_apellidos = 'Ivanova'
#Ingresamos el valor de edad en setter
Persona1.set_edad = 30
#Imprimimos el valor de nombre en getter
print(Persona1.get_nombre)
#Imprimimos el valor de apellidos en getter
print(Persona1.get_apellidos)
#Imprimimos el valor de edad en getter
print(Persona1.get_edad)

