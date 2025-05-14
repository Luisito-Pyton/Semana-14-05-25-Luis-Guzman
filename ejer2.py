class Animal:
    def hacer_sonido(self):
        print("Sonido genérico")

class Perro(Animal):
    def hacer_sonido(self):
        print("Guau")

class Gato(Animal):
    def hacer_sonido(self):
        print("Miau")

animal = Animal()
perro = Perro()
gato = Gato()

animal.hacer_sonido()
perro.hacer_sonido()
gato.hacer_sonido()
