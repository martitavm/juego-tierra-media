# Equipar un arma a un personaje:

# Permite que un personaje seleccione un arma de su inventario de equipamiento y la equipe.
# Si el personaje ya tiene una arma equipada, se debe reemplazar con la nueva.

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
    # Se piden el nombre del personaje al que se le va a equipar un arma y el arma que se le va a equipar.
    nombre_personaje = input("Introduce el nombre del personaje: ")
    nombre_arma = input("Introduce el nombre del arma: ")

    try:
        # Se almacena el nombre del personaje introducido en la variable 'personaje'.
        personaje = personajes[nombre_personaje]
        # Se busca el arma por el nombre que el usuario ha introducido.
        arma = buscar_arma_equipamiento(personaje, nombre_arma)

        # Si no se encuentra el arma, se avisa al usuario.
        if not arma:
            print(f"El arma '{nombre_arma.capitalize()}' no se encuentra en el equipamiento del personaje {nombre_personaje}.")
            return

        # Se comprueba si el personaje ya tiene esta arma en su equipada.
        if personaje["arma_equipada"]["nombre"].lower() == nombre_arma.lower():
            print(f"El personaje {nombre_personaje} ya tiene el arma '{arma['nombre']}' equipada.")
            return

        # Se le sustituye el arma antigüa por el arma que se ha introducido por teclado.
        personaje["arma_equipada"].update(arma)
        print(f"El arma '{arma['nombre']}' ha sido equipada al personaje {nombre_personaje}.")

    except KeyError:
        print (f"El personaje {nombre_personaje} no existe.")

