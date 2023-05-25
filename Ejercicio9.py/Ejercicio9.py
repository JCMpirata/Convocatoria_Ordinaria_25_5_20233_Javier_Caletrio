class Tarea:
    def __init__(self, nombre, duracion):
        self.nombre = nombre
        self.duracion = duracion

# Definir las tareas y sus duraciones
tareas = {
    'A': 20,
    'B': 5,
    'C': 40,
    'D': 10,
    'E': 5,
    'F': 10,
    'G': 20,
    'H': 25,
    'I': 35,
    'J': 25,
    'K': 15,
    'L': 5,
    'M': 25
}

# Definir las dependencias entre tareas
dependencias = {
    'A': [],
    'B': [],
    'C': [],
    'D': ['A'],
    'E': ['D'],
    'F': ['D'],
    'G': ['B'],
    'H': ['C', 'G'],
    'I': ['H'],
    'J': ['H', 'I'],
    'K': [],
    'L': ['K'],
    'M': ['E', 'F', 'J', 'L']
}

# Construir el grafo de tareas y asignar las duraciones
grafo = {}
tareas_obj = {}

for tarea, duracion in tareas.items():
    tareas_obj[tarea] = Tarea(tarea, duracion)
    grafo[tarea] = {}

for tarea, dependencias_tarea in dependencias.items():
    for dependencia in dependencias_tarea:
        grafo[tarea][dependencia] = tareas_obj[dependencia].duracion
        grafo[dependencia][tarea] = tareas_obj[dependencia].duracion

# Función recursiva para encontrar el camino más corto utilizando el algoritmo de Dijkstra
def dijkstra(grafo, inicio, destino, visitados, distancias, previo):
    visitados.add(inicio)
    if inicio == destino:
        return
    for vecino, peso in grafo[inicio].items():
        nueva_distancia = distancias[inicio] + peso
        if nueva_distancia < distancias[vecino]:
            distancias[vecino] = nueva_distancia
            previo[vecino] = inicio
    siguiente = None
    min_distancia = float('inf')
    for nodo, distancia in distancias.items():
        if nodo not in visitados and distancia < min_distancia:
            siguiente = nodo
            min_distancia = distancia
    if siguiente:
        dijkstra(grafo, siguiente, destino, visitados, distancias, previo)

if __name__ == '__main__':

    # Inicializar los diccionarios de distancias y previos
    distancias = {nodo: float('inf') for nodo in grafo}
    previo = {nodo: None for nodo in grafo}

    # Establecer la duración mínima de la misión como 100 (100 minutos disponibles)
    duracion_minima = 100

    # Aplicar el algoritmo de Dijkstra para encontrar el camino más corto desde el inicio hasta la facturación
    dijkstra(grafo, 'A', 'M', set(), distancias, previo)

    # Obtener la duración total del camino más corto
    tiempo_total = distancias['M']

    # Verificar si el líder llega a facturar a tiempo dentro de los 100 minutos disponibles
    llega_a_facturar_a_tiempo = tiempo_total <= duracion_minima

    # Imprimir la duración mínima de la misión, el tiempo total y si llega a facturar a tiempo
    print("Duración mínima de la misión:", tiempo_total)
    print("¿Llega a facturar a tiempo?", llega_a_facturar_a_tiempo)

    # Reconstruir el camino más corto desde el inicio hasta la facturación
    camino = []
    nodo_actual = 'M'
    while nodo_actual:
        camino.insert(0, nodo_actual)
        nodo_actual = previo[nodo_actual]

    # Imprimir la secuencia óptima de tareas
    print("Secuencia óptima de tareas:")
    for tarea in camino:
        print(tarea)

