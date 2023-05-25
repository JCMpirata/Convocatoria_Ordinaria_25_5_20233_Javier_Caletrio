class Nodo:
    def __init__(self, ruta):
        self.ruta = ruta
        self.vecinos = []

    def agregar_vecino(self, vecino):
        self.vecinos.append(vecino)


