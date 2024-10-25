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

equipamiento = [{
    "nombre": ["Andúril", "Arco de Galadriel", "Hacha de Gimli", "Daga de Frodo", "Báculo de Saruman", "Anillo único", "Espada de Boromir"],
    "tipo": ["Arma", "Armadura", "Objeto especial", "Arco", "Hacha", "Daga", "Bastón"],
    "potencia": range(10,101)}]