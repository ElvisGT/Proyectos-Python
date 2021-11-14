#Agregar puntos adelante de texto

texto = """The lines list now contains modified lines that start with stars. But 
pyperclip.copy() is expecting a single string value, not a list of string values. 
To make this single string value, pass lines into the join() method to get a 
single string joined from the list’s strings. Make your program look like the 
following"""

lineas = texto.split('\n')

for i in range(len(lineas)):
    lineas[i] = '* ' + lineas[i]

texto = '\n'.join(lineas)

print(texto)
