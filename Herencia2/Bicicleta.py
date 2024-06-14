from Vehiculo import Vehiculo
class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return f"Bicicleta {self.color} con {self.ruedas} ruedas de tipo {self.tipo}"
color = input("Ingrese el color de la bicicleta: ")
ruedas = int(input("Ingrese el número de ruedas de la bicicleta: "))
tipo = input("Ingrese el tipo de bicicleta: ")
print("========================================")
bicicleta = Bicicleta(color, ruedas, tipo)
print(bicicleta.__str__())    
