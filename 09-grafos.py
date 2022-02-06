"""
Grafos

Consta de dos conjuntos finitos

Matematicamente :
    G = (V(G), E(G))
    G = (V, E)

Donde V(G) o V es el conjunto de vertices del grafo y E(G) o E es el conjunto de aristas.


Data de 1736 originada por Leonard Euler, cuando quiso encontrar el problema a los 7 puentes de konigsberg

Grafo:

 2---0---6---3 
     |\ /|
     | 5 |
     |   |
     1---4

"""

# Clase parar definir vertice

class Vertice:
    #constructor
    def __init__(self, i):
        self.id = i
        self.visitado = False
        self.nivel = -1
        self.vecinos = []
    
    def agregarVecino(self, v):
        if v not in self.vecinos:
            self.vecinos.append(v)

class Grafica:
    #constructor
    def __init__(self):
        self.vertices = {}
        
    def agregaVertice(self, v):
        if v not in self.vertices:
            self.vertices[v] = Vertice(v)

    def agregarArista(self, a, b):
        if a in self.vertices and b in self.vertices:
            self.vertices[a].agregarVecino(b)
            self.vertices[b].agregarVecino(a)

def main():
    
    #define el grafo
    g = Grafica()

    # Crea lista con los id de los vertices
    l = [0, 1, 2, 3, 4, 5, 6]

    #agregar vertices que conforman la grafica
    for v in l:
        g.agregaVertice(v)
    
    #crear aristas

    l = [2, 0, 0, 6, 6, 3, 0, 5, 6, 5, 0, 1, 6, 4, 1, 4]

    for i in range(0, len(l) - 1, 2):
        g.agregarArista(l[i], l[i + 1])

    for v in g.vertices:
        print(v, g.vertices[v].vecinos)

main()