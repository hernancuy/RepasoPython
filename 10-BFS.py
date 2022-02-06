"""
- Busqueda por expansion

Tambien llamada busqueda por anchura o BFS(Breath First Search). 
Esta busqueda comienza por la raiz y se explora por todos los nodos vecinos de este y a continuacion se realiza lo mismo con cada uno de los nodos vecinos hasta recorrer toda la grafica

- Complejidad

O[ |V| + |E| ]


- Pseudocodigo

BFS( Nodo inicial r)
    Marcar el nivel de r como 0
    Crear cola Q
    Agregar r a Q
    Marcar r como visitado
    Mientras Q tenga elementos:
        actual = Extraer un elemento de Q
        Agregar actual a listaFinal
        Para cada nodo en los vecinos de actual:
            Si nodo no ha sido visitado:
                Agregar nodo a Q
                Marcar nodo como visitado
                Nivel del nodo = Nivel de actual + 1
        Regresar listaFinal
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

    def bfs(self, r):
        if r in self.vertices:
            cola = [r]

            self.vertices[r].visitado = True
            self.vertices[r].nivel = 0
            
            print("(" + str(r) + ", " + str(self.vertices[r].nivel) + ")")

            while( len(cola) > 0):
                act = cola[0] 
                cola = cola[1:]

                

                for v in self.vertices[act].vecinos:
                    if self.vertices[v].visitado == False:
                        cola.append(v)
                        self.vertices[v].visitado = True
                        self.vertices[v].nivel = self.vertices[act].nivel + 1

                        print("(" + str(v) + ", " + str(self.vertices[v].nivel) + ")")
def main():
    
    #define el grafo
    g = Grafica()

    # Crea lista con los id de los vertices
    l = [0, 1, 2, 3, 4, 5, 6]

    #agregar vertices que conforman la grafica
    for v in l:
        g.agregaVertice(v)
    
    #crear aristas

    l = [1, 4, 4, 3, 4, 6, 3, 5, 3, 2, 6, 5, 5, 2]

    for i in range(0, len(l) - 1, 2):
        g.agregarArista(l[i], l[i + 1])

    for v in g.vertices:
        print(v, g.vertices[v].vecinos)

    print("\n\n")

    g.bfs(2)

main()