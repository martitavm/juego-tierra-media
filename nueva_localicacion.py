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