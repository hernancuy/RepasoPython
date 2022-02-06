"""
- QuickSort

Algoritmo del tipo divide y venceras que consiste en elegir un pivote y particionar la lista de numeros tomando dicho pivote como punto central.

Hay varias versiones de QuickSort que cambian la forma de elegir el pivote:

1. Elegir primer elemento de la lista como pivote
2. Elegir el ultimo elemento de la lista como pivote
3. Elegir el punto medio como pivote
4. Elegir un pivote aleatorio

- Complejidad 

Peor caso : O(n^2)
Mejor caso y caso pormedio O(n log(n))

- Pseudocodigo

QuickSort(lista):
    #Caso base
    Si longitud(lista) <= 1:
        Regresa lista 
    #Caso Recursivo
    Si no:
        pivote = ultimo elemento de la lista
        lista1 = elementos de la lista menores o iguales al pivote
        lista2 = elementos de la lista mayores al pivote

        lista1 = quickSort(lista1)
        lista2 = quickSort(lista2)

        Regresa lista1 concatenada con el pivote y lista2


"""
def quickSort(lista):
    #Caso Base
    if len(lista) <= 1:
        return lista
    #Caso Recursivo
    pivote = lista.pop()

    lista1 = []
    lista2 = []
    
    for e in lista:
        if e <= pivote:
            lista1.append(e)
        else:
            lista2.append(e)
    
    lista1 = quickSort(lista1)
    lista2 = quickSort(lista2)

    return lista1 + [pivote] + lista2


lista = [20, 19, 5, 6, 15, -4, 0, 10, 7, 3]

print(lista)
print(quickSort(lista))
