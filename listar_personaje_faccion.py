from registrar_personaje import verificar_si_input_vacio


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
        verificar_si_input_vacio(nombre_faccion)
        personajes_en_faccion = [
            personaje for personaje in personajes
            if personajes[personaje]["faccion"].lower() == nombre_faccion.lower()
        ]
        # Comprobamos si existe la facción escrita por el usuario, si existe muestra los personajes de esa facción y si no existe saltará un aviso
        if personajes_en_faccion:
            for personaje in personajes_en_faccion:
                print(personaje)
        else:
            print("No hay personajes en esa facción o no existe.")

    except Exception as e:
        print(f"Error: {e}")
