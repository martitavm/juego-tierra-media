# Añadir equipamiento a un personaje:
#
# Permite añadir equipamiento a un personaje ya registrado.
# Cada equipamiento tiene los siguientes atributos:
# Nombre del objeto: (string) El nombre del equipamiento.
# Tipo: Arma, Armadura, Objeto especial.
# Potencia: (entero positivo) Un valor numérico que representa la potencia del objeto.
# El equipamiento se añadirá a la lista de objetos del personaje.

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


equipamiento = [
{"nombre": "Andúril", "tipo": "Espada", "potencia": 80, "descripcion": "La espada legendaria de Aragorn, forjada de los fragmentos de Narsil."},
    {"nombre": "Arco de Galadriel", "tipo": "Arco", "potencia": 70, "descripcion": "El arco de Legolas, dado como un regalo por la dama Galadriel."},
    {"nombre": "Hacha de Gimli", "tipo": "Hacha", "potencia": 75, "descripcion": "El arma favorita del enano Gimli, eficaz en combate cuerpo a cuerpo."},
    {"nombre": "Daga de Frodo", "tipo": "Daga", "potencia": 40, "descripcion": "Daga élfica que Frodo lleva durante su viaje."},
    {"nombre": "Báculo de Saruman", "tipo": "Bastón", "potencia": 90, "descripcion": "Un bastón de poder usado por el mago Saruman."},
    {"nombre": "Anillo Único", "tipo": "Objeto especial", "potencia": 100, "descripcion": "El Anillo creado por Sauron para gobernar todos los demás."},
    {"nombre": "Espada de Boromir", "tipo": "Espada", "potencia": 70, "descripcion": "El arma usada por Boromir, capitán de Gondor."}
]


def buscar_arma(nombre_arma):
    for arma in equipamiento:
        if arma["nombre"].lower() == nombre_arma.lower():
            return arma
    return  {}

def anadir_equipamiento(nombre_personaje, nombre_arma):

    if nombre_personaje not in personajes:
        print(f"El personaje {nombre_personaje} no existe.")
        return
    personaje = personajes[nombre_personaje]
    arma = buscar_arma(nombre_arma)

    if not arma:
        print(f"El arma {nombre_arma} no existe.")
        return

    for armita in personaje["equipamiento"]:
        if armita["nombre"].lower() == arma["nombre"].lower():
            print(f"El personaje {nombre_personaje} ya tiene el arma '{armita['nombre']}' en el equipamiento.")
            return


    personaje["equipamiento"].append(arma)
    print(f"El arma '{arma['nombre']}' ha sido añadida al equipamiento del personaje {nombre_personaje}.")


anadir_equipamiento("Aragorn", "Andúril")
anadir_equipamiento("Frodo", "Daga de Frodo")

