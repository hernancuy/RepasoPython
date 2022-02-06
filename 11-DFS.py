"""
- Busqueda por profundidad

Tambien llamada busqueda por profundidad o DFS (Depth First Search).

Consiste en ir recorriendo todos y cada uno de los nodos que va encontrando, de forma recurrente.
Cuando ya no quedan más nodos que visitar de dicho camino, regresa, repitiendo el mismo proceso con cada uno de los hermanos del nodo ya procesado.


- Complejidad

- Pseudocodigo

DFS(nodo r)
    Marcar r como visitado
    Para cada nodo en vecinos de r:
        Si nodo no ha sido visitado:
            Marcar a r como padre de nodo 
            DFS(nodo)
    Regresa

"""

# Clase parar definir vertice

class Vertice:
    #constructor
    def __init__(self, i):
        self.id = i
        self.visitado = False
        self.nivel = -1
        self.padre = None
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

    def dfs(self, r):
        if r in self.vertices:
            self.vertices[r].visitado = True

            for nodo in self.vertices[r].vecinos:
                if self.vertices[nodo].visitado == False:
                    self.vertices[nodo].padre = r
                    print("(" + str(nodo) + ", " + str(r) + ")")
                    self.dfs(nodo)



def main():
    
    #define el grafo
    g = Grafica()

    # Crea lista con los id de los vertices
    l = [0, 1, 2, 3, 4, 5, 6]

    #agregar vertices que conforman la grafica
    for v in l:
        g.agregaVertice(v)
    
    #crear aristas

    l = [1, 2, 1, 5, 2, 3, 2, 5, 3, 4, 4, 5, 4, 6]

    for i in range(0, len(l) - 1, 2):
        g.agregarArista(l[i], l[i + 1])

    print("(1, NULL)")
    g.dfs(1)
    

main()