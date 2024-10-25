import random

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

def battle(p1, p2):
    if p1 in personajes and p2 in personajes:
        if personajes[p1]["arma_equipada"] != {} and personajes[p2]["arma_equipada"] != {}:
            print(f"{p1} y {p2} empiezan un combate")
            print(personajes[p1]["arma_equipada"]["tipo"])
            print("Tremendo golpe") if random.random() * 100 > 60 else ""
        else:
            print("Uno de los personajes no tiene arma equipada")
    else:
        print("Uno de los personajes no está en este universo")

battle("Aragorn", "Legolas")