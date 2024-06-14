from Vehiculo import Vehiculo
class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self.velocidad = velocidad

    def __str__(self):
        return f"Coche {self.color} con {self.ruedas} ruedas y una velocidad de {self.velocidad} km/h"
    
print('================================')
color = input('Introduce el color del coche: ')
ruedas = int(input('Introduce el número de ruedas del coche: '))
velocidad = int(input('Introduce la velocidad del coche: '))

Bicicleta1 = Bicicleta(color, ruedas, velocidad)
print(Bicicleta1.__str__())
