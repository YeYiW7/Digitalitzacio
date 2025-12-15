# 2.1 Crear el diccionari
cotxe = {
    "marca": "Toyota",
    "model": "Corolla",
    "any": 2020
}

# Mostrar el valor de la clau "marca"
print(cotxe["marca"])

# 2.2 Afegir una nova clau
cotxe["color"] = "vermell"

# Eliminar la clau "any"
del cotxe["any"]

# Mostrar el diccionari actualitzat
print(cotxe)
