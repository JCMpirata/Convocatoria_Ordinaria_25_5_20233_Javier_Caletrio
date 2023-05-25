import random
import string

class Pokemon:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
        print("Se ha creado el Pokémon", self.nombre, "con éxito.")
        self.clasificacion()

    def clasificacion(self):
        temp = self.nombre.split()
        self.codigo = temp[0]
        temp = temp[1]
        self.ataque = temp[0]
        self.defensa= temp[1]
        self.ataqueespecial = temp[2]
        self.defensaespecial = temp[3]

    def __str__(self):
        return "Tipo: " + self.tipo + ", Clasificación: PS, Ataque, Defensa, Ataque Especial, Defensa Especial, Velocidad"


def crear_pokemon(n):
    lista_pokemon = []
    for _ in range(n):
        nombre = ''.join(random.choices(string.ascii_uppercase, k=2))
        tipo = random.choice(["Fuego", "Agua", "Planta", "Eléctrico"])
        pokemon = Pokemon(nombre, tipo)
        lista_pokemon.append(pokemon)
    return lista_pokemon

if __name__ == '__main__':
    n = int(input('Ingrese la cantidad de Pokémon que desea crear: '))
    lista_pokemon = crear_pokemon(n)

    for pokemon in lista_pokemon:
        print(pokemon.clasificacion())
