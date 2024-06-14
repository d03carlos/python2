from FiguraGeometrica import FiguraGeometrica
from Color import Color

class Cuadreado(FiguraGeometrica, Color):
    def __init__(self, lado, color):
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)

    def calcularArea(self):
        return self.base* self.altura

lado =int(input('ingrese el lado delcuadrado:'))
color = input('ingrese el color del cuadrado:')
cuadrado = Cuadreado(lado, color)
print(f'El area del cuadrado es: {cuadrado.calcularArea()} de color: {color}')