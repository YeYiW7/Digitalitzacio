l=[1,2,3,5,7]
print(l)

#Afegir
l.append(11)
print(l)

# Eliminar
l.pop(4)
print(l)

# Manera 1
for x in l:
    print(x)

# Manera 2
for x in range(len(l)):
    print(l[x])

#Manera 3
cont= 0
while cont < len(l):
    print(l[cont])
    cont+=1


