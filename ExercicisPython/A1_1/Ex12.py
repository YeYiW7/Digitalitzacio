text = "Hello Word"
text2= "Hola mon!!!"
comptador = 0

# Assegurar-nos que comparem només fins a la longitud de la cadena més curta
longitud_minima = min(len(text), len(text2))
for i in range(longitud_minima):
    if text[i] == text2[i]:
        comptador += 1
