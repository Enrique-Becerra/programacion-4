# Importación de clases

from modelos.producto import Producto
from modelos.cliente import Cliente


class Restaurante:
    def _init_(self, nombre):
        self.nombre = nombre
        self.productos = []
        self.clientes = []

    # Agregar productos
    def agregar_producto(self, producto):
        self.productos.append(producto)

    # Agregar clientes
    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)

    # Mostrar productos
    def mostrar_productos(self):
        print("\n--- PRODUCTOS DISPONIBLES ---")
        for producto in self.productos:
            print(producto)

    # Mostrar clientes
    def mostrar_clientes(self):
        print("\n--- CLIENTES REGISTRADOS ---")
        for cliente in self.clientes:
            print(cliente)