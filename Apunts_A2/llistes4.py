list_num = [6,9,6]

#DONA ERROR AQUEST ALGORITME
# fer llista duplicats NOVA
for i in range(0,len(list_num)):
    duplicat=False 
    for j in range(i+1,len(list_num)):
        if list_num[i] == list_num[j]:
            duplicat=True
        if duplicat:
            list_num.pop(i)
print(list_num)