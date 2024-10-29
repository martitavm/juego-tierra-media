# --- Menú de Gestión de la Tierra Media ---
# 1. Registrar un nuevo personaje
# 2. Añadir equipamiento a un personaje
# 3. Equipar un arma a un personaje
# 4. Establecer relaciones entre personajes
# 5. Mover un personaje a una nueva localización
# 6. Simular una batalla entre dos personajes
# 7. Listar personajes por facción
# 8. Buscar personajes por equipamiento
# 9. Mostrar todos los personajes
# 10. Salir

"""
   Muestra el menú principal de opciones para la gestión de personajes de la Tierra Media.
   :return: No devuelve nada
"""
def menu():
    print("--- Menú de Gestión de la Tierra Media ---")
    print("1. Registrar un nuevo personaje")
    print("2. Añadir equipamiento a un personaje")
    print("3. Equipar un arma a un personaje")
    print("4. Establecer relaciones entre personajes")
    print("5. Mover un personaje a una nueva localización")
    print("6. Simular una batalla entre dos personajes")
    print("7. Listar personajes por facción")
    print("8. Buscar personajes por equipamiento")
    print("9. Mostrar todos los personajes")
    print("10. Salir")

"""
    Ejecuta la acción correspondiente según la opción seleccionada en el menú.
    :param opcion_juego: int - Número de la opción elegida por el usuario
    :return: Mensaje de confirmación de la acción realizada o mensaje de salida
    
    Nota: Si el usuario selecciona una opción no válida, se mostrará un mensaje de error.
"""
def switch_menu(opcion_juego):
    match opcion_juego:
        case 1:
            print("Has seleccionado 1. Registrar un nuevo personaje")
            # return registrar_personaje()
        case 2:
            print("Has seleccionado 2. Añadir equipamiento a un personaje")
            # return anadir_equipamiento()
        case 3:
            print("Has seleccionado 3. Equipar un arma a un personaje")
            # return equipar_arma()
        case 4:
            print("Has seleccionado 4. Establecer relaciones entre personajes")
            # return establecer_relaciones()
        case 5:
            print("Has seleccionado 5. Mover un personaje a una nueva localización")
            # TODO:
            # return nueva_localizacion()
        case 6:
            print("Has seleccionado 6. Simular una batalla entre dos personajes")
            # return simular_batalla()
        case 7:
            print("Has seleccionado 7. Listar personajes por facción")
            # return listar_personaje_faccion()
        case 8:
            print("Has seleccionado 8. Buscar personajes por equipamiento")
            # return buscar_personaje_equipamiento()
        case 9:
            print("Has seleccionado 9. Mostrar todos los personajes")
            # return mostrar_personajes()
        case 10:
            return print("Has seleccionado 10. Salir")
        case _:
            return "Opción no válida"

menu()
opcion = int(input("---Selecciona una de las opciones jugador/a---\n"))

switch_menu(opcion)