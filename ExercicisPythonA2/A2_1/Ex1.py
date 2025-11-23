
# Crea una llista amb 5 números enters i mostra-la per pantalla
llista_numeros = [10, 20, 30, 40, 50]
print("Llista de números:", llista_numeros)

# Accedir a elements
noms = ["Anna", "Pere", "Maria", "Joan", "Laura"]
print("Primer element:", noms[0])
print("Últim element:", noms[-1])

# Afegir i eliminar elements
print("Llista original:", noms)
noms.append("Carles")  # Afegeix al final
print("Després d'afegir 'Carles':", noms)
element_eliminat = noms.pop(0)  # Elimina el primer
print(f"Després d'eliminar '{element_eliminat}':", noms)


# Longitud d'una llista
print(f"Longitud de la llista de números: {len(llista_numeros)}")
print(f"Longitud de la llista de noms: {len(noms)}")
