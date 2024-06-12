from Persona import Persona


class Empleado(Persona):
    def __init__(self,nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self.sueldo = sueldo

empleado1 = Empleado('Kayden', '30', 1000)
print(empleado1.nombre)
print(empleado1.edad)
print(empleado1.sueldo)