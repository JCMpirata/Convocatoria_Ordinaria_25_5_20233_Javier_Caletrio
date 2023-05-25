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

def generar_codigos(nodo, valor='', camino=''):
    nuevo_val = valor + str(nodo.huff)
    if nodo.izquierdo:
        camino = generar_codigos(nodo.izquierdo, nuevo_val, camino)
    if nodo.derecho:
        camino = generar_codigos(nodo.derecho, nuevo_val, camino)

    if not nodo.izquierdo and not nodo.derecho:
        camino += ('%s%s%s\n' % (nodo.simbolo, ' : ', nuevo_val))
    return camino

frecuencias = {
    'T': 0.15,
    'O': 0.15,
    'A': 0.12,
    'E': 0.10,
    'H': 0.09,
    'S': 0.07,
    'P': 0.07,
    'M': 0.07,
    'N': 0.06,
    'C': 0.06,
    'D': 0.05,
    'Z': 0.04,
    'K': 0.03,
    ',': 0.03
}

arbol = crear_arbol(frecuencias)
codigos = generar_codigos(arbol)
codigos = {line.split(' : ')[0]: line.split(' : ')[1][:-1] for line in codigos.split('\n') if line}

def comprimir(mensaje):
    comprimido = ''
    for i in mensaje:
        if i in codigos:
            comprimido += codigos[i]
        else:
            print(f"Error: El carácter '{i}' no se encuentra en el diccionario de códigos.")
    return comprimido


def descomprimir(mensaje):
    clave = ''
    res = ''
    for i in mensaje:
        clave += i
        for k, v in codigos.items():
            if clave == v:
                res += k
                clave = ''
                break
    return res

if __name__ == '__main__':

    mensaje = 'HOLA, SOY TOMAS'
    mensaje_comprimido = comprimir(mensaje)
    mensaje_descomprimido = descomprimir(mensaje_comprimido)

    print('Mensaje original:', mensaje)
    print('Mensaje comprimido:', mensaje_comprimido)
    print('Mensaje descomprimido:', mensaje_descomprimido)
