class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Drive!")


class Boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Sail!")


class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Fly!")


car1 = Car("Ford", "Mustang")  # Create a Car object
boat1 = Boat("Ibiza", "Touring 20")  # Create a Boat object
plane1 = Plane("Boeing", "747")  # Create a Plane object

for x in (car1, boat1, plane1):
    x.move()

# !Por que foi usado for x in?
# O for x in é uma estrutura de repetição em Python usada para iterar sobre uma
# sequência de elementos. Neste caso, a sequência é uma tupla (car1, boat1, plane1)
# que contém os três objetos que você criou.
# Explicação detalhada:
# Tupla de objetos:
# (car1, boat1, plane1) é uma tupla que contém os três objetos: car1 (da classe Car),
# boat1 (da classe Boat) e plane1 (da classe Plane).
# Iteração com for:
# O for x in itera sobre cada elemento da tupla, um por vez.
# Na primeira iteração, x será igual a car1.
# Na segunda iteração, x será igual a boat1.
# Na terceira iteração, x será igual a plane1.
# Chamada do método move:
# Dentro do loop, x.move() chama o método move do objeto atual (x).
# Como cada objeto pertence a uma classe diferente (Car, Boat, Plane), o método
# move específico de cada classe é executado:
# Para car1, imprime "Drive!".
# Para boat1, imprime "Sail!".
# Para plane1, imprime "Fly!".
