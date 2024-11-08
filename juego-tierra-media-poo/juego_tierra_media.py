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


"""
    def buscar_arma(nombre_arma):
        
        Busca un arma en la lista de equipamiento usando su nombre.

        :param nombre_arma: El nombre del arma que queremos encontrar. Se ignoran las mayúsculas, así que
                            "Espada" y "espada" se consideran iguales.
        :return: Devuelve un diccionario con la información del arma si se encuentra. Si no se encuentra,
                 retorna un diccionario vacío.

        Nota: Si estás buscando un arma, asegúrate de escribir bien el nombre.
        
        for arma in equipamiento:
            if arma["nombre"].lower() == nombre_arma.lower():
                return arma
        return {}

"""
"""
    def anadir_equipamiento(personajes):
        
        Añade un arma al equipamiento de un personaje si este existe y si no la tiene ya.

        Esta función pregunta al usuario por el nombre del personaje y el nombre del arma que se
        quiere añadir. Si el personaje no está en la lista, informa al usuario. Si el arma no existe,
        también lo dice. Además, verifica que el personaje no tenga ya el arma en su equipamiento.

        :return: No devuelve nada, pero imprime mensajes con información según la situación.

        Nota: Asegúrate de que el personaje y el arma estén bien escritos, porque si no,
              no las podrás añadir. No queremos que un elfo se quede sin su arco favorito.
        

        try:
            # Se piden el nombre del personaje al que se le va a ampliar el equipamiento y el arma que se va a añadir.
            nombre_personaje = input("Introduce el nombre del personaje: ")
            campo_vacio_exception(nombre_personaje)
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

"""
"""
    def ampliar_equipamiento(personajes):
        
        Esta función es para los moderadores del juego.

        Registra un nuevo arma en el equipamiento pidiendo al usuario detalles sobre ella.

        Esta función solicita al usuario el nombre, tipo, potencia y descripción del arma que se
        quiere añadir. Asegura que ninguna de estas entradas esté vacía y que la potencia sea un
        número entero. Si está correcto, añade el arma al equipamiento y lo confirma con un
        mensaje.

        :return: No devuelve nada, pero imprime mensajes que indican el estado del registro del arma.

        Nota: Recuerda que la potencia tiene que ser un número entero. Y no olvides que un arma sin nombre
              es como un guerrero sin espada: ¡no tiene sentido!
        
        campo_relleno = False
        while not campo_relleno:
            try:
                nombre = input("Nombre del arma: ")
                campo_vacio_exception(nombre)
                tipo = input("Tipo de arma: ")
                campo_vacio_exception(tipo)
                potencia = int(input("Potencia: "))
                arma_nueva = {"nombre": nombre, "tipo": tipo, "potencia": potencia}
                equipamiento.append(arma_nueva)
                print(f"\n---> El arma '{nombre.capitalize()}' ha sido registrada exitosamente. <---\n")
                campo_relleno = True
                return arma_nueva
            except KeyboardInterrupt:
                print("\nRegistro de armas finalizado.")
            except ValueError:
                print("La potencia debe ser un número entero.")
            except Exception as e:
                print(e)
"""

"""
    tipos = ["Amigo", "Enemigo", "Neutral"]

    def establecer_relaciones(personajes):
        
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

"""

"""
def nueva_localizacion(personajes):
    
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
"""

    def listar_personaje_faccion(personajes):
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
                nombre for nombre, personaje in personajes.items()
                if personaje.faccion.lower() == nombre_faccion.lower()
            ]

            # Comprobamos si existe la facción escrita por el usuario, si existe muestra los personajes de esa facción y si no existe saltará un aviso
            if personajes_en_faccion:
                for nombre in personajes_en_faccion:
                    print(nombre)
            else:
                print("No hay personajes en esa facción o no existe.")

        except Exception as e:
            print(f"Error: {e}")
            


"""
def buscar_personaje_equipamiento(personajes):
    
    Función que muestra los personajes que tienen en su equipamiento el
    arma introducida por teclado.
    :return: Lista con los personajes que tienen el arma en su equipamiento.
    
    lista_personaje_equipado = []
    try:
        equipo = input("Introduce el arma a buscar: ").lower()
        campo_vacio(equipo)

        for keys, values in personajes.items():
            for arma in values["equipamiento"]:
                if equipo in arma["nombre"].lower():
                    lista_personaje_equipado.append(keys)

        if len(lista_personaje_equipado) == 0:
            print(f"Ningún personaje tiene {equipo}")
        else:
            print(f"Personajes con {equipo.capitalize()} \n{lista_personaje_equipado}")
        return
    except AttributeError:
        print("Introduce el nombre del equipo")
    except NameError:
        print("El diccionario con datos no existe")
    except Exception as e:
        print(f"{e}")
        
"""
"""
def mostrar_personajes(personajes):
    
    Función que recorre un diccionario de personajes y muestra todos sus datos.
    :return: Datos del diccionario recorrido.
    
    try:
        for keys, values in personajes.items():
            print(f"Personaje: {keys}")
            for value, datos in values.items():
                print(f"-> {value.capitalize()}: {datos}")
            print("---------------------------------------")
        return
    except NameError:
        print("El diccionario con datos no existe")
"""


def salir():
    print("Has finalizado el juego")
    exit(0)
