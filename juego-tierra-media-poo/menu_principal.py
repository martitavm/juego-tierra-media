from juego_tierra_media import JuegoTierraMedia
from batalla import Batalla
from personaje import UtilidadesPersonaje


def menu():
    """
       Muestra el menú principal de opciones para la gestión de personajes de la Tierra Media.
       :return: No devuelve nada
    """

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


def switch_menu(opcion):
    """
    Ejecuta la acción correspondiente según la opción seleccionada en el menú.
    :return: Mensaje de confirmación de la acción realizada o mensaje de salida

    Nota: Si el usuario selecciona una opción no válida, se mostrará un mensaje de error.
    """
    match opcion:
        case 1:
            print("Has seleccionado 1. Registrar un nuevo personaje")
            juego.registrar_personaje()

        case 2:
            _case_anadir_equipamiento()

        case 3:
            _case_equipar_arma()

        case 4:
            print("Has seleccionado 4. Establecer relaciones entre personajes")
            nombre_personaje = input("Nombre del personaje: ")
            personaje = dict_personajes.get(nombre_personaje)  # Obtener el objeto Personaje del diccionario

            if personaje:  # Verificar si el personaje existe
                personajes_relacion = input("Personaje a relacionar: ")
                personaje_relacion = dict_personajes.get(
                    personajes_relacion)  # Obtener el objeto del personaje relacionado

                if personaje_relacion:  # Verificar si el personaje relacionado existe
                    tipo = input("Tipo de relación: ").capitalize()
                    nivel_confianza = int(input("Nivel de relación (1-10): "))

                    return juego.establecer_relacion(personaje, personaje_relacion, tipo, nivel_confianza)
                else:
                    print(f"El personaje '{personajes_relacion}' no existe.")
            else:
                print(f"El personaje '{nombre_personaje}' no existe.")

        case 5:
            print("Has seleccionado 5. Mover un personaje a una nueva localización")
            try:
                nombre_personaje = input("Nombre del personaje: ")
                p1 = dict_personajes[nombre_personaje]
                nueva_ubicacion = input("Indique la ubicaion: ")
                return juego.nueva_ubicacion(p1, nueva_ubicacion)
            except KeyError:
                print(f"El personaje '{nombre_personaje}' no existe.")
        case 6:
            print("Has seleccionado 6. Simular una batalla entre dos personajes")
            try:
                nombre_p1 = input("Nombre del personaje: ").capitalize()
                p1 = dict_personajes[nombre_p1]
                nombre_p2 = input("Nombre del personaje: ").capitalize()
                p2 = dict_personajes[nombre_p2]
            except KeyError:
                print("Parece que uno de los personajes no existe, prueba de nuevo.")
                return
            Batalla.simular(p1, p2)
        case 7:
            print("Has seleccionado 7. Listar personajes por facción")
            juego.listar_personaje_faccion()

        case 8:
            print("Has seleccionado 8. Buscar personajes por equipamiento")
            equipo = input("Introduce el equipo a buscar: ")
            juego.buscar_personaje_equipamiento(equipo)
        case 9:
            print("Has seleccionado 9. Mostrar todos los personajes")
            juego.mostrar_personajes()
        case 10:
            print("Has seleccionado 10. Salir")
            juego.salir()
        case _:
            print("Opción no válida")


def _case_equipar_arma():
    print("Has seleccionado 3. Equipar un arma a un personaje")
    nombre = input("Nombre del personaje: ")
    pnj = dict_personajes[nombre]
    arma = UtilidadesPersonaje.elegir_arma_a_equipar(pnj)
    pnj.equipar_arma(arma)


def _case_anadir_equipamiento():
    print("Has seleccionado 2. Añadir equipamiento a un personaje")
    nombre = input("Nombre del personaje: ")
    UtilidadesPersonaje.mostrar_equipamiento()
    equipo = input("Elige el arma que quieres añadir al equipamiento: ")
    juego.anadir_equipamiento(nombre, equipo)


if __name__ == '__main__':

    dict_personajes = {}
    dict_facciones = {}
    juego = JuegoTierraMedia(dict_personajes, dict_facciones)

    opcion_juego = -1
    while opcion_juego != 10:
        try:
            menu()
            opcion_juego = int(input("---Selecciona una de las opciones jugador/a ---> "))
            switch_menu(opcion_juego)
        except ValueError:
            print(f"Introduce un número entre 1-10.")
