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


def verificar_si_input_vacio(input):
    if input == "":
        raise ValueError("Introduce el contenido correctamente.")
    return input


"""
    Muestra todos los personajes que pertenecen a una facción específica.

    Solicita al usuario introducir el nombre de una facción y luego muestra una lista de personajes que
    pertenecen a esa facción. Si la facción introducida no contiene personajes o no existe, muestra un
    mensaje indicándolo.

    :return: No devuelve nada
"""
def listar_personaje_faccion():

    try:
        nombre_faccion = input("Ingrese el nombre de la faccion que desea listar: ")
        verificar_si_input_vacio(nombre_faccion)

        personajes_en_faccion = [
            personaje for personaje in personajes
            if personajes[personaje]["faccion"].lower() == nombre_faccion.lower()
        ]

        if personajes_en_faccion:
            for personaje in personajes_en_faccion:
                print(personaje)
        else:
            print("No hay personajes en esa facción o no existe.")

    except Exception as e:
        print(f"Error: {e}")


listar_personaje_faccion()
