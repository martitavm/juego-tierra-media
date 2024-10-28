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

frases_combate = ["Menudo golpe.",
                  "Justo en la coronilla.",
                  "Eso tiene que doler.",
                  "¿No estaba prohibido dar en los ojos?",
                  "Cuidado con el.... terraplén.",
                  "Corre insensato",
                  "¡Por la barba de Gandalf, eso duele!",
                  "Esto va a doler más que caminar descalzo hasta Mordor.",
                  "¡Por el hacha de Gimli, esto se pone intenso!",
                  "¡Por los rizos de Sam, esto se complica!",
                  "¡Por los pies peludos de Bilbo, vaya sacudida!",
                  "¡Por la calvicie de Gollum, eso fue brillante!",
                  "¿A quién se le ocurre apuntar al dedo meñique del pie?",
                  "¿En serio? ¿Otra vez en la cabeza?",
                  "¡Carambolas, dale caña ahí!"]

probabilidad_golpe = {"espada": 0.6, "arco": 0.5, "hacha": 0.55, "daga": 0.4}

def check_character_equip(personaje):
    arma = personaje.get("arma_equipada")
    if not arma:
        return {}, 100
    tipo_arma = arma["tipo"].lower()
    probabilidad = probabilidad_golpe.get(tipo_arma, 100)
    return arma, probabilidad

def battle(p1, p2):
    try:
        arma_p1, prob_p1 = check_character_equip(personajes[p1])
        vida_p1 = 100
        arma_p2, prob_p2 = check_character_equip(personajes[p2])
        vida_p2 = 100
        if arma_p1 == {} or arma_p2 == {}:
            print(f"{p1 if arma_p1 == {} else p2} no tiene un arma equipada.")
            return
        print(f"{p1} ha insultado a la madre de {p2}, se vienen los problemas.")
        while vida_p1 or vida_p2:
            if random.random() < prob_p1 and vida_p1 > 0:
                print(f"{p1} golpea con su {arma_p1["tipo"]} a {p2}.")
                print(f"{random.choice(frases_combate)}")
                print("----------------------------------------------")
                vida_p2 -= arma_p1["potencia"]
            if random.random() < prob_p2 and vida_p2 > 0:
                print(f"{p2} golpea con su {arma_p2["tipo"]} a {p1}.")
                print(f"{random.choice(frases_combate)}")
                print("----------------------------------------------")
                vida_p1 -= arma_p2["potencia"]
            if vida_p1 <= 0:
                print(f"{p1} ha sido derrotado, {p2} GANA!")
                return
            if vida_p2 <= 0:
                print(f"{p2} ha sido derrotado, {p1} GANA!")
                return
    except KeyError:
        print(f"{p1 if p1 not in personajes else p2} no está en estas tierras")
        return

def show_characters():
    for keys, values in personajes.items():
        print(f"Personaje: {keys}")
        for value, datos in values.items():
            print(f"-> {value.capitalize()}: {datos}")
        print("---------------------------------------")
    return

def show_character_equip(equipo):
    lista_personaje_equipado = []
    try:
        for keys, values in personajes.items():
            if equipo.lower() in values["equipamiento"][0]["nombre"].lower():
                lista_personaje_equipado.append(keys)
        if len(lista_personaje_equipado) == 0:
            print(f"Ningún personaje tiene {equipo}")
        else:
            print(f"Personajes con {equipo.capitalize()} \n{lista_personaje_equipado}")
        return
    except AttributeError:
        print("Introduce el nombre del equipo")



(battle("Aragorn", "Legolas"))
# show_characters()
#show_character_equip("Arco de Galadriel")
