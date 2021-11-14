import re

telefonoRegex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")

mo = telefonoRegex.search("El telefono de Elvis es 123-456-7891")
print("Telefono encontrado: ",mo.group())