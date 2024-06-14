from FiguraGeometrica import FiguraGeometrica
from Color import Color
class Rectangulo(FiguraGeometrica, Color):
    def __init__(self, base, altura, color):
        FiguraGeometrica.__init__(self, base, altura)
        Color.__init__(self, color)
    def areaRectangulo(self):
        return self.base * self.altura

base = int(input('Ingrese el valor de base: '))
altura = int(input('Ingrese el valor de la altura: '))
color = input('Ingrese el color: ')    
rectangulo1 = Rectangulo(base, altura, color)

print(f'El área del rectangulo es: {rectangulo1.areaRectangulo()} de color {color}')