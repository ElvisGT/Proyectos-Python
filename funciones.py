import random

def suerte(numero):
    if numero == 1:
        return "Campeon"

    elif numero == 2:
        return "Plata"

    else:
        return "Bronce"

r = random.randint(1,3)
fortuna = suerte(r)
print(fortuna)



