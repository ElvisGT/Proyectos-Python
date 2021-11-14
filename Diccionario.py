dire = {"Elvis":"22","Edgar":"14"}

def practica():
    while True:
        print("Teclea el nombre del la persona o deja en blanco para salir")
        name = input()
        if name == "":
            break
        if name in dire:
            print(name + " tiene una edad de " + dire[name])

        else:
            print("No se encuentra en la lista")
            print("Tecle su fecha para agregarlo")
            edad = input()
            dire[name] = edad


practica()
            


