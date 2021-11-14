import random

def randomize():
    numero = random.randint(1,20)
    return numero


intento = 1
usuario_numero = 0
print("Estoy pensando en un numero del 1 al 20")

def pregunta():
    print("Teclee el numero")
    usuario = int(input())
    return usuario


adivina = randomize()


while True:
    usuario_numero = pregunta()
    if usuario_numero == adivina:
        print("Haz adivinado en " + str(intento) + " intentos")
        break
    
    elif usuario_numero < adivina:
        print("Demasiado bajo")
        intento+=1
        
    elif usuario_numero > adivina:
        print("Demasiado alto")
        intento+=1
        
