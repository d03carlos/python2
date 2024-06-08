import random
print("Bienvenido al juego de adivinar el numero")
numeroUsuario = int(input("Ingrese un numero del 1 al 10: "))
contador =0
numeroAleatorio = random.randint(1,10)
while numeroUsuario != numeroAleatorio:
    #print("El numero es incorrecto")
    
    if numeroUsuario > numeroAleatorio:
        print("El numero es menor")
    elif numeroUsuario < numeroAleatorio:
        print("El numero es mayor")
    numeroUsuario = int(input("Ingrese un numero del 1 al 10: "))
    contador += 1
print(f"El aleatorio es: {numeroAleatorio}")
print(f"El numero de intentos es: {contador}")