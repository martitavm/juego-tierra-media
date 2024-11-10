from equipamiento import Arma
class Personaje:
    def __init__(self, nombre, raza, faccion, ubicacion):
        self._nombre = nombre
        self._raza = raza
        self._faccion = faccion
        self._ubicacion = ubicacion
        self._equipamiento = []
        self._relaciones = []
        self._arma_equipada = None

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

    @property
    def ubicacion(self):
        return self._ubicacion

    @ubicacion.setter
    def ubicacion(self, valor):
        if isinstance(valor, str):
            self._ubicacion = valor
        else:
            raise ValueError("La facción debe ser una cadena de caracteres.")

    @property
    def equipamiento(self):
        return self._equipamiento

    @equipamiento.setter
    def equipamiento(self, valor):
        self._equipamiento = valor


    @property
    def relaciones(self):
        return self._relaciones

    @relaciones.setter
    def relaciones(self, valor):
        self._faccion = valor
        
    @property
    def arma_equipada(self):
        return self._arma_equipada
    
    @arma_equipada.setter
    def arma_equipada(self, value):
        self._arma_equipada = value

    def __str__(self):
        # Creamos una variable para pasar a string los objetos que contiene la lista equipamiento. Se recorre la lista y se hace casting a string a cada arma.
        equipamiento_str = ""
        for weapon in self._equipamiento:
            equipamiento_str += f"[{str(weapon)}]"

        return f"Nombre: {self._nombre}, Raza: {self._raza}, Facción: {self._faccion}, Ubicacion: {self._ubicacion}, Equipamiento: {equipamiento_str}, Relaciones: {self._relaciones}, Arma Equipada: [{self._arma_equipada}]"

    # Metodo añadir equipamiento

    def anadir_equipamiento(self, nombre_arma):
        """
        Añade un arma al equipamiento de un personaje.

        Este metodo busca el arma indicada en una lista predeterminada y, si existe y el personaje aún no la tiene, la añade al
        equipamiento del personaje. Si el arma no existe, pregunta al usuario si desea que un
        moderador la añada o si quiere sugerirla.

        Al ejecutar este metodo:
          1. Busca el arma por el nombre.
          2. Si el arma no está, pregunta si el usuario es moderador o si desea sugerir el arma.
          3. Verifica si el personaje ya tiene esa arma. Si ya está, no la añade de nuevo.
          4. Si está bien, añade el arma al equipamiento.

        :param nombre_arma: El nombre del arma que se quiere añadir al personaje.
        :return: No devuelve nada, pero muestra mensajes con información sobre el proceso.
        """

        try:

            # Se busca el arma por el nombre que se ha pasado como parametro.
            arma = UtilidadesPersonaje.buscar_arma(nombre_arma)

            # Si no se encuentra el arma, se avisa al usuario.
            if not arma:
                print(f"\n ---> El arma {nombre_arma.nombre} no existe. <---\n")
                es_moderador = input("¿Eres moderador del juego?(SI/NO)")

                # Si es moderador, le damos la opción de añadir el arma al juego
                if es_moderador.upper() == "SI":
                    respuesta = input("Eres moderador. ¿Deseas añadir este arma al equipamiento? (SI/NO): ")
                    if respuesta.upper() == "SI":
                        print(f"¡Genial! Vamos a añadir ese arma al equipamiento.\n")
                        arma_nueva = UtilidadesPersonaje.ampliar_equipamiento()
                        if arma_nueva:
                            # Añadimos el arma recién creada al equipamiento del personaje
                            self._equipamiento.append(arma_nueva)
                            print(
                                f"\n ---> El arma '{arma_nueva.nombre}' ha sido añadida al equipamiento del personaje {self._nombre}. <---\n")
                            return
                    else:
                        print("\n---> ¡Está bien! No se añadirá este arma al equipamiento. <---\n")
                else:
                    # Si no es moderador, le damos la opción de sugerir que se añada el arma
                    peticion = input(
                        f"¿Deseas que los moderadores del juego añadan este arma al equipamiento? (SI/NO): ")
                    if peticion.upper() == "SI":
                        print(
                            "\n---> ¡Gracias por la sugerencia! Los moderadores lo añadirán tan pronto como puedan. <---\n")
                    if peticion.upper() == "NO":
                        print("\n---> ¡Perfecto! Este arma no será añadida. <---\n")
                    return

            # Se comprueba si el personaje ya tiene esta arma en su equipamiento.
            for armita in self._equipamiento:
                if armita.nombre.lower() == arma.nombre.lower():
                    print(
                        f"\n ---> El personaje {self._nombre} ya tiene el arma '{armita.nombre}' en el equipamiento. <---\n")
                    return

            # Se añade el arma al equipamiento del personaje.
            self._equipamiento.append(arma)
            print(
                f"\n ---> El arma '{arma.nombre}' ha sido añadida al equipamiento del personaje {self._nombre}. <---\n")

        except Exception as e:
            print(f"{e}")


    # Metodo equipar arma:
    def equipar_arma(self, nombre_arma):
        """
        Intenta equipar un arma a un personaje si este ya la tiene en su equipamiento.

        Este metodo busca el arma en el inventario del personaje usando el nombre que recibe como
        parámetro. Si el arma está en su equipamiento y no está ya equipada, la equipa. Si el personaje ya
        lleva esa arma o no la tiene, se muestra un mensaje informativo.

        Pasos:
          1. Busca el arma en el equipamiento del personaje.
          2. Si no la tiene, muestra un mensaje informativo.
          3. Si ya la tiene equipada, avisa que ya está equipada.
          4. Si es nueva, equipa el arma y reemplaza la anterior si existía.

        :param nombre_arma: Nombre del arma que queremos equipar.
        :return: Nada; solo muestra mensajes que confirman cada paso.
        """

        try:
            # Se busca el arma por el nombre que se ha pasado como parametro.
            arma = UtilidadesPersonaje.buscar_arma_equipamiento(nombre_arma)

            # Si no se encuentra el arma, se avisa al usuario.
            if not arma:
                print(
                    f"\n ---> El arma '{nombre_arma.nombre}' no se encuentra en el equipamiento del personaje {self._nombre}. <---\n")
                return

            # Se comprueba si el personaje ya tiene esta arma en su equipada.
            if self._arma_equipada and self._arma_equipada.nombre == arma.nombre:
                print(f"\n ---> El personaje {self._nombre} ya tiene el arma '{arma.nombre}' equipada. <---\n")
                return


            # Se le sustituye el arma antigüa por el arma que se ha introducido por teclado.
            self._arma_equipada = arma
            print(f"\n ---> El arma '{arma.nombre}' ha sido equipada al personaje {self._nombre}. <---\n")

        except Exception as e:
            print(f"{e}")

        # Metodo establecer relacion
        def establecer_relaciones(personajes):
            """
              Función para establecer o actualizar relaciones entre personajes.

              Solicita al usuario que ingrese el nombre de un personaje principal y otro personaje con el cual
              establecerá una relación.

              Entradas:
              - personaje (str): Nombre del personaje que establece la relación.
              - personaje_relacion (str): Nombre del personaje con el cual se establece la relación.
              - tipo (str): Tipo de relación entre personajes. Debe ser uno de los valores en `tipos`.
              - nivel_confianza (int): Nivel de confianza o enemistad en un rango de 1 a 10.

              Reglas de Validación:
              1. El nombre de los personajes deben ser cadenas de texto.
              2. El tipo de relación debe estar en `tipos`: 'Amigo', 'Enemigo' o 'Neutral'.
              3. El nivel de confianza debe ser un entero entre 1 y 10.

              """

            personaje = input("Ingrese el personaje que va a establecer una relacion: ")
            personaje_relacion = input("Ingrese el nombre del personaje a relacionar: ")
            tipo = input(f"Ingrese el tipo de relaciones ({tipos}): ")
            nivel_confianza = int(input("Indique el nivel de confianza (1-10): "))

            # Verificar tipos de entrada
            if type(personaje) != str:
                print("Tipo de personaje incorrecto")
                return
            elif type(personaje_relacion) != str:
                print("Tipo de personaje-relación incorrecto")
                return
            elif tipo not in tipos:
                print("Tipo de relación inexistente, tipos: 'Amigo', 'Enemigo', 'Neutral'")
                return
            elif type(nivel_confianza) != int or not (nivel_confianza > 1 or nivel_confianza < 10):
                print("Nivel de confianza incorrecto, tiene que ser un número entre 1 y 10")
                return

            # Verificar que ambos personajes existen
            if personaje in personajes and personaje_relacion in personajes:

                relacion_actualizada = False

                for relacion in personajes[personaje]["relaciones"]:
                    if relacion["personaje"] == personaje_relacion:
                        # Si ya existe la relación, actualizamos
                        relacion["tipo"] = tipo
                        relacion["nivel_confianza"] = nivel_confianza
                        relacion_actualizada = True
                        print(f"Relación actualizada entre {personaje} y {personaje_relacion}")
                        break

                # Si no se encontró la relación, agregar una nueva
                if not relacion_actualizada:
                    nueva_relacion = {
                        "personaje": personaje_relacion,
                        "tipo": tipo,
                        "nivel_confianza": nivel_confianza
                    }
                    personajes[personaje]["relaciones"].append(nueva_relacion)
                    print(f"Relación nueva añadida entre {personaje} y {personaje_relacion}")
            else:
                print("Uno o ambos personajes no existen en el diccionario.")

    # Metodo mover
    def nueva_localizacion(personajes):
        """
       Actualiza o añade la ubicación de un personaje en el diccionario `personajes`.

       Solicita al usuario un personaje y permite:
       1. Moverlo a una ubicación existente.
       2. Añadir una nueva ubicación y mover al personaje allí.

       Entradas:
       - personaje (str): Nombre del personaje.
       - opcion (str): '1' para mover, '2' para añadir nueva ubicación.

       Actualiza:
       - `personajes[personaje]["ubicacion"]` con la ubicación seleccionada.
       - `localizaciones` si se añade una ubicación nueva.
        """

        while True:
            personaje = input("Ingrese el nombre del personaje: ")

            # Verificar si el personaje existe
            if personaje in personajes:
                break
            else:
                print("Este personaje no existe. Por favor, ingrese un nombre válido.")

        opcion = input("¿Qué desea? 1. Mover ubicación o 2. Añadir una ubicación: ")

        # Lista de ubicaciones conocidas
        localizaciones = ["Rivendel", "Hobbiton", "Minas Tirith", "Mordor", "Isengard", "Bosque Negro", "Lothlórien"]

        if opcion == "1":
            # Mover a una ubicación existente
            nueva_ubicacion = input(f"Las ubicaciones son {localizaciones}. Indique a dónde desea mover el personaje: ")

            if nueva_ubicacion in localizaciones:

                personajes[personaje]["ubicacion"] = nueva_ubicacion
                print(f"{personaje} ha sido movido a {nueva_ubicacion}.")
            else:
                print("Ubicación no válida. Por favor, elija una de las ubicaciones listadas.")

        elif opcion == "2":
            # Añadir una nueva ubicación
            ubicacion_nueva = input("Indique la nueva ubicación: ")

            if ubicacion_nueva not in localizaciones:
                # Agrega la nueva ubicación a la lista de localizaciones
                localizaciones.append(ubicacion_nueva)
                personajes[personaje]["ubicacion"] = ubicacion_nueva
                print(f"{ubicacion_nueva} ha sido añadida a las ubicaciones y {personaje} ha sido movido allí.")
            else:
                print(f"La ubicación {ubicacion_nueva} ya existe en la lista de ubicaciones conocidas.")

        else:
            print("Opción no válida. Por favor, elija 1 o 2.")

    # Metodo obtener potencia arma
    def obtener_potencia_arma(self, _arma_equipada):

        if self._arma_equipada is not None:
            return _arma_equipada.Equipamiento.potencia
        else:
            raise ValueError("No tiene arma equipada")

class UtilidadesPersonaje:

    # Lista de equipamiento que pueden añadir los personajes
    equipamiento = [
        Arma("Andúril", "Espada", 80, 50, 0.3),
        Arma("Arco de Galadriel", "Arco", 70, 10, 0.2),
        Arma("Hacha de Gimli", "Hacha", 75, 45, 0.2),
        Arma("Daga de Frodo", "Daga", 40, 20, 0.1),
        Arma("Báculo de Saruman", "Bastón", 90, 90, 0.5),
        Arma("Anillo Único", "Objeto especial", 100, 100, 1),
        Arma("Espada de Boromir", "Espada", 70, 40, 0.6)
    ]

    # Metodos adicionales para que funcione añadir equipamiento
    @staticmethod
    def buscar_arma(nombre_arma):
        """
         Busca un arma en la lista de equipamiento usando su nombre exacto.

        :param nombre_arma: Nombre del arma que queremos encontrar (ignora mayúsculas y minúsculas).
        :return: Devuelve el arma si la encuentra. Si no, devuelve un diccionario vacío.

        Nota: Asegúrate de escribir bien el nombre del arma.
        """
        for armita in UtilidadesPersonaje.equipamiento:
            if armita.nombre.lower() == nombre_arma.lower():
                return armita
        return {}

    @staticmethod
    def ampliar_equipamiento():
        """
        Permite a los moderadores añadir un nuevo arma al equipamiento.

        Le pide al usuario información como el nombre, tipo, potencia, alcance y probabilidad del arma.
        Se asegura de que estos datos sean válidos (la potencia debe ser un número entero, por ejemplo).
        Si está bien, la añade al equipamiento y confirma con un mensaje.

        :return: Devuelve el arma creada si se añadió correctamente; si no, nada.

        Nota: La potencia tiene que ser un número entero. Y sin un nombre, el arma no sirve de nada.
        """
        campo_relleno = False
        while not campo_relleno:
            try:
                nombre = input("Nombre del arma: ")
                tipo = input("Tipo de arma: ")
                potencia = int(input("Potencia: "))
                alcance = int(input("Alcance: "))
                probabilidad = float(input("Probabilidad: "))

                # Creamos el arma nueva y confirmamos al usuario
                arma_nueva = Arma(nombre, tipo, potencia, alcance, probabilidad)
                print(f"\n---> El arma '{nombre.capitalize()}' ha sido registrada exitosamente. <---\n")
                campo_relleno = True
                return arma_nueva
            except KeyboardInterrupt:
                print("\nRegistro de armas finalizado.")
            except ValueError:
                print("La potencia debe ser un número entero.")
            except Exception as e:
                print(e)

    # Metodo adicional para que funcione el metodo equipar arma
    @staticmethod
    def buscar_arma_equipamiento(nombre_arma):
        """
        Busca un arma específica en el equipamiento de un personaje.

        :param nombre_arma: Nombre del arma que queremos encontrar.
        :return: Devuelve el arma si está en el equipamiento del personaje; si no, None.

        Nota: Asegúrate de que el personaje tiene armas en su equipamiento.
        """
        for armita in UtilidadesPersonaje.equipamiento:
            if armita.nombre == nombre_arma.nombre:
                return armita
        return None

    @staticmethod
    def elegir_arma_a_equipar(personaje):
        equipamiento_str = ""
        indice = 1
        for arma in personaje.equipamiento:
            equipamiento_str += f"-> {indice}: [{str(arma)}]"
            indice += 1
        print(f"{equipamiento_str}")
        eleccion = int(input("Elige el arma a equipar (introduce el número del arma): "))
        arma = personaje.equipamiento[eleccion - 1]
        return arma

    @staticmethod
    def mostrar_equipamiento():
        equipamiento_str = ""
        for arma in UtilidadesPersonaje.equipamiento:
            equipamiento_str += f"->[{str(arma)}]\n"
        print(f"{equipamiento_str}")
        return equipamiento_str