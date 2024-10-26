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
    frases_combate = ["Menudo golpe.",
                      "Justo en la coronilla.",
                      "Eso tiene que doler.",
                      "¿No estaba prohibido dar en los ojos?",
                      "Cuidado con el.... terraplén.",
                      "Corre insensato"]

    probabilidad_golpe = {"espada": 0.6, "arco": 0.5, "hacha": 0.55, "daga": 0.4}

    if p1 not in personajes:
        print(f"{p1} no está en estas tierras.")
        return
    if p2 not in personajes:
        print(f"{p2} no está en estas tierras.")
        return

    personaje1 = personajes[p1]
    arma_p1 = personaje1.get("arma_equipada")
    vida_p1 = 100
    prob_p1 = 100
    if not arma_p1:
        print(f"{p1} no tiene arma equipada.")
        return
    elif arma_p1["tipo"].lower() in probabilidad_golpe:
        prob_p1 = probabilidad_golpe[arma_p1["tipo"].lower()]

    personaje2 = personajes[p2]
    arma_p2 = personaje2.get("arma_equipada")
    vida_p2 = 100
    prob_p2 = 100
    if not arma_p2:
        print(f"{p2} no tiene arma equipada.")
        return
    elif arma_p2["tipo"].lower() in probabilidad_golpe:
        prob_p2 = probabilidad_golpe[arma_p2["tipo"].lower()]

    print(f"{p1} ha insultado a la madre de {p2}, se vienen los problemas.")
    while vida_p1 or vida_p2:
        if random.random() < prob_p1 and vida_p1 > 0:
            num_frase1 = random.randint(0,len(frases_combate)-1)
            print(f"{p1} golpea con su {arma_p1["tipo"]} a {p2}.")
            print(f"{frases_combate[num_frase1]}")
            print("----------------------------------------------")
            vida_p2 -= arma_p1["potencia"]
        if random.random() < prob_p2 and vida_p2 > 0:
            num_frase2 = random.randint(0, len(frases_combate) - 1)
            print(f"{p2} golpea con su {arma_p2["tipo"]} a {p1}.")
            print(f"{frases_combate[num_frase2]}")
            print("----------------------------------------------")
            vida_p1 -= arma_p2["potencia"]
        if vida_p1 <= 0:
            print(f"{p1} ha sido derrotado, {p2} GANA!")
            return
        if vida_p2 <= 0:
            print(f"{p2} ha sido derrotado, {p1} GANA!")
            return

(battle("Aragorn", "Legolas"))