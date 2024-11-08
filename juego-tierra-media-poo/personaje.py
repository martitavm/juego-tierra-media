class Personaje:
    def __init__(self, nombre, raza, faccion, ubicacion):
        self._nombre = nombre
        self._raza = raza
        self._faccion = faccion
        self._ubicacion = ubicacion
        self._equipamiento = []
        self._relaciones = []
        self._arma_equipada = {}

    @property
    def nombre(self):  # Getter
        return self._nombre

    @nombre.setter
    def nombre(self, valor):  # Setter
        if isinstance(valor, str):
            self._nombre = valor
        else:
            raise ValueError("El nombre debe ser una cadena de caracteres.")

    @property
    def raza(self):
        return self._raza

    @raza.setter
    def raza(self, valor):
        if isinstance(valor, str):
            self._raza = valor
        else:
            raise ValueError("La raza debe ser una cadena de caracteres.")

    @property
    def faccion(self):
        return self._faccion

    @faccion.setter
    def faccion(self, valor):
        if isinstance(valor, str):
            self._faccion = valor
        else:
            raise ValueError("La facción debe ser una cadena de caracteres.")


def __str__(self):
    return f"Nombre: {self._nombre}, Raza: {self._raza}, Facción: {self._faccion}, Ubicacion: {self._ubicacion}, Equipamiento: {self._equipamiento}, Relaciones: {self._relaciones}, Arma Equipada: {self._arma_equipada}"
