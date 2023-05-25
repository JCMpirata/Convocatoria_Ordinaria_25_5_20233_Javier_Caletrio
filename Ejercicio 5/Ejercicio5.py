class MovimientoAbra:
    def __init__(self):
        self.matrix = [
            [0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
            [0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 1, 0, 0, 1],
            [0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
            [1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 1, 0, 0, 0, 0]
        ]

    def movimiento_caballo(self, n):
        posibilidades_validas = self.matrix_power(n)
        print("Posibilidades validas: ", posibilidades_validas)

        c = self.sumar_posibilidades_validas(posibilidades_validas)
        print("Cantidad total de posibilidades validas: ", c)

    def matrix_power(self, n):
        if n == 0:
            return [[1 if i == j else 0 for j in range(10)] for i in range(10)]
        elif n == 1:
            return self.matrix.copy()
        else:
            half_power = self.matrix_power(n // 2)
            result = self.multiply_matrices(half_power, half_power)
            if n % 2 == 1:
                result = self.multiply_matrices(result, self.matrix)
            return result

    def multiply_matrices(self, matrix1, matrix2):
        result = [[0] * 10 for _ in range(10)]
        for i in range(10):
            for j in range(10):
                for k in range(10):
                    result[i][j] += matrix1[i][k] * matrix2[k][j]
        return result

    def sumar_posibilidades_validas(self, matrix):
        c = 0
        for i in range(10):
            for j in range(10):
                c += matrix[i][j]
        return c


if __name__ == "__main__":
    movimientos_abra = MovimientoAbra()
    n = int(input("Ingrese un numero: "))
    movimientos_abra.movimiento_caballo(n)
