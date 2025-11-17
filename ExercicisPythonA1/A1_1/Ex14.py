text = "Hola"
inversa = ""

for i in range(len(text)-1, -1, -1):
    inversa += text[i]

print(f"Paraula original: {text}")
print(f"Paraula invertida: {inversa}")
