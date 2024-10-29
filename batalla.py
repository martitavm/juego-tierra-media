import random

personajes = {
    "Aragorn": {
        "raza": "Humano",
        "faccion": "La Comunidad del Anillo",
        "ubicacion": "Rivendel",
        "equipamiento": [
            {"nombre": "Andúril", "tipo": "Espada", "potencia": 80},
            {"nombre": "Arco de Galadriel"}
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

def campo_vacio(campo):
    """
    Función para comprobar que los campos que se introducen por teclado no están vacíos.
    :param campo: String introducido por teclado.
    :return: Excepcion si está vacio, string si no.
    """
    if campo == "":
        raise Exception("No puedes dejar vacío este campo")
    return campo

def check_character_equip(personaje):
    """
    Función que recibe un personaje del diccionario, comprueba su arma equipada
    y devuelve el arma y su probabilidad de golpear.
    :param personaje: String con nombre del personaje.
    :return: Diccionario con datos del arma y la probabilidad de golpear.
            En caso de no tener arma devuelve diccionario vacío y 100% de probabilidad.
    """
    arma = personaje.get("arma_equipada")
    if not arma:
        return {}, 1
    tipo_arma = arma["tipo"].lower()
    probabilidad = probabilidad_golpe.get(tipo_arma, 1)
    return arma, probabilidad

def battle():
    """
    Función que simula un combate entre dos personajes introducidos por teclado
    La función comprueba la existencia de esos personajes en el diccionario, asigna
    a los personajes una cantidad de vida, y su arma equipada con su probabilidad de golpear
    y devuelve el ganador del combate tras simularlo.
    :return: Ganador del combate.
    """
    p1, p2 = "", ""
    try:
        p1 = input("Nombre del primer combatiente: ").capitalize()
        campo_vacio(p1)
        p2 = input("Nombre del segundo combatiente: ").capitalize()
        campo_vacio(p2)
        # Asigno el arma, probabilidad de golpear y la vida a los personajes
        arma_p1, prob_p1 = check_character_equip(personajes[p1])
        vida_p1 = 300
        arma_p2, prob_p2 = check_character_equip(personajes[p2])
        vida_p2 = 300
        if arma_p1 == {} or arma_p2 == {}:
            print(f"{p1 if arma_p1 == {} else p2} no tiene un arma equipada.")
            return
        # Comienza el combate
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
            # Si se cumple esta condición uno de los personajes muere
            if random.random() < 0.05:
                print(f"{p1 if random.random() < 0.5 else p2} ha sido golpeado por una abuela y ha fallecido.")
                return
    except KeyError:
        print(f"{p1 if p1 not in personajes else p2} no está en estas tierras")
    except NameError:
        print("El diccionaro con datos no existe")
    except Exception as e:
        print(f"{e}")

def show_characters():
    """
    Función que recorre un diccionario de personajes y muestra todos sus datos.
    :return: Datos del diccionario recorrido.
    """
    try:
        for keys, values in personajes.items():
            print(f"Personaje: {keys}")
            for value, datos in values.items():
                print(f"-> {value.capitalize()}: {datos}")
            print("---------------------------------------")
        return
    except NameError:
        print("El diccionario con datos no existe")

def show_character_equip():
    """
    Función que muestra los personajes que tienen en su equipamiento el
    arma introducida por teclado.
    :return: Lista con los personajes que tienen el arma en su equipamiento.
    """
    lista_personaje_equipado = []
    try:
        equipo = input("Introduce el arma a buscar: ").lower()
        campo_vacio(equipo)

        for keys, values in personajes.items():
            for arma in values["equipamiento"]:
                if equipo in arma["nombre"].lower():
                    lista_personaje_equipado.append(keys)

        if len(lista_personaje_equipado) == 0:
            print(f"Ningún personaje tiene {equipo}")
        else:
            print(f"Personajes con {equipo.capitalize()} \n{lista_personaje_equipado}")
        return
    except AttributeError:
        print("Introduce el nombre del equipo")
    except NameError:
        print("El diccionario con datos no existe")
    except Exception as e:
        print(f"{e}")

# battle()
# show_characters()
# show_character_equip()