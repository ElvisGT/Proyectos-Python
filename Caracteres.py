while True:
    print("Teclee su edad")
    edad = input()

    if edad.isdecimal():
        break

    print("Eso no es un numero teclea tu verdadera edad")



while True:
    print("Teclea tu contra")
    contra = input()

    if contra.isalnum():
        break

    print("Solo se acepta letra y numero")
