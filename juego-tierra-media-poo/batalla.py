import random

class Batalla:
    @staticmethod
    def simular(p1, p2):
        arma_p1 = "Puño" if p1.arma_equipada is None else p1.arma_equipada.nombre
        prob_p1, vida_p1 = 0.6, 300
        arma_p2, prob_p2, vida_p2 = p2.arma_equipada.nombre, 0.6, 300
        # Comienza el combate
        print(f"\n-->{p1} ha insultado a la madre de {p2}, se vienen los problemas.")
        print(f"¡¡¡QUE COMIENCE EL DUELO!!!")
        print("----------------------------------------------")
        while vida_p1 or vida_p2:
            if random.random() < prob_p1 and vida_p1 > 0:
                print(f"{p1.nombre} golpea con su {arma_p1} a {p2.nombre}.")
                # print(f"{random.choice(frases_combate)}")
                print("----------------------------------------------")
                vida_p2 -= 20
            if random.random() < prob_p2 and vida_p2 > 0:
                print(f"{p2.nombre} golpea con su {arma_p2} a {p1.nombre}.")
                # print(f"{random.choice(frases_combate)}")
                print("----------------------------------------------")
                vida_p1 -= 20
            if vida_p1 <= 0:
                print(f"{p1.nombre} ha sido derrotado, {p2.nombre} GANA!")
                return
            if vida_p2 <= 0:
                print(f"{p2.nombre} ha sido derrotado, {p1.nombre} GANA!")
                return
            # Si se cumple esta condición uno de los personajes muere
            if random.random() < 0.02:
                print(f"{p1.nombre if random.random() < 0.5 else p2.nombre} ha sido golpeado por una abuela y ha fallecido.")
                return