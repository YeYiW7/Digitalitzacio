"""
8- Comprovació de pertinença
# Pregunta a l’usuari un número i comprova si està dins d’una llista.
list_num = [2, 7, 4, 2, 1, 6, 3, 7, 6, 10]
"""
list_num = [2, 7, 4, 2, 1, 6, 3, 7, 6, 10]
print(list_num)

usr= int(input("Introdueix un número d'aquesta llistes per comprovvació de pertinença: "))
if usr in list_num:
    print (f"El número {usr} Sí està en la llista")
else:
    print(f"El número {usr} que has introduit no es valid!")