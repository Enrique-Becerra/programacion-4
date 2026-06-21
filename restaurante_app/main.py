# Archivo principal del programa

from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante

# Crear restaurante
restaurante = Restaurante("Sabor Costeño")

# Crear productos
producto1 = Producto("Hamburguesa", 4.25, "Comida")
producto2 = Producto("Jugo Natural", 2.50, "Bebida")
producto3 = Producto("Pizza", 7.00, "Comida")

# Crear clientes
cliente1 = Cliente("Ricky Jordan", "0939943358")
cliente2 = Cliente("Tatiana Lara", "0939219454")

# Registrar productos
restaurante.agregar_producto(producto1)
restaurante.agregar_producto(producto2)
restaurante.agregar_producto(producto3)

# Registrar clientes
restaurante.agregar_cliente(cliente1)
restaurante.agregar_cliente(cliente2)

# Mostrar información
print("=== SISTEMA DE GESTIÓN DE RESTAURANTE ===")
print(f"Restaurante: {restaurante.nombre}")

restaurante.mostrar_productos()
restaurante.mostrar_clientes()