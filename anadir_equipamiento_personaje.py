# Añadir equipamiento a un personaje:
#
# Permite añadir equipamiento a un personaje ya registrado.
# Cada equipamiento tiene los siguientes atributos:
# Nombre del objeto: (string) El nombre del equipamiento.
# Tipo: Arma, Armadura, Objeto especial.
# Potencia: (entero positivo) Un valor numérico que representa la potencia del objeto.
# El equipamiento se añadirá a la lista de objetos del personaje.

equipamiento = [
{"nombre": "Andúril", "tipo": "Espada", "potencia": 80},
    {"nombre": "Arco de Galadriel", "tipo": "Arco", "potencia": 70},
    {"nombre": "Hacha de Gimli", "tipo": "Hacha", "potencia": 75},
    {"nombre": "Daga de Frodo", "tipo": "Daga", "potencia": 40},
    {"nombre": "Báculo de Saruman", "tipo": "Bastón", "potencia": 90},
    {"nombre": "Anillo Único", "tipo": "Objeto especial", "potencia": 100},
    {"nombre": "Espada de Boromir", "tipo": "Espada", "potencia": 70}
]

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
    return  {}

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
        campo_vacio_exception(nombre_personaje)
        if nombre_personaje.capitalize() not in personajes:
            print(f"\n ---> El personaje {nombre_personaje} no existe (comprueba que lo has escrito correctamente). <---\n")
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
                respuesta= input("Eres moderador. ¿Deseas añadir este arma al equipamiento? (SI/NO): ")
                if respuesta.upper() == "SI":
                    print(f"¡Genial! Vamos a añadir ese arma al equipamiento.\n")
                    arma_nueva = ampliar_equipamiento(personajes)
                    if arma_nueva:
                        personaje["equipamiento"].append(arma_nueva)
                        print(f"\n ---> El arma '{arma_nueva['nombre']}' ha sido añadida al equipamiento del personaje {nombre_personaje}. <---\n")
                        return
                else:
                    print("\n---> ¡Está bien! No se añadirá este arma al equipamiento. <---\n")
            else:
                peticion = input(f"¿Deseas que los moderadores del juego añadan este arma al equipamiento? (SI/NO): ")
                if peticion.upper() == "SI":
                    print("\n---> ¡Gracias por la sugerencia! Los moderadores lo añadirán tan pronto como puedan. <---\n")
                if peticion.upper() == "NO":
                    print("\n---> ¡Perfecto! Este arma no será añadida. <---\n")
                return

        # Se comprueba si el personaje ya tiene esta arma en su equipamiento.
        for armita in personaje["equipamiento"]:
            if armita["nombre"].lower() == arma["nombre"].lower():
                print(f"\n ---> El personaje {nombre_personaje} ya tiene el arma '{armita['nombre']}' en el equipamiento. <---\n")
                return

        # Se añade el arma al equipamiento del personaje.
        personaje["equipamiento"].append(arma)
        print(f"\n ---> El arma '{arma['nombre']}' ha sido añadida al equipamiento del personaje {nombre_personaje}. <---\n")

    except Exception as e:
        print(f"{e}")

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


def campo_vacio_exception(entrada):
    """
    Verifica si la entrada está vacía y lanza una excepción si lo está.

    Esta función comprueba si el valor que se le pasa está vacío (es decir, si es una cadena vacía).
    Si es así, lanza una excepción con un mensaje que indica que el campo no puede estar vacío.
    Si la entrada no está vacía, simplemente la devuelve.

    :param entrada: La entrada que se va a comprobar. Puede ser cualquier cadena que el usuario
                    proporcione.
    :return: La misma entrada si no está vacía.
    """
    if entrada == "" or entrada == " ":
        raise Exception("El campo no puede estar vacío. Por favor, inserte algo.")
    return entrada