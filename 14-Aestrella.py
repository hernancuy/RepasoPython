"""
- A*

Creado en 1968 por Peter Hart, Nills Nilsson y Bertram Raphael. El algoritmo trabaja con heuristica

Usa una funcion para evaluar el costo de los nodos: f(n) = g(n) + h(n) es el costo o peso hasta el nodo actual y h(n) es el costo estimado (heuristica) para llegar al nodo actual al nodo buscado

- Complejidad

Depende la heuristica. 
Peor caso : Exponencial
COn buena heuristica: linea

- Pseudocodigo

1. Inicializacion:

    a. Crear un conjunto de nodos descubiertos pero no evaluados(conjunto_abierto) que contiene el nodo inicial.
    b. Predecesor nulo para todos los nodos. Asignar una distancia tentativa (g(n)) para cada nodo (0 para el inicial , infinito para los demás)
    c. Asignar a cada nodo una distancia tentativa (f(n)) para llegar al nodo destino (g(inicial) + h(inicial)) para el nodo inicial, "infinito2 para los demas nodos restantes
2. Mientras conjunto_abierto tenga elementos:
    a. actual = nodo del conjunto_abierto con la menor distancia tentativa
    b. Si actual = objetivo. Regresar reconstruir_camino(destino)
    c. Sacar a actual del conjunto_abierto
    d. Cambiar estado de actual a verificado
    e. Para cada vecino actual:
        1. si vecino ya esta visitado, ignorar y pasar al siguietne
        2. Si vecino no esta en conjunto_abierto agregar
        3. Si g(actual) + peso_arista(actual_vecino) + g(vecino) hacer
            predecesor(vecino) = actual
            g(vecino) = g(actual)+peso_arista(acutal(vecino))
            f(vecino)= g(vecino)+ h(vecino)
3. Regresar error


"""