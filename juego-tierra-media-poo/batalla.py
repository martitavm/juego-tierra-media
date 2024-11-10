import random

class Batalla:
    @staticmethod
    def simular(p1, p2):
        arma_p1, prob_p1, potencia_p1, vida_p1 = preparacion(p1)
        arma_p2, prob_p2, potencia_p2, vida_p2 = preparacion(p2)
        # Comienza el combate
        print(f"\n-->{p1.nombre} ha insultado a la madre de {p2.nombre}, se vienen los problemas.")
        print(f"¡¡¡QUE COMIENCE EL DUELO!!!")
        print("----------------------------------------------")
        while vida_p1 or vida_p2:
            if random.random() < prob_p1 and vida_p1 > 0:
                print(f"{p1.nombre} golpea con su {arma_p1} a {p2.nombre}.")
                # print(f"{random.choice(frases_combate)}")
                print("----------------------------------------------")
                vida_p2 -= potencia_p1
            if random.random() < prob_p2 and vida_p2 > 0:
                print(f"{p2.nombre} golpea con su {arma_p2} a {p1.nombre}.")
                # print(f"{random.choice(frases_combate)}")
                print("----------------------------------------------")
                vida_p1 -= potencia_p2
            if vida_p1 <= 0:
                print(f"{p1.nombre} ha sido derrotado, {p2.nombre} GANA!\n")
                return
            if vida_p2 <= 0:
                print(f"{p2.nombre} ha sido derrotado, {p1.nombre} GANA!\n")
                return
            # Si se cumple esta condición uno de los personajes muere
            if random.random() < 0.02:
                print(f"{p1.nombre if random.random() < 0.5 else p2.nombre} ha sido golpeado por una abuela y ha fallecido.\n")
                return

def preparacion(pnj):
    """
    Función para asignar el arma, la probabilidad de golpear, la potencia
    y la vida a los personajes que van a combatir.
    :param pnj: Objeto de la clase Personaje
    :return: arma: Nombre del arma,
    probabilidad: Probabilidad de golpear del arma,
    potencia: Potencia del arma,
    vida: Vida para el personaje
    """
    if pnj.arma_equipada is None:
        arma = "Puño"
        probabilidad = 0.2
        potencia = 20
    else:
        arma = pnj.arma_equipada.nombre
        probabilidad = pnj.arma_equipada.probabilidad
        potencia = pnj.arma_equipada.potencia
    vida = 300
    return arma, probabilidad, potencia, vida