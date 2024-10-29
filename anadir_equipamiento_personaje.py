# Añadir equipamiento a un personaje:
#
# Permite añadir equipamiento a un personaje ya registrado.
# Cada equipamiento tiene los siguientes atributos:
# Nombre del objeto: (string) El nombre del equipamiento.
# Tipo: Arma, Armadura, Objeto especial.
# Potencia: (entero positivo) Un valor numérico que representa la potencia del objeto.
# El equipamiento se añadirá a la lista de objetos del personaje.

personajes = {
    "Aragorn": {
        "raza": "Humano",
        "faccion": "La Comunidad del Anillo",
        "ubicacion": "Rivendel",
        "equipamiento": [
            {"nombre": "Andúril", "tipo": "Espada", "potencia": 80}
        ],
        "arma_equipada": {"nombre": "Andúril", "tipo": "Espada", "potencia": 80},
        "relaciones": [
            {"personaje": "Legolas", "tipo": "Amigo", "nivel_confianza": 10}
        ]
    },
    "Legolas": {
        "raza": "Elfo",
        "faccion": "La Comunidad del Anillo",
        "ubicacion": "Bosque Negro",
        "equipamiento": [
            {"nombre": "Arco de Galadriel", "tipo": "Arco", "potencia": 70}
        ],
        "arma_equipada": {"nombre": "Arco de Galadriel", "tipo": "Arco", "potencia": 70},
        "relaciones": [
            {"personaje": "Aragorn", "tipo": "Amigo", "nivel_confianza": 10}
        ]
    }
}


equipamiento = [
{"nombre": "Andúril", "tipo": "Espada", "potencia": 80, "descripcion": "La espada legendaria de Aragorn, forjada de los fragmentos de Narsil."},
    {"nombre": "Arco de Galadriel", "tipo": "Arco", "potencia": 70, "descripcion": "El arco de Legolas, dado como un regalo por la dama Galadriel."},
    {"nombre": "Hacha de Gimli", "tipo": "Hacha", "potencia": 75, "descripcion": "El arma favorita del enano Gimli, eficaz en combate cuerpo a cuerpo."},
    {"nombre": "Daga de Frodo", "tipo": "Daga", "potencia": 40, "descripcion": "Daga élfica que Frodo lleva durante su viaje."},
    {"nombre": "Báculo de Saruman", "tipo": "Bastón", "potencia": 90, "descripcion": "Un bastón de poder usado por el mago Saruman."},
    {"nombre": "Anillo Único", "tipo": "Objeto especial", "potencia": 100, "descripcion": "El Anillo creado por Sauron para gobernar todos los demás."},
    {"nombre": "Espada de Boromir", "tipo": "Espada", "potencia": 70, "descripcion": "El arma usada por Boromir, capitán de Gondor."}
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

def anadir_equipamiento():
    """
    Añade un arma al equipamiento de un personaje si este existe y si no la tiene ya.

    Esta función pregunta al usuario por el nombre del personaje y el nombre del arma que se
    quiere añadir. Si el personaje no está en la lista, informa al usuario. Si el arma no existe,
    también lo dice. Además, verifica que el personaje no tenga ya el arma en su equipamiento.

    :return: No devuelve nada, pero imprime mensajes con información según la situación.

    Nota: Asegúrate de que el personaje y el arma estén bien escritos, porque si no,
          no las podrás añadir. No queremos que un elfo se quede sin su arco favorito.
    """
    nombre_personaje = input("Introduce el nombre del personaje: ")
    nombre_arma = input("Introduce el nombre del arma: ")

    try:
        if nombre_personaje not in personajes:
            print(f"El personaje {nombre_personaje} no existe.")
            return
        personaje = personajes[nombre_personaje]
        arma = buscar_arma(nombre_arma)

        if not arma:
            print(f"El arma {nombre_arma.capitalize()} no existe.")
            return

        for armita in personaje["equipamiento"]:
            if armita["nombre"].lower() == arma["nombre"].lower():
                print(f"El personaje {nombre_personaje} ya tiene el arma '{armita['nombre']}' en el equipamiento.")
                return


        personaje["equipamiento"].append(arma)
        print(f"El arma '{arma['nombre']}' ha sido añadida al equipamiento del personaje {nombre_personaje}.")

    except KeyError:
        print(f"El personaje {nombre_personaje} no existe.")

def ampliar_equipamiento():
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
            descripcion = input("Descripcion: ")
            campo_vacio_exception(descripcion)
            equipamiento.append({"nombre": nombre, "tipo": tipo, "potencia": potencia, "descripcion": descripcion})
            print(f"El arma '{nombre.capitalize()}' ha sido registrada exitosamente.")
            campo_relleno = True
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
    if entrada == "":
        raise Exception("El campo no puede estar vacío. Por favor, inserte algo.")
    return entrada




anadir_equipamiento()
ampliar_equipamiento()
print(equipamiento)

