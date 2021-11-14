nombres = ["Elvis","Edgar","Kathy"]

print("Teclee su nombre para chequear si esta en la lista")
name = input()

if name not in nombres:
    print("Su nombre no esta en la lista")

else:
    print("Bienvenido " + name)
