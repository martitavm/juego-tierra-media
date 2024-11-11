from personaje import Personaje


class JuegoTierraMedia:
    def __init__(self, personajes_dict, facciones_dict):
        self._personajes = personajes_dict
        self._facciones = facciones_dict

    @property
    def personajes(self):
        return self._personajes

    @personajes.setter
    def personajes(self, valor):
        self._personajes = valor

    @property
    def facciones(self):
        return self._facciones

    @facciones.setter
    def facciones(self, valor):
        self._facciones = valor

    def registrar_personaje(self):
        """
            Registra un nuevo personaje en el diccionario general de personajes.

            Este método permite añadir la información de un nuevo personaje en el diccionario `personajes`, con los siguientes
            atributos: nombre, raza, facción, ubicación, equipamiento y relaciones. Los atributos `equipamiento` y `relaciones`
            se inicializan como listas vacías y  `arma_equipada` como un diccionario.
            :param personajes: dict - Diccionario de objetos de clase personajes.
            :return: No devuelve nada.
        """
        try:
            nombre = input("Introduce el nombre del personaje que desea registrar: ")
            raza = input("Introduce la raza que desea registrar: ")
            faccion = input("Introduce la faccion que desea registrar: ")
            ubicacion = input("Introduce la ubicacion que desea registrar: ")

            personaje = Personaje(nombre, raza, faccion, ubicacion)

            # Agregamos el personaje al diccionario, usando su nombre como clave
            self._personajes[nombre] = personaje

            print(f"El personaje {personaje.nombre} ha sido registrado exitosamente. ")
        except ValueError as e:
            print(f"Error: {e}")


    def anadir_equipamiento(self, nombre_personaje, nombre_arma):
        """
        Añade un arma al equipamiento de un personaje si el personaje existe y no tiene ya el arma.

        Esta función recibe el nombre de un personaje y un arma. Primero, comprueba que el personaje
        está en la lista de personajes, si no, muestra un mensaje. Luego verifica si el personaje
        ya tiene el arma. Si no la tiene, la añade al equipamiento.

        :param nombre_personaje: Nombre del personaje al que se le quiere añadir el arma.
        :param nombre_arma: Nombre del arma que se quiere añadir al equipamiento.
        :return: No devuelve nada, solo imprime mensajes según la situación.

        Nota: Es importante que los nombres estén bien escritos para evitar errores de búsqueda.
        """
        try:
            # Se comprueba si el personaje existe. Si existe se llama a la función anadir_equipamiento. Si no existe, se avisa.
            if nombre_personaje in self._personajes:
                # Obtiene el objeto del personaje y llama a su metodo para añadir el arma.
                personaje = self._personajes[nombre_personaje]
                personaje.anadir_equipamiento(nombre_arma)
            else:
                print(
                    f"\n ---> El personaje {nombre_personaje} no existe (comprueba que lo has escrito correctamente). <---\n")
                return

        except Exception as e:
            print(f"{e}")

    def buscar_personaje_equipamiento(self, nombre_equipo):
        """
        Función que muestra los personajes que tienen en su equipamiento el
        arma pasada como parámetro
        :param str nombre_equipo: Nombre del equipo a buscar
        :return: Lista con los personajes que tienen el arma en su equipamiento.
        """
        lista_personaje_equipado = []
        for pnj in self.personajes:
            for equipo in self.personajes[pnj].equipamiento:
                if nombre_equipo == equipo.nombre:
                    lista_personaje_equipado.append(pnj)

        if len(lista_personaje_equipado) == 0:
            print(f"Ningún personaje tiene {nombre_equipo}")
        else:
            print(f"Personajes con {nombre_equipo.capitalize()}: \n{lista_personaje_equipado}")
        return

    def mostrar_personajes(self):
        """
        Función que recorre un diccionario de objetos personajes y muestra todos sus datos.
        :return: Datos del diccionario recorrido.
        """
        for pnj in self.personajes:
            print(f"Personaje: {pnj}")
            print(f"--> Datos: {self.personajes[pnj]}")
            print("----------------------------------")
        return


    def listar_personaje_faccion(self):
        """
            Muestra todos los personajes que pertenecen a una facción específica.

            Solicita al usuario introducir el nombre de una facción y luego muestra una lista de personajes que
            pertenecen a esa facción. Si la facción introducida no contiene personajes o no existe, muestra un
            mensaje indicándolo.
            :param personajes: dict - Diccionario de personajes, donde cada clave es un nombre de personaje y el valor es un diccionario
            con los atributos del personaje.
            :return: No devuelve nada
        """

        try:
            nombre_faccion = input("Ingrese el nombre de la faccion que desea listar: ")
            personajes_en_faccion = [
                nombre for nombre, personaje in self._personajes.items()
                if personaje.faccion == nombre_faccion
            ]

            # Comprobamos si existe la facción escrita por el usuario, si existe muestra los personajes de esa facción y si no existe saltará un aviso
            if personajes_en_faccion:
                for nombre in personajes_en_faccion:
                    print(nombre)
            else:
                print("No hay personajes en esa facción o no existe.")

        except Exception as e:
            print(f"Error: {e}")

    @staticmethod
    def salir():
        print("Has finalizado el juego")
        exit(0)

    def establecer_relacion(self, personaje, personaje_relacion, tipo, nivel_confianza):
        """
        Establece una relación entre dos personajes si ambos existen en el juego.

        :param personaje: Objeto del personaje que establece la relación.
        :param personaje_relacion: Objeto del personaje con el cual se establece la relación.
        :param tipo: Tipo de relación ('Amigo', 'Enemigo', 'Neutral').
        :param nivel_confianza: Nivel de confianza en la relación (1 a 10).
        """

        personaje.establecer_relaciones(personaje_relacion, tipo, nivel_confianza)


    def nueva_ubicacion(self,nombre_personaje,nueva_ubicacion):

             nombre_personaje.nueva_localizacion(nueva_ubicacion)






