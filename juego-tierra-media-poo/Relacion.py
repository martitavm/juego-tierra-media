class Relacion:

    def __init__(self, personaje ,tipo,nivel_confianza):

        self._personaje = personaje
        self._tipo = tipo
        self._nivel_confianza = nivel_confianza


    @property
    def personaje(self):
         return self._personaje

    @personaje.setter
    def personaje(self, personaje):
        self._personaje = personaje

    @property
    def tipo(self):
          return self._tipo

    @tipo.setter
    def tipo(self, tipo):
        if tipo == 'Amigo'and tipo == 'Enemigo'and tipo == 'Neutral':
          self._tipo = tipo
        else:
         raise ValueError("EL tipo tiene que ser: Amigo, Enemigo, Neutral")

    @property
    def nivel_confianza(self):
        return self._nivel_confianza

    @nivel_confianza.setter
    def nivel_confianza(self, nivel_confianza):
        if nivel_confianza < 1 or nivel_confianza > 10:
         self._nivel_confianza = nivel_confianza
        else:
            raise ValueError("EL nivel de confianza tiene que ser: 1-10")