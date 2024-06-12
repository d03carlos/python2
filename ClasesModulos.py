#si queremos importar todo de una clase, se usa *
#from Clases import *
from GetterSetter import Persona

persona1 = Persona("Kayden", "Kross", 30)

print(persona1.get_nombre)
print(persona1.get_apellidos)
print(persona1.get_edad)

