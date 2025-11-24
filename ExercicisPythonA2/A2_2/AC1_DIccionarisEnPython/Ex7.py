# Exercici 2.10
# Conteig de freqüència d'una llista de paraules
paraules = ["bioinfo", "dades", "python", "bioinfo", "python", "python"]
frequencia = {}


for paraula in paraules:
    frequencia[paraula] = frequencia.get(paraula, 0) + 1


print(frequencia)
# Sortida: {'bioinfo': 2, 'dades': 1, 'python': 3}
