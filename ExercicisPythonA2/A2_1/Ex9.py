"""
9- Ordenació (deixar pel final)
Ordenar una llista per exemple  list_num=[4,7,2,9,5,6]
# Ordena una llista de números de menor a major.
list_num = [2, 7, 4, 2, 1, 6, 3, 7, 6, 10]
Intenta fer el teu algoritme cercant els mínims de la llista
Cerca diferents algoritmes d’ordenació
Implementa amb l’algoritme d’ordenació “Selection Sort”
Implementa amb l’algoritme d’ordenació “Insertion Sort”
"""

list_num = [2, 7, 4, 2, 1, 6, 3, 7, 6, 10]
print("Llista original:", list_num)
llista_ordenada = sorted(list_num)
print("Llista ordenada (amb sorted):", llista_ordenada)

def selection_sort(llista):
    llista = llista.copy() 
    n = len(llista)
    
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if llista[j] < llista[min_idx]:
                min_idx = j
        
        llista[i], llista[min_idx] = llista[min_idx], llista[i]
    
    return llista

def insertion_sort(llista):
    llista = llista.copy()
    n = len(llista)
    
    for i in range(1, n):
        clau = llista[i]
        j = i - 1
        while j >= 0 and llista[j] > clau:
            llista[j + 1] = llista[j]
            j -= 1
        
        llista[j + 1] = clau
    
    return llista


print("Llista original:", list_num)
print("Selection Sort:", selection_sort(list_num))
print("Insertion Sort:", insertion_sort(list_num))
print("Llista original sense canvis:", list_num) 