def esNumero(texto):
    if len(texto) != 12:
        return False

    for i in range(0,3):
        if not texto[i].isdecimal():
            return False
    
    if texto[3] != "-":
        return False
    
    for i in range(4,7):
        if not texto[i].isdecimal():
            return False

    if texto[7] != "-":
        return False

    for i in range(8,12):
        if not texto[i].isdecimal():
            return False

    return True


print(esNumero("123-456-7889"))
print(esNumero("Hola"))

message = "Call me at 415-555-1011 tomorrow. 415-555-9999 is my office, 123-456-7894"

for i in range(len(message)):
    chuk = message[i:i+12]
    if esNumero(chuk):
        print("Numero encontrado: ", chuk)
print("Done")