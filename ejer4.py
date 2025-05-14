class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

class Empleado:
    def trabajar(self):
        print(f"{self.nombre} está trabajando.")

class Deportista:
    def entrenar(self):
        print(f"{self.nombre} está entrenando.")

class EmpleadoDeportista(Persona, Empleado, Deportista):
    def __init__(self, nombre):
        super().__init__(nombre)

persona1 = EmpleadoDeportista("Carlos")
persona1.trabajar()
persona1.entrenar()

print(EmpleadoDeportista.__mro__)
