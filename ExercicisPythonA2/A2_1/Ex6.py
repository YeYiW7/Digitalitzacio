"""
6- Invertir una llista
# Inverteix l’ordre dels elements d’una llista sense usar reverse().
list_num = [2, 7, 4, 5, 1, 8, 3, 9, 6, 10]
"""
list_num = [2, 7, 4, 2, 1, 6, 3, 7, 6, 10]

for i in range(0,len(list_num)):
    duplicat=False 
    for j in range(i+1,len(list_num)):
        if list_num[i] == list_num[j]:
            duplicat=True
        if duplicat:
            list_num.pop(i)
print(list_num)        