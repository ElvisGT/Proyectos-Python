cumple = {"Elvis": "3 de sep","Edgar": "26 de mar","Kathy": "30 de sep"}

while True:
    print("Entra el nombre o deja en blanco para finalizar")
    name = input()
    if name =="":
        break

    if name in cumple:
        print(cumple[name] + " es el cumple de " + name)

    else:
        print("No esta registrado, Teclee su dia de cumple")
        dia = input()
        cumple[name] = dia
        print("Base de datos actualizada")
        
