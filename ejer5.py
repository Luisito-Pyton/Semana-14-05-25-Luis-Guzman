class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class ProductoPerecedero(Producto):
    def __init__(self, nombre, precio, fecha_vencimiento):
        super().__init__(nombre, precio)
        self.fecha_vencimiento = fecha_vencimiento

producto = ProductoPerecedero("Leche", 2500, "2026-09-05") 
print(f"Nombre: {producto.nombre}")
print(f"Precio: ${producto.precio} COP")
print(f"Fecha de vencimiento: {producto.fecha_vencimiento}")
