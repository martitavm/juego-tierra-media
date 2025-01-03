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

    @staticmethod
    def es_arma(equipo):
       return True if isinstance(equipo, Arma) else False

    def __str__(self):
        return f"Nombre: {self._nombre}, Tipo: {self._tipo}, Potencia: {self._potencia}"

class Arma(Equipamiento):
    def __init__(self, nombre, tipo, potencia, alcance, probabilidad):
        super().__init__(nombre, tipo, potencia)
        self._alcance = alcance
        self._probabilidad = probabilidad

    @property
    def alcance(self):
        return self._alcance

    @alcance.setter
    def alcance(self, value):
        self._alcance = value

    @property
    def probabilidad(self):
        return self._probabilidad
        
    @probabilidad.setter
    def probabilidad(self, value):
            self._probabilidad = value

    def __str__(self):
        return f"Nombre: {self._nombre}, Tipo: {self._tipo}, Potencia: {self._potencia}, Alcance: {self._alcance}, Probabilidad: {self._probabilidad}."

class Armadura(Equipamiento):
    def __init__(self, nombre, tipo, potencia, defensa, peso):
        super().__init__(nombre, tipo, potencia)
        self._defensa = defensa
        self._peso = peso

    @property
    def defensa(self):
        return self._defensa

    @defensa.setter
    def defensa(self, value):
        self._defensa = value
            
    @property
    def peso(self):
        return self._peso
        
    @peso.setter
    def peso(self, value):
        self._peso = value

    def __str__(self):
        return f"Nombre: {self._nombre}, Tipo: {self._tipo}, Potencia: {self._potencia}, Defensa: {self._defensa}, Peso: {self._peso}."