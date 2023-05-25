class Nodo:
    def __init__(self, frecuencia, simbolo, izquierdo=None, derecho=None):
        self.frecuencia = frecuencia
        self.simbolo = simbolo
        self.izquierdo = izquierdo
        self.derecho = derecho
        self.huff = ''

def crear_arbol(frecuencias):
    nodos = [Nodo(frecuencia, simbolo) for simbolo, frecuencia in frecuencias.items()]
    while len(nodos) > 1:
        nodos = sorted(nodos, key=lambda x : x.frecuencia)

        izquierdo = nodos[0]
        derecho = nodos[1]

        izquierdo.huff = 0
        derecho.huff = 1

        nuevo_nodo = Nodo(izquierdo.frecuencia + derecho.frecuencia, izquierdo.simbolo + derecho.simbolo, izquierdo, derecho)

        nodos.remove(izquierdo)
        nodos.remove(derecho)
        nodos.append(nuevo_nodo)
    return nodos[0]