from datetime import datetime
import unittest

class Pokeball:
    def __init__(self, peso, nombre, precio, fecha_caducidad):
        self.peso = peso
        self.nombre = nombre
        self.precio = precio
        self.fecha_caducidad = datetime.strptime(fecha_caducidad, "%d-%m-%Y")
        print(f"La Pokeball {self.nombre} se ha creado con éxito.")

    def __str__(self):
        return f"Nombre: {self.nombre}, Peso: {self.peso}kg, Precio: ${self.precio}, Fecha de Caducidad: {self.fecha_caducidad.strftime('%d-%m-%Y')}"

# Crear 9 artefactos valiosos de Star Wars
pokeball1 = Pokeball(0.5, "Pokeball", 100, "03-03-2021")
pokeball2 = Pokeball(1, "Masterball", 1000, "26-11-2003")
pokeball3 = Pokeball(2, "Ultraball", 500, "13-12-2020")
pokeball4 = Pokeball(3, "Safari Ball", 200, "30-03-2004")
pokeball5 = Pokeball(4, "Nest Ball", 300, "21-09-2005")

# Pruebas de la clase Pokeball
class TestPokeball(unittest.TestCase):
        def test_pokeball(self):
            pokeball = Pokeball(0.5, "Pokeball", 100, "03-03-2021")
            self.assertEqual(pokeball.peso, 0.5)
            self.assertEqual(pokeball.nombre, "Pokeball")
            self.assertEqual(pokeball.precio, 100)
            self.assertEqual(pokeball.fecha_caducidad, datetime.strptime("03-03-2021", "%d-%m-%Y"))
            self.assertEqual(pokeball.__str__(), "Nombre: Pokeball, Peso: 0.5kg, Precio: $100, Fecha de Caducidad: 03-03-2021")

if __name__ == '__main__':

    # Modificar el precio de las pokeballs
    pokeball1.precio = 200
    pokeball2.precio = 2000
    pokeball3.precio = 1000

    # Mostrar las pokeballs por su precio
    pokeb = [pokeball1, pokeball2, pokeball3, pokeball4, pokeball5]
    pokeb.sort(key=lambda x: x.precio)
    for poke in pokeb:
        print(poke)


    # Mostrar las pokeballs por su fecha de caducidad
    pokeb = [pokeball1, pokeball2, pokeball3, pokeball4, pokeball5]
    pokeb.sort(key=lambda x: x.fecha_caducidad)
    for poke in pokeb:
        print(poke)

    unittest.main()

    

