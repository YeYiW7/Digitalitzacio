"""
5- Eliminar duplicats
 # Donada una llista amb elements repetits, crea una nova llista sense duplicats.  Crear una llista Nova
list_num = [2, 7, 4, 2, 1, 6, 3, 7, 6, 10]
"""
list_num = [2, 7, 4, 2, 1, 6, 3, 7, 6, 10]
list_nova = list(set(list_num))
print(list_nova)
