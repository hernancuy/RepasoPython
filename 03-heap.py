"""
-HeapSort

Es una tecnica de ordenamiento basada en la estructura de datos llamada monticulo heap, el cual a su vez se basa en arboles binarios balanceados

Monticulo heap. Arbol binario completo con la caracteristica de que los nodos padres son mayores(o menores) que sus hijos

Monticulo heap puede ser representado facilmente mediante arreglos: si el padre se encuentra en posicion i del arreglo, el hijo izquierdo puede ser calculado mediante la expresion 2 * i + 1 y el hijo derecho con 2 * i + 2

[1, 2 , 4, 3, 4, 5, 6, 5]

         1
        /  \.
       2    4  
      / \  / \,
     3   4 5  6
    /
   5 
- Complejidad

Para los tres casos es O(n log(n))

- Pseudocodigo

HeapSort(lista[]):
    listaFinal = []
    Para i = len(lista/2-1) hasta i = 0:
        Heapify(lista, i)
    
    Para i = 0 hasta i = len(lista-1):
        intercambiar primer elemento (el menor de la lista) por el ultimo elemento de la lista
        agregamos el elemento menor al final de la listaFinal
        Eliminamos el elemento menor de lista
        Heapify(lista, 0)
    
    Regresa listaFinal

Heapify(lista[], i):
    Si el nodo i tiene dos hijos:
        j = posicion del menor de los hijos
        Si el padre es mayor que lista[]:
            intercambiar lugares
            Heapify(lista[], j)
    Si el nodo i tiene un hijo:
        Si el nodo hijo es menor que el padre:
            intercambiar lguares
    Regresa lista
"""
def heapify(lista, i):
    #Revisar si el nodo tiene 2 hijos
    if 2 * i + 2 <= len(lista) - 1:
        if lista[2 * i + 1] <= lista[2 * i + 2]:
            min = 2 * i + 1
        else:
            min = 2 * i + 2

        if lista[i] > lista[min]:
            auxiliar = lista[i]
            lista[i] = lista[min]
            lista[min] = auxiliar

            heapify(lista, min)
    
    #Si el nodo tiene un hijo
    elif 2 * i + 1 <= len(lista) - 1:
        if lista[i] > lista[2 * i + 1]:
            auxiliar = lista[i]
            lista[i] = lista[2 * i + 1]
            lista[2 * i + 1] = auxiliar
    
    return lista

def heapsort(lista):
    lista2 =  []
    for i in range(len(lista)//2 - 1, -1, -1):
        lista = heapify(lista, i)
    
    for i in range(0, len(lista)):
        auxiliar = lista[0]
        lista[0] = lista[len(lista) - 1]
        lista[len(lista) - 1] = auxiliar

        lista2.append(auxiliar)

        lista = lista[:len(lista) - 1]

        lista = heapify(lista, 0)
    
    return lista2
    
lista = [20, 19, 5, 6, 15, -4, 0, 10, 7, 3]

print(lista)
print(heapsort(lista))

