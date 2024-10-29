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

def nueva_localizacion():


        while True:
            personaje = input("Ingrese el nombre del personaje: ").lower()

            # Verificar si el personaje existe
            if personaje in personajes:
                break
            else:
                print("Este personaje no existe. Por favor, ingrese un nombre válido.")


        opcion = input("¿Qué desea? 1. Mover ubicación o 2. Añadir una ubicación:\n")

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
            ubicacion_nueva = input("Indique la nueva ubicación:\n")

            if ubicacion_nueva not in localizaciones:
                # Agrega la nueva ubicación a la lista de localizaciones
                localizaciones.append(ubicacion_nueva)
                personajes[personaje]["ubicacion"] = ubicacion_nueva
                print(f"{ubicacion_nueva} ha sido añadida a las ubicaciones y {personaje} ha sido movido allí.")
            else:
                print(f"La ubicación {ubicacion_nueva} ya existe en la lista de ubicaciones conocidas.")

        else:
            print("Opción no válida. Por favor, elija 1 o 2.")
nueva_localizacion()

print(personajes)