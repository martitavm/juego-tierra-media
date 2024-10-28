
dicc = {
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

#Personaje relacionado: Nombre del otro personaje.
#Tipo de relación: Amigo, Enemigo, Neutral.
#Nivel de confianza: (entero entre 1 y 10) Grado de confianza o enemistad.

tipos = ["Amigo", "Enemigo", "Neutral"]

def establecer_relaciones(dicc,personaje,personaje_relacion, tipo, nivel_confianza):

    # Verificar tipos de entrada
    if type(personaje) != str:
        print("Tipo de personaje incorrecto")
        return
    elif type(personaje_relacion) != str:
        print("Tipo de personaje-relación incorrecto")
        return
    elif tipo not in tipos:
        print("Tipo de relación inexistente, tipos: 'Amigo', 'Enemigo', 'Neutral'")
        return
    elif type(nivel_confianza) != int or not (nivel_confianza > 1 or nivel_confianza < 10):
        print("Nivel de confianza incorrecto, tiene que ser un número entre 1 y 10")
        return

    # Verificar que ambos personajes existen en el diccionario
    if personaje in dicc and personaje_relacion in dicc:

        # Buscar la relación en la lista de relaciones
        relacion_actualizada = False

        for relacion in dicc[personaje]["relaciones"]:

            if relacion["personaje"] == personaje_relacion:
                 # Si ya existe la relación, actualizamos
                relacion["tipo"] = tipo
                relacion["nivel_confianza"] = nivel_confianza
                relacion_actualizada = True
                print(f"Relación actualizada entre {personaje} y {personaje_relacion}")
                break

        # Si no se encontró la relación, agregar una nueva
        if not relacion_actualizada:
            nueva_relacion = {
                "personaje": personaje_relacion,
                "tipo": tipo,
                "nivel_confianza": nivel_confianza
            }
            dicc[personaje]["relaciones"].append(nueva_relacion)
            print(f"Relación nueva añadida entre {personaje} y {personaje_relacion}")

    else:
        print("Uno o ambos personajes no existen en el diccionario.")
establecer_relaciones(dicc,"Legolas","Aragorn","Amigo", 10)

print(dicc)