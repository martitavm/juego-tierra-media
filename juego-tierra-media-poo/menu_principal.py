from juego_tierra_media import JuegoTierraMedia
from batalla import Batalla
from equipamiento import Arma
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


dict_personajes = {}
dict_facciones = {}
juego = JuegoTierraMedia(dict_personajes, dict_facciones)

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
            print("Has seleccionado 2. Añadir equipamiento a un personaje")
            nombre = input("Nombre del personaje: ")
            equipo = input("Equipamiento del personaje: ")
            juego.anadir_equipamiento(nombre, equipo)
        case 3:
            print("Has seleccionado 3. Equipar un arma a un personaje")
            nombre = input("Nombre del personaje: ")
            pnj = dict_personajes[nombre]
            arma = Arma("Andúril", "Espada", 80, 5, 0.6)
            pnj.equipar_arma(arma)
            # Personaje.equipar_arma(arma)
        case 4:
            print("Has seleccionado 4. Establecer relaciones entre personajes")
            # return establecer_relaciones(personajes)
        case 5:
            print("Has seleccionado 5. Mover un personaje a una nueva localización")
            # return nueva_localizacion(personajes)
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

            # return listar_personaje_faccion(personajes)
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


opcion_juego = -1
while opcion_juego != 10:
    try:
        menu()
        opcion_juego = int(input("---Selecciona una de las opciones jugador/a ---> "))
        switch_menu(opcion_juego)
    except ValueError:
        print(f"Introduce un número entre 1-10.")

# if __name__ == '__main__':
#     juego = JuegoTierraMedia(personajes_dict={}, facciones_dict={})
