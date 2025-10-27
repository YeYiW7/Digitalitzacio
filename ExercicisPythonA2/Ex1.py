print('Lliste de 5 números')
num=[1,2,3,4,5]
print(num)

print('Llista de noms')
noms=['Juan', 'Carlos' , 'Luis','Fernando', 'Javi']
print(noms)


print('Llista de noms (afegir i eliminar)')
noms=['Juan', 'Carlos' , 'Luis','Fernando', 'Javi']
noms.append('Jose')
noms.pop(0)
print(noms)

print("Longitud d'una llista")
cont= 0
while cont < len(noms):
    print(noms[cont])
    cont+=1