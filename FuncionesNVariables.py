def suma(*args):
    resultado =0
    for valor in args:
        resultado += valor
    return resultado
print(suma(1,2,3,4,5))