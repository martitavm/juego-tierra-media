class Equipamiento:
    def __init__(self, nombre, tipo, potencia):
        self._nombre = nombre
        self._tipo = tipo
        self._potencia = potencia

    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, value):
        self._nombre = value

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, value):
        self._tipo = value
        
    @property
    def potencia(self):
        return self._potencia
    
    @potencia.setter
    def potencia(self, value):
        self._potencia = value

    def __str__(self):
        return f"Nombre: {self._nombre}, Tipo: {self._tipo}, Potencia: {self._potencia}"

    @classmethod
    def es_arma(cls, nombre_arma):
        return nombre_arma

