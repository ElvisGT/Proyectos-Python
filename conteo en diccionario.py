total = {"Elvis":{"manzanas":2,"peras":4},
         "Edgar":{"cocos":1,"fresas":5},
         "Kathy":{"manzanas":1,"peras":3}}

def contador(Atotal,cantidad):
    numero = 0
    for k, i in Atotal.items():
        numero = numero + i.get(cantidad,0)

    return numero


print("Manzanas: " + str(contador(total,"manzanas")))
print("Peras: " + str(contador(total,"peras")))
print("Cocos: " + str(contador(total,"cocos")))
print("Fresas: " + str(contador(total,"fresas")))
        
        
    
    
        
