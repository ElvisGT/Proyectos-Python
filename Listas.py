catNames = []

while True:
    print("Escriba el nombre del gato " + str(len(catNames)+1) + " o deje vacio para terminar")
    name = input()

    if name == "":
        break

    catNames = catNames + [name]

for i in catNames:
    print(i)
    
