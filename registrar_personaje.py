# Registrar un nuevo personaje:
# Debes permitir registrar personajes con los siguientes atributos:
# Nombre: (string) El nombre único del personaje.
# Raza: Elfo, Humano, Enano, Hobbit.
# Facción: (string) Nombre de la facción a la que pertenece (por ejemplo: "La Comunidad del Anillo").
# Ubicación: (string) Lugar donde se encuentra el personaje (por ejemplo: "Rivendel", "Mordor").
# Equipamiento: (lista vacía al inicio). Aquí se almacenarán los objetos que el personaje puede llevar (como armas o armaduras).
# Relaciones: (lista vacía al inicio). Almacena las relaciones del personaje con otros personajes (amigos, enemigos, etc.).
# El personaje debe almacenarse en un diccionario dentro de un diccionario general llamado personajes.

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

"""
   Verifica que el input no esté vacío.

   :param input: str - Cadena de texto que representa el valor introducido por el usuario
   :return: str - Devuelve el valor de entrada si no está vacío
   :raises ValueError: Si el input está vacío, lanza un error con el mensaje "Introduce el contenido correctamente."
"""
def verificar_si_input_vacio(input):
    if input == "":
        raise ValueError("Introduce el contenido correctamente.")
    return input

"""
    Registra un nuevo personaje en el diccionario general de personajes.

    Este método permite ingresar la información de un nuevo personaje en el diccionario `personajes`, con los siguientes
    atributos: nombre, raza, facción, ubicación, equipamiento y relaciones. Los atributos `equipamiento` y `relaciones` 
    se inicializan como listas vacías.

    :return: No devuelve nada.
"""
def registrar_personaje():
    try:
        nombre = input("Introduce el nombre del personaje que desea registrar: ")
        verificar_si_input_vacio(nombre)
        raza = input("Introduce la raza que desea registrar: ")
        verificar_si_input_vacio(raza)
        faccion = input("Introduce la faccion que desea registrar: ")
        verificar_si_input_vacio(faccion)
        ubicacion = input("Introduce la ubicacion que desea registrar: ")
        verificar_si_input_vacio(ubicacion)
        equipamiento = []
        relaciones = []

        personajes.update({nombre: {"raza": raza, "faccion": faccion, "ubicacion": ubicacion, "equipamiento": equipamiento, "relaciones": relaciones}})
        print(f"El personaje {nombre} ha sido registrado exitosamente. ")
    except ValueError as e:
        print(f"Error: {e}")

    finally:
        print(personajes)


registrar_personaje()