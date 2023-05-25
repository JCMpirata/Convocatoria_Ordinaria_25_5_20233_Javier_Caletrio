class Nodo:
    def __init__(self, ruta):
        self.ruta = ruta
        self.vecinos = []

    def agregar_vecino(self, vecino):
        self.vecinos.append(vecino)


class MovimientoAbra:
    def __init__(self):
        self.nodos = []
        self.cantidad_posibilidades = {}

        # Crear nodos
        for i in range(10):
            self.nodos.append(Nodo(i))

        # Agregar vecinos a los nodos
        self.nodos[0].agregar_vecino(self.nodos[6])
        self.nodos[0].agregar_vecino(self.nodos[8])

        self.nodos[1].agregar_vecino(self.nodos[7])
        self.nodos[1].agregar_vecino(self.nodos[9])

        self.nodos[2].agregar_vecino(self.nodos[4])
        self.nodos[2].agregar_vecino(self.nodos[8])

        self.nodos[3].agregar_vecino(self.nodos[9])
        self.nodos[3].agregar_vecino(self.nodos[0])
        self.nodos[3].agregar_vecino(self.nodos[4])

        self.nodos[4].agregar_vecino(self.nodos[3])
        self.nodos[4].agregar_vecino(self.nodos[9])
        self.nodos[4].agregar_vecino(self.nodos[0])

        self.nodos[6].agregar_vecino(self.nodos[1])
        self.nodos[6].agregar_vecino(self.nodos[7])
        self.nodos[6].agregar_vecino(self.nodos[0])

        self.nodos[7].agregar_vecino(self.nodos[2])
        self.nodos[7].agregar_vecino(self.nodos[6])

        self.nodos[8].agregar_vecino(self.nodos[1])
        self.nodos[8].agregar_vecino(self.nodos[3])

        self.nodos[9].agregar_vecino(self.nodos[2])
        self.nodos[9].agregar_vecino(self.nodos[4])

    
