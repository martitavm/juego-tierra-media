



#Personaje relacionado: Nombre del otro personaje.
#Tipo de relación: Amigo, Enemigo, Neutral.
#Nivel de confianza: (entero entre 1 y 10) Grado de confianza o enemistad.

tipos = ["Amigo", "Enemigo", "Neutral"]

def establecer_relaciones(personajes):
    """
      Función para establecer o actualizar relaciones entre personajes.

      Solicita al usuario que ingrese el nombre de un personaje principal y otro personaje con el cual
      establecerá una relación.

      Entradas:
      - personaje (str): Nombre del personaje que establece la relación.
      - personaje_relacion (str): Nombre del personaje con el cual se establece la relación.
      - tipo (str): Tipo de relación entre personajes. Debe ser uno de los valores en `tipos`.
      - nivel_confianza (int): Nivel de confianza o enemistad en un rango de 1 a 10.

      Reglas de Validación:
      1. El nombre de los personajes deben ser cadenas de texto.
      2. El tipo de relación debe estar en `tipos`: 'Amigo', 'Enemigo' o 'Neutral'.
      3. El nivel de confianza debe ser un entero entre 1 y 10.

      """

    personaje = input("Ingrese el personaje que va a establecer una relacion")
    personaje_relacion = input("Ingrese el nombre del personaje a relacionar")
    tipo = input("Ingrese el tipo de relaciones: ")
    nivel_confianza = int(input("Indique el nivel de confianza: "))

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

    # Verificar que ambos personajes existen
    if personaje in personajes and personaje_relacion in personajes:


        relacion_actualizada = False

        for relacion in personajes[personaje]["relaciones"]:

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
            personajes[personaje]["relaciones"].append(nueva_relacion)
            print(f"Relación nueva añadida entre {personaje} y {personaje_relacion}")

    else:
        print("Uno o ambos personajes no existen en el diccionario.")


