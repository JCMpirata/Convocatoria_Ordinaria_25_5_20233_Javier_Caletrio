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

    def movimiento_caballo(self, n):
        posibilidades_validas = self.calcular_posibilidades_validas(n)
        print("Posibilidades válidas: ", posibilidades_validas)

        c = sum(posibilidades_validas.values())
        print("Cantidad total de posibilidades válidas: ", c)

    def calcular_posibilidades_validas(self, n):
        if n in self.cantidad_posibilidades:
            return self.cantidad_posibilidades[n]

        if n == 1:
            posibilidades = {nodo.ruta: 1 for nodo in self.nodos}
        else:
            posibilidades = {nodo.ruta: 0 for nodo in self.nodos}
            for nodo in self.nodos:
                for vecino in nodo.vecinos:
                    sub_posibilidades = self.calcular_posibilidades_validas(n - 1)
                    for ruta, cantidad in sub_posibilidades.items():
                        if ruta == nodo.ruta:
                            posibilidades[nodo.ruta] += cantidad
                        else:
                            posibilidades[vecino.ruta] += cantidad

        self.cantidad_posibilidades[n] = posibilidades
        return posibilidades


if __name__ == "__main__":
    movimientos_abra = MovimientoAbra()
    n = int(input("Ingrese un número: "))
    movimientos_abra.movimiento_caballo(n)
