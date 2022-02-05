"""
BubbleSort(list[]):
  n = longitud de lista - 1
  Para i = 1 hasta n:
    Para j = 0 hasta n - 1:
      Si(lista[j] > lista[j+1]):
        temp = lista[j]
        lista[j] = lista[j+1]
        lista[j+1] = temp
  Regresa lista 
"""
def bubbleSort(lista):
  n = len(lista)
  for i in range(1, n):
    for j in range(0, n-1):
      if lista[j]>lista[j+1]:
        temp = lista[j]
        lista[j] = lista[j+1]
        lista[j+1] = temp
  return lista

lista = [20, 19, 5, 6, 15, -4, 0, 10, 7, 3]

print(lista)
print(bubbleSort(lista))