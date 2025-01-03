from anadir_equipamiento_personaje import anadir_equipamiento
from batalla import simular_batalla, buscar_personaje_equipamiento, mostrar_personajes
from equipar_arma import equipar_arma
from establcer_relaciones import establecer_relaciones
from listar_personaje_faccion import listar_personaje_faccion
from nueva_localicacion import nueva_localizacion
from registrar_personaje import registrar_personaje

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
            return registrar_personaje(personajes)

        case 2:
            print("Has seleccionado 2. Añadir equipamiento a un personaje")
            return anadir_equipamiento(personajes)
        case 3:
            print("Has seleccionado 3. Equipar un arma a un personaje")
            return equipar_arma(personajes)
        case 4:
            print("Has seleccionado 4. Establecer relaciones entre personajes")
            return establecer_relaciones(personajes)
        case 5:
            print("Has seleccionado 5. Mover un personaje a una nueva localización")
            return nueva_localizacion(personajes)
        case 6:
            print("Has seleccionado 6. Simular una batalla entre dos personajes")
            return simular_batalla(personajes)
        case 7:
            print("Has seleccionado 7. Listar personajes por facción")

            return listar_personaje_faccion(personajes)
        case 8:
            print("Has seleccionado 8. Buscar personajes por equipamiento")
            return buscar_personaje_equipamiento(personajes)
        case 9:
            print("Has seleccionado 9. Mostrar todos los personajes")
            return mostrar_personajes(personajes)
        case 10:
            print("Has seleccionado 10. Salir")
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