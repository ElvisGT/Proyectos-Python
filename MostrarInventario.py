inventary = {"Flechas":12,"Ropa":5,"Soga":4,"Platos":2,"Espada":1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def mostrarInv(inventario):
    total= 0
    for k,v in inventary.items():
        print(str(v) + " " + k)
        total+=v
    print("El total de items es " + str(total))

mostrarInv(inventary)

def addToInventory(inventary, addedItems):
    for i in dragonLoot:
        inventary.setdefault(i,1) 
    

inv = addToInventory(inventary, dragonLoot)
mostrarInv(inv)



    
