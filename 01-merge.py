"""

- Merge Sort:

De tipo divide y vencerás, divide la lista de numeros de entrada a la mitad, llama a si mismo (es recursivo) para cada una de las mitades y, finalmente junta las dos mitades ya ordenadas

- Complejidad: 

Para los tres casos es O(n log(n))

- Pseudocodigo:

MergeSort(lista[]):
    # Caso Base
    Si longitud(lista) == 1:
        Regresa lista
    # Caso Recursivo
    Si no:
        1: Encuentra el punto medio que divide la lista en dos partes
        2: Llama a la funcion MergeSort para la parte izquierda de la lista
        3: Llama a la funcion MergeSort para la parte derecha de la lista
        4: Junta las dos partes obtenidos en los pasos 2 y 3 con la funcion Merge
            Regresa listaOrdenada
    
    Merge(lista1[], lista2[]):
        Mientras lista1 y lista2 tengan elementos:
            Si lista1[0] < lista2 [0]:
                Agrega lista1[0] al final de listaFinal
                Elimina lista1[0] de la lista1
            Si no 
                Agrega lista2[0] al final de la listaFinal
                Elimina lista2[0] de lista1
        Si quedaron elementos en lista1 o lista2:
            Agrega elementos a lista final
    Regresa lista final
    
"""
def merge(lista1, lista2):
    lista3=[]
    while(len(lista1) > 0 and len(lista2) > 0 ):
        if lista1[0] < lista2[0]:
            lista3.append(lista1[0])
            lista1 = lista1[1:]
        else:
            lista3.append(lista2[0])
            lista2 = lista2[1:]
    
    if len(lista1) > 0:
        lista3 = lista3 + lista1
    if len(lista2) > 0:
        lista3 = lista3 + lista2

    return lista3

def mergeSort(lista):
    #Caso Base
    if len(lista) == 1:
        return lista
    #Caso Recursivo
    listaIzquierda = lista[:len(lista)//2]
    listaDerecha = lista[len(lista)//2:]

    listaIzquierda = mergeSort(listaIzquierda)
    listaDerecha = mergeSort(listaDerecha)

    return merge(listaIzquierda, listaDerecha)

lista = [20, 19, 5, 6, 15, -4, 0, 10, 7, 3]

print(lista)
print(mergeSort(lista))