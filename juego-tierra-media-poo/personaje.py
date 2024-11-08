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
        return f"Nombre: {self._nombre}, Raza: {self._raza}, Facción: {self._faccion}, Ubicacion: {self._ubicacion}, Equipamiento: {self._equipamiento}, Relaciones: {self._relaciones}, Arma Equipada: {self._arma_equipada}"

    # Metodo añadir equipamiento

    def anadir_equipamiento(personajes):
        """
        Añade un arma al equipamiento de un personaje si este existe y si no la tiene ya.

        Esta función pregunta al usuario por el nombre del personaje y el nombre del arma que se
        quiere añadir. Si el personaje no está en la lista, informa al usuario. Si el arma no existe,
        también lo dice. Además, verifica que el personaje no tenga ya el arma en su equipamiento.

        :return: No devuelve nada, pero imprime mensajes con información según la situación.

        Nota: Asegúrate de que el personaje y el arma estén bien escritos, porque si no,
              no las podrás añadir. No queremos que un elfo se quede sin su arco favorito.
        """

        try:
            # Se piden el nombre del personaje al que se le va a ampliar el equipamiento y el arma que se va a añadir.
            nombre_personaje = input("Introduce el nombre del personaje: ")
            if nombre_personaje.capitalize() not in personajes:
                print(
                    f"\n ---> El personaje {nombre_personaje} no existe (comprueba que lo has escrito correctamente). <---\n")
                return

            print("Estas son las armas disponibles para el personaje:\n")
            for weapon in equipamiento:
                print(f"-> {weapon}")
            nombre_arma = input("\nIntroduce el nombre del arma que quieres añadir: ")

            # Si el personaje existe, lo almacenamos en la variable 'personaje'.
            personaje = personajes[nombre_personaje]
            # Se busca el arma por el nombre que el usuario ha introducido.
            arma = buscar_arma(nombre_arma)

            # Si no se encuentra el arma, se avisa al usuario.
            if not arma:
                print(f"\n ---> El arma {nombre_arma.capitalize()} no existe. <---\n")
                es_moderador = input("¿Eres moderador del juego?(SI/NO)")
                if es_moderador.upper() == "SI":
                    respuesta = input("Eres moderador. ¿Deseas añadir este arma al equipamiento? (SI/NO): ")
                    if respuesta.upper() == "SI":
                        print(f"¡Genial! Vamos a añadir ese arma al equipamiento.\n")
                        arma_nueva = ampliar_equipamiento(personajes)
                        if arma_nueva:
                            personaje["equipamiento"].append(arma_nueva)
                            print(
                                f"\n ---> El arma '{arma_nueva['nombre']}' ha sido añadida al equipamiento del personaje {nombre_personaje}. <---\n")
                            return
                    else:
                        print("\n---> ¡Está bien! No se añadirá este arma al equipamiento. <---\n")
                else:
                    peticion = input(
                        f"¿Deseas que los moderadores del juego añadan este arma al equipamiento? (SI/NO): ")
                    if peticion.upper() == "SI":
                        print(
                            "\n---> ¡Gracias por la sugerencia! Los moderadores lo añadirán tan pronto como puedan. <---\n")
                    if peticion.upper() == "NO":
                        print("\n---> ¡Perfecto! Este arma no será añadida. <---\n")
                    return

            # Se comprueba si el personaje ya tiene esta arma en su equipamiento.
            for armita in personaje["equipamiento"]:
                if armita["nombre"].lower() == arma["nombre"].lower():
                    print(
                        f"\n ---> El personaje {nombre_personaje} ya tiene el arma '{armita['nombre']}' en el equipamiento. <---\n")
                    return

            # Se añade el arma al equipamiento del personaje.
            personaje["equipamiento"].append(arma)
            print(
                f"\n ---> El arma '{arma['nombre']}' ha sido añadida al equipamiento del personaje {nombre_personaje}. <---\n")

        except Exception as e:
            print(f"{e}")


    # Metodo equipar arma:
    def equipar_arma(personajes):
        """
        Equipa un arma a un personaje si este la tiene en su inventario.

        Esta función solicita al usuario que introduzca el nombre de un personaje y el nombre de un
        arma. Luego, verifica si el personaje existe y si el arma está en su equipamiento. Si el
        arma ya está equipada, informa al usuario. Si está correcto, equipa el arma al
        personaje y lo confirma con un mensaje.

        :return: No devuelve nada, pero imprime mensajes que indican el estado del proceso de
                 equipar el arma.

        Nota: ¡Asegúrate de que tu personaje no esté ya armado hasta los dientes! Solo puedes tener un arma
         equipada. Si añades una nueva, se reemplazará por la antigua.
         Si intentas equipar algo que ya lleva puesto, te lo recordaremos para evitar confusiones.
        """

        try:
            # Se piden el nombre del personaje al que se le va a equipar un arma y el arma que se le va a equipar.
            nombre_personaje = input("Introduce el nombre del personaje: ").capitalize()

            if nombre_personaje not in personajes:
                print(f"El personaje {nombre_personaje} no existe (comprueba que lo has escrito correctamente).")
                return

            # Se almacena el nombre del personaje introducido en la variable 'personaje'.
            personaje = personajes[nombre_personaje]

            print(f"Estas son las armas disponibles en el equipamiento de {nombre_personaje}:\n")
            for weapon in personaje["equipamiento"]:
                print(f"-> {weapon}")

            nombre_arma = input("\nIntroduce el nombre del arma que quieres equipar: ")

            # Comprobar si el personaje ya tiene un campo "arma_equipada" en su diccionario, si no, crear uno como lista vacía
            if "arma_equipada" not in personaje:
                personaje["arma_equipada"] = {}

            # Se busca el arma por el nombre que el usuario ha introducido.
            arma = buscar_arma_equipamiento(personaje, nombre_arma)

            # Si no se encuentra el arma, se avisa al usuario.
            if not arma:
                print(
                    f"\n ---> El arma '{nombre_arma.capitalize()}' no se encuentra en el equipamiento del personaje {nombre_personaje}. <---\n")
                return

            # Se comprueba si el personaje ya tiene esta arma en su equipada.
            if personaje["arma_equipada"] and personaje["arma_equipada"]["nombre"].lower() == nombre_arma.lower():
                print(f"\n ---> El personaje {nombre_personaje} ya tiene el arma '{arma['nombre']}' equipada. <---\n")
                return

            # Se le sustituye el arma antigüa por el arma que se ha introducido por teclado.
            personaje["arma_equipada"] = arma
            print(f"\n ---> El arma '{arma['nombre']}' ha sido equipada al personaje {nombre_personaje}. <---\n")

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

class UtilidadesPersonaje:

    # Metodos adicionales para que funcione añadir equipamiento
    @staticmethod
    def buscar_arma(nombre_arma):
        """
        Busca un arma en la lista de equipamiento usando su nombre.

        :param nombre_arma: El nombre del arma que queremos encontrar. Se ignoran las mayúsculas, así que
                            "Espada" y "espada" se consideran iguales.
        :return: Devuelve un diccionario con la información del arma si se encuentra. Si no se encuentra,
                    retorna un diccionario vacío.

        Nota: Si estás buscando un arma, asegúrate de escribir bien el nombre.
        """
        for arma in equipamiento:
            if arma["nombre"].lower() == nombre_arma.lower():
                return arma
        return {}

    @staticmethod
    def ampliar_equipamiento(personajes):
        """
        Esta función es para los moderadores del juego.

        Registra un nuevo arma en el equipamiento pidiendo al usuario detalles sobre ella.

        Esta función solicita al usuario el nombre, tipo, potencia y descripción del arma que se
        quiere añadir. Asegura que ninguna de estas entradas esté vacía y que la potencia sea un
        número entero. Si está correcto, añade el arma al equipamiento y lo confirma con un
        mensaje.

        :return: No devuelve nada, pero imprime mensajes que indican el estado del registro del arma.

        Nota: Recuerda que la potencia tiene que ser un número entero. Y no olvides que un arma sin nombre
                es como un guerrero sin espada: ¡no tiene sentido!
        """
        campo_relleno = False
        while not campo_relleno:
            try:
                nombre = input("Nombre del arma: ")
                tipo = input("Tipo de arma: ")
                potencia = int(input("Potencia: "))
                arma_nueva = {"nombre": nombre, "tipo": tipo, "potencia": potencia}
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
    def buscar_arma_equipamiento(nombre_personaje, nombre_arma):
        """
        Busca un arma específica en el equipamiento de un personaje.

        Esta función toma el nombre de un personaje y el nombre de un arma, y busca en la lista de
        equipamiento del personaje para ver si tiene el arma que se le indica. La búsqueda no distingue
        entre mayúsculas y minúsculas, así que no te preocupes por eso.

        :param nombre_personaje: El diccionario del personaje cuyo equipamiento se está revisando.
        :param nombre_arma: El nombre del arma que queremos encontrar dentro del equipamiento del personaje.
        :return: Devuelve el diccionario del arma si se encuentra; si no, devuelve None.

        Nota: Si buscas un arma en el equipamiento, asegúrate de que el personaje realmente tenga algo
                en su inventario.
        """
        for arma in nombre_personaje["equipamiento"]:
            if arma["nombre"].lower() == nombre_arma.lower():
                return arma
        return None



