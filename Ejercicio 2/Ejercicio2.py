import unittest

class Pokemon:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
        print(f"El Pokemon {self.nombre} se ha creado con éxito.")

    def clasificacion(self):
        clasificacion_tipo = {
            "Agua": "PS",
            "Fuego": "Ataque",
            "Planta": "Defensa",
            "Eléctrico": "Ataque Especial",
            "Hielo": "Defensa Especial",
            "Volador": "Velocidad"
        }
        if self.tipo in clasificacion_tipo:
            return clasificacion_tipo[self.tipo]
        else:
            return "Desconocido"

class Pokemon:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
        print(f"El Pokemon {self.nombre} se ha creado con éxito.")

    def clasificacion(self):
        clasificacion_tipo = {
            "Agua": "PS",
            "Fuego": "Ataque",
            "Planta": "Defensa",
            "Eléctrico": "Ataque Especial",
            "Hielo": "Defensa Especial",
            "Volador": "Velocidad"
        }
        if self.tipo in clasificacion_tipo:
            return clasificacion_tipo[self.tipo]
        else:
            return "Desconocido"
        
# Hacer pruebas de la clase Pokemon
class TestPokemon(unittest.TestCase):
        def test_pokemon(self):
            pokemon = Pokemon("Squirtle", "Agua")
            self.assertEqual(pokemon.nombre, "Squirtle")
            self.assertEqual(pokemon.tipo, "Agua")
            self.assertEqual(pokemon.clasificacion(), "PS")
            self.assertEqual(pokemon.__str__(), "Nombre: Squirtle, Tipo: Agua")


if __name__ == '__main__':

    # Crear una lista con Pokemon
    pokemones = [
        Pokemon("Squirtle", "Agua"),
        Pokemon("Charizard", "Fuego"),
        Pokemon("Bulbasaur", "Planta"),
        Pokemon("Pikachu", "Eléctrico"),
        Pokemon("Articuno", "Hielo"),
        Pokemon("Pidgeot", "Volador")
    ]

    # Clasificar los Pokemon
    for pokemon in pokemones:
        print(f"{pokemon.nombre}: {pokemon.clasificacion()}")

    unittest.main()

