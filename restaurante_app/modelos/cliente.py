# Clase que representa un cliente

class Cliente:
    def _init_(self, nombre, cedula):
        self.nombre = nombre
        self.cedula = cedula

    def _str_(self):
        return f"Cliente: {self.nombre} | Cédula: {self.cedula}"