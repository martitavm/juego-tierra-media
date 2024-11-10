# Juego Tierra Media
> Bienvenidos al Juego de la Tierra Media, donde puedes manejar a personajes de la 
Tierra Media y darles una vida llena de acción, drama y un equipamiento de lujo.
> 
> En este programa podremos crear personajes, añadirles equipamiento, ver batallas épicas 
**(cuidado con la abuela)** y establecer relaciones entre ellos entre otras opciones.  
> 
> Este trabajo ha sido realizado por los Nazgûls:  
> - *Ana Morillo Troya*
> - *Ismael Capote Benítez*  
> - *Marta Villanueva Magán*  
> - *Alejandro Morillo Troya*



## Descripción del Proyecto
El Juego Tierra Media es un proyecto migrado a una arquitectura de Programación Orientada a Objetos (POO), con el objetivo de mejorar la organización, modularidad y escalabilidad del código. En este juego, los jugadores pueden gestionar personajes, equipamientos y relaciones en un mundo inspirado en la Tierra Media, incluyendo funciones como simulación de batallas y movimientos estratégicos.

## Estructura del Proyecto:  
Para este programa hemos creado una única carpeta llamada 
`juego-tierra-media-poo` que contiene varios ficheros `.py`.  
De entre esos ficheros, el más relevante es el fichero `menu_principal.py` ya que en él hemos importado todas
las funcionalidades que los integrantes del grupo han hecho en sus respectivos ficheros y también es donde
se encuentra el menú principal para ejecutar el programa en su totalidad. 

El resto de ficheros son:  
- `equipamiento.py`: Este fichero contiene la Equipamiento y dos subclases: Arma y Armadura.  
- `juego_tierra_media.py`: Este fichero es el más importante ya que lleva la clase JuegoTierraMedia, que es el controlador principal del juego y 
  alberga la gran mayoría de funciones que van a ser llamadas por menu_principal. 
- `personaje.py`: Este fichero contiene la clase Personaje con sus respectivos atributos y con algunas funciones.
- `Relacion.py`: Este fichero contiene la clase Relacion.
- `batalla.py`: Este fichero contiene la clase Batalla y la función batalla.


El proyecto cuenta con las siguientes clases principales (mencionadas anteriormente), cada una con atributos y métodos específicos para cubrir las funcionalidades descritas:

### Clase Personaje

- Atributos: nombre, raza, faccion, ubicacion, equipamiento, relaciones, arma_equipada
- Métodos: añadir_equipamiento, equipar_arma, establecer_relacion, mover, obtener_potencia_arma
### Clase Equipamiento

- Atributos: nombre, tipo, potencia
- Método: es_arma

### Clase Relacion

- Atributos: personaje, tipo, nivel_confianza
### Clase Batalla

- Método Estático: simular, que permite simular una batalla entre dos personajes y determina al ganador según su potencia de arma y probabilidades
### Clase JuegoTierraMedia (Controlador Principal)

- Atributos: personajes, facciones
- Métodos: registrar_personaje, añadir_equipamiento, establecer_relacion, mover_personaje, listar_personajes_por_faccion, buscar_personaje_por_equipamiento, mostrar_todos_personajes, salir


## Funcionalidades del Programa:
| **Función**                             | **Descripción**                                                              | **Ejemplo de uso**                                                                                                |
|-----------------------------------------|------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| **registrar_personaje()**           | Permite registrar un personaje                                               | **resgistrar_personaje()** Pedirá nombre, raza, facción y ubicación al usuario                          |
| **anadir_equipamiento(nombre_personaje, nombre_arma)**           | Añade armas al inventario del personaje (permite crear nuevas armas)         | **anadir_equipamiento(nombre_personaje, nombre_arma)** Pedirá nombre del personaje y arma a añadir de una lista                      |
| **equipar_arma(arma)**                  | Permite equipar un arma al personaje de las que tiene en su equipamiento     | **equipar_arma(arma)** Pedirá nombre del personaje y arma de su inventario a equipar                        |
| **establecer_relaciones(personajes)**         | Permite crear vínculos entre dos personajes                                  | **establecer_relaciones(personajes)** Pedirá nombre de los personajes a relacionar entre sí y el tipo de relación |
| **nueva_localizacion(personajes)**            | Mueve un personaje a una nueva ubicación (permite crear nuevas ubicaciones)  | **nueva_localizacion(personajes)** Pedirá el personaje y la ubicación a la que se va a mover                      |
| **simular_batalla(p1, p2)**               | Simula una batalla entre dos personajes                                      | **simular_batalla(p1, p2)** Pedirá los nombres de los personajes que van a combatir                           |
| **listar_personaje_faccion()**      | Muestra por pantalla los personajes que pertenecen a una facción en concreto | **listar_personaje_faccion()** Pedirá el nombre de una facción para listar sus integrantes              |
| **buscar_personaje_equipamiento(nombre_equipo)** | Devuelve los nombres de los propietarios de un arma en específico            | **buscar_personaje_equipamiento(nombre_equipo)** Pedirá el nombre de un arma para listar sus propietarios            |
| **mostrar_personajes()**            | Lista todos los personajes del diccionario                                   | **mostrar_personajes()** Lista todos los personajes del diccionario                                     |
| **obtener_potencia_arma(_arma_equipada)**            | Permite obtener la potencia del arma equipada del personaje                                   | **obtener_potencia_arma(_arma_equipada)** Devuelve la potencia del arma equipada.                                     |
| **buscar_arma(nombre_arma)**            | Busca un arma en la lista de equipamiento usando su nombre exacto                                   | **buscar_arma(nombre_arma)** Devuelve el arma si la encuentra.                        |
| **ampliar_equipamiento()**            | Permite a los moderadores añadir un nuevo arma al equipamiento                                  | **ampliar_equipamiento()** Preguntará si eres moderador o no y dejará añadir equipamiento.                       |
| **buscar_arma_equipamiento(nombre_arma)**            | Busca un arma específica en el equipamiento de un personaje.                                  | **buscar_arma_equipamiento(nombre_arma)** Buscará el arma específica en el equipamiento.                       |
| **elegir_arma_a_equipar(personaje)**            | Permite elegir que arma equipar al personaje.                                 | **elegir_arma_a_equipar(personaje)** Lista todas las armas en equipamiento y deja elegir cual arma quieres equipar.                      |
| **es_arma(equipo)**            | Comprueba si el parámetro dado es un arma o no.                                 | **es_arma(equipo)** Devuelve true o false dependiendo de si el parámetro dado es un arma o no.                      |
| **salir()**            | Permite salir del juego                                   | **salir()** Al elegir esta opción acabará el flujo del programa                                     |


## Uso del Menú Interactivo:
```
--- Menú de Gestión de la Tierra Media ---
1. Registrar un nuevo personaje
2. Añadir equipamiento a un personaje
3. Equipar un arma a un personaje
4. Establecer relaciones entre personajes
5. Mover un personaje a una nueva localización
6. Simular una batalla entre dos personajes
7. Listar personajes por facción
8. Buscar personajes por equipamiento
9. Mostrar todos los personajes
10. Salir
---Selecciona una de las opciones jugador/a --->
```
El menú consta de 10 opciones, cada una de las opciones llevará a cabo las tareas descritas anteriormente.  
Para navegar a través del menú simplemente introduciremos los números indicados a la izquierda de cada apartado
y posteriormente nos pedirá los datos necesarios para realizar la tarea indicada.

A continuación mostramos un ejemplo de flujo de uso para equipar un arma a un personaje (Opción 3):  
>1. Seleccionamos la opción número 3 introduciendo por teclado el número y presionando **Intro**.
>2. El programa mostrará un mensaje indicando que ya estás dentro del apartado 3.
>3. Ahora nos pedirá introducir el nombre del personaje al que queremos equipar un arma.
>4. Introducimos el nombre del personaje por teclado y si está en nuestro diccionario nos mostrará su equipamiento.
>En caso contrario, nos indicará que el personaje no existe y volverá al menú principal.
>5. Tras mostrar el equipamiento, nos pedirá introducir el nombre del arma que queremos equipar al personaje.
>Si se elige un arma que ya está equipada nos avisará de ello, y si el arma no está en su equipamiento también.
>6. Si el arma existe, será equipada al personaje, nos mostrará un mensaje confirmando que se ha equipado 
>correctamente y nos redirigirá al menú de opciones.
>7. Si ya no se desea realizar ninguna tarea más, introducimos el número 10 y salimos del programa.

Los pasos serían los mismos con el resto de opciones, cambiando únicamente los datos necesarios para cada función.
## Manejo de Errores:
Para manejos de errores hemos llevado a cabo diferentes estrategias:
- Manejo de excepciones (incluyendo de excepciones propias).
- Creación de métodos adicionales para prevenir errores.
- Uso de funciones built-in como `lower()`, `capitalize()` o `upper()`.
- Estructuras condicionales para verificaciones.

### Manejo de excepciones
Hemos trabajado con estructuras `Try-Except` para controlar errores como `ValueError`, `KeyError` y 
`AttributeError`, la mayoría para evitar problemas a la hora de introducir datos por teclado.  
Además, hemos creado excepciones propias para controlar que el dato introducido no esté vacío, esta
excepción es llamada `campo_vacio_exception(entrada)`

### Métodos adicionales
Hemos creado métodos adicionales (mencionados en funcionalidades) para verificar la existencia de personajes, armas, ubicaciones...  
Un ejemplo de estos métodos mencionados sería `buscar_arma(nombre_arma)` el cual comprueba si un arma
existe en el equipamiento de un personaje antes de añadirlo al inventario.

### Uso de funciones built-in
Hemos usado las funciones mencionadas anteriormente para comparar datos introducidos con los datos del
diccionario y asi realizar las funciones evitando errores de escritura.

### Estructuras condicionales
Por último hemos realizado control de algunos errores evitando que se produzcan a través de bloques
condicionales que nos devuelve un mensaje de aviso si algo ha ido mal.

## Trabajo en Equipo:
### Flujo de trabajo en GitHub
Para la realización de este proyecto cada integrante del grupo ha ido trabajando individualmente en las
funcionalidades que se le asignaron y una vez que tenía esa funcionalidad completa se realizaba un `commit`
y `push`, para posteriormente realizar un `pull-request`, resolver los conflictos pertinentes y una vez revisado
el código y corregido los conflictos realizar `merge` con la rama main.  
Una vez realizado merge con la rama main, cada uno de los integrantes en su IDE particular lleva a cabo un
`pull` de la rama main para tener todos los cambios hasta el momento.  
Este flujo se ha realizado hasta asegurarnos de que el proyecto funciona correctamente según los criterios establecidos.

### Enlaces
[Enlace a Pull Requests del proyecto](https://github.com/martitavm/juego-tierra-media/pulls?q=is%3Apr+is%3Aclosed)
### Trabajo por miembro
|                                   |   Ana    |  Ismael  |  Marta   | Alejandro |
|-----------------------------------|:--------:|:--------:|:--------:|:---------:|
| Menú                              |  &#x2714;|          | &#x2714; |&#x2714;   |
| Registrar Personaje               |          |          | &#x2714; |           |
| Añadir Equipamiento               | &#x2714; |          |          |           |
| Equipar Arma                      | &#x2714; |          |          |           |
| Establecer Relaciones             |          |    -     |          |           |
| Nueva Localización                |          |    -     |          |           |
| Simular Batalla                   |          |          |          | &#x2714;  |
| Listar Personajes por Facción     |          |          | &#x2714; |           |
| Buscar Personaje por Equipamiento |          |          |          | &#x2714;  |
| Mostrar Personajes                |          |          |          | &#x2714;  |
| obtener_potencia_arma             |          | &#x2714; |          |           |
| es_arma                           |          |          |          | &#x2714;  |
| Clase JuegoTierraMedia            |          |          | &#x2714; |           |
| Clase Personaje                   |          |          | &#x2714; |           |
| Clase Equipamiento                |&#x2714;  |          |          |           |
| Clase Batalla                     |          |          |          | &#x2714;  |
| Clase Relacion                    |          | &#x2714; |          |           |
| Documentación                     | &#x2714; |          | &#x2714; |           |

![](forodo.gif)
=======
# Juego Tierra Media
> Bienvenidos al Juego de la Tierra Media, donde puedes manejar a personajes de la 
Tierra Media y darles una vida llena de acción, drama y un equipamiento de lujo.
> 
> En este programa podremos crear personajes, añadirles equipamiento, ver batallas épicas 
**(cuidado con la abuela)** y establecer relaciones entre ellos entre otras opciones.  
> 
> Este trabajo ha sido realizado por los Nazgûls:  
> - *Ana Morillo Troya*
> - *Ismael Capote Benítez*  
> - *Marta Villanueva Magán*  
> - *Alejandro Morillo Troya*


## Estructura del Proyecto:  
Para este programa hemos creado una única carpeta llamada 
`juego-tierra-media` que contiene varios ficheros `.py`.  
De entre esos ficheros, el más relevante es el fichero `menu.py` ya que en él hemos importado todas
las funcionalidades que los integrantes del grupo han hecho en sus respectivos ficheros y también es donde
se encuentra el menú principal para ejecutar el programa en su totalidad. 

El resto de ficheros son:  
- `registrar_personaje.py`: Este fichero contiene las funciones necesarias para agregar un personaje correctamente.
- `anadir_equipamiento_personaje.py`: Este fichero incluye la función para añadir equipamiento a un personaje existente
así como funciones extras para evitar errores.
- `equipar_arma.py`: Este fichero permite importa la función de equipar un arma del equipo de un personaje para luchar.
- `establecer_relaciones.py`: Este fichero contiene la función que nos permite relacionar los personajes entre sí.
- `nueva_localizacion.py`: En este fichero puedes encontrar la función que permite a los personajes cambiar de localización.
- `batalla.py`: Este fichero contiene varias funciones, concretamente, la función para realizar batallas entre dos personajes,
la función para listar a todos los personajes y la función para listar los propietarios de un arma específica.
- `listar_personaje_faccion.py`: Este fichero incluye la función que nos permite listar los personajes que pertenecen a una
facción específica.



## Funcionalidades del Programa:
| **Función**                             | **Descripción**                                                              | **Ejemplo de uso**                                                                                                |
|-----------------------------------------|------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| **registrar_personaje(dict)**           | Permite registrar un personaje                                               | **resgistrar_personaje(personajes)** Pedirá nombre, raza, facción y ubicación al usuario                          |
| **anadir_equipamiento(dict)**           | Añade armas al inventario del personaje (permite crear nuevas armas)         | **anadir_equipamiento(personajes)** Pedirá nombre del personaje y arma a añadir de una lista                      |
| **equipar_arma(dict)**                  | Permite equipar un arma al personaje de las que tiene en su equipamiento     | **equipar_arma(personajes)** Pedirá nombre del personaje y arma de su inventario a equipar                        |
| **establecer_relaciones(dict)**         | Permite crear vínculos entre dos personajes                                  | **establecer_relaciones(personajes)** Pedirá nombre de los personajes a relacionar entre sí y el tipo de relación |
| **nueva_localizacion(dict)**            | Mueve un personaje a una nueva ubicación (permite crear nuevas ubicaciones)  | **nueva_localizacion(personajes)** Pedirá el personaje y la ubicación a la que se va a mover                      |
| **simular_batalla(dict)**               | Simula una batalla entre dos personajes                                      | **simular_batalla(personajes)** Pedirá los nombres de los personajes que van a combatir                           |
| **listar_personaje_faccion(dict)**      | Muestra por pantalla los personajes que pertenecen a una facción en concreto | **listar_personaje_faccion(personajes)** Pedirá el nombre de una facción para listar sus integrantes              |
| **buscar_personaje_equipamiento(dict)** | Devuelve los nombres de los propietarios de un arma en específico            | **buscar_personaje_equipamiento(personajes)** Pedirá el nombre de un arma para listar sus propietarios            |
| **mostrar_personajes(dict)**            | Lista todos los personajes del diccionario                                   | **mostrar_personajes(personajes)** Lista todos los personajes del diccionario                                     |

Nota:  
Para los ejemplos de uso indicamos los inputs que recibimos del usuario y nos referimos con "personajes" a un diccionario estructurado de la siguiente forma:
```
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
```
## Uso del Menú Interactivo:
```
--- Menú de Gestión de la Tierra Media ---
1. Registrar un nuevo personaje
2. Añadir equipamiento a un personaje
3. Equipar un arma a un personaje
4. Establecer relaciones entre personajes
5. Mover un personaje a una nueva localización
6. Simular una batalla entre dos personajes
7. Listar personajes por facción
8. Buscar personajes por equipamiento
9. Mostrar todos los personajes
10. Salir
---Selecciona una de las opciones jugador/a --->
```
El menú consta de 10 opciones, cada una de las opciones llevará a cabo las tareas descritas anteriormente.  
Para navegar a través del menú simplemente introduciremos los números indicados a la izquierda de cada apartado
y posteriormente nos pedirá los datos necesarios para realizar la tarea indicada.

A continuación mostramos un ejemplo de flujo de uso para equipar un arma a un personaje (Opción 3):  
>1. Seleccionamos la opción número 3 introduciendo por teclado el número y presionando **Intro**.
>2. El programa mostrará un mensaje indicando que ya estás dentro del apartado 3.
>3. Ahora nos pedirá introducir el nombre del personaje al que queremos equipar un arma.
>4. Introducimos el nombre del personaje por teclado y si está en nuestro diccionario nos mostrará su equipamiento.
>En caso contrario, nos indicará que el personaje no existe y volverá al menú principal.
>5. Tras mostrar el equipamiento, nos pedirá introducir el nombre del arma que queremos equipar al personaje.
>Si se elige un arma que ya está equipada nos avisará de ello, y si el arma no está en su equipamiento también.
>6. Si el arma existe, será equipada al personaje, nos mostrará un mensaje confirmando que se ha equipado 
>correctamente y nos redirigirá al menú de opciones.
>7. Si ya no se desea realizar ninguna tarea más, introducimos el número 10 y salimos del programa.

Los pasos serían los mismos con el resto de opciones, cambiando únicamente los datos necesarios para cada función.
## Manejo de Errores:
Para manejos de errores hemos llevado a cabo diferentes estrategias:
- Manejo de excepciones (incluyendo de excepciones propias).
- Creación de métodos adicionales para prevenir errores.
- Uso de funciones built-in como `lower()`, `capitalize()` o `upper()`.
- Estructuras condicionales para verificaciones.

### Manejo de excepciones
Hemos trabajado con estructuras `Try-Except` para controlar errores como `ValueError`, `KeyError` y 
`AttributeError`, la mayoría para evitar problemas a la hora de introducir datos por teclado.  
Además, hemos creado excepciones propias para controlar que el dato introducido no esté vacío, esta
excepción es llamada `campo_vacio_exception(entrada)`

### Métodos adicionales
Hemos creado métodos adicionales para verificar la existencia de personajes, armas, ubicaciones...  
Un ejemplo de estos métodos mencionados sería `buscar_arma(nombre_arma)` el cual comprueba si un arma
existe en el equipamiento de un personaje antes de añadirlo al inventario.

### Uso de funciones built-in
Hemos usado las funciones mencionadas anteriormente para comparar datos introducidos con los datos del
diccionario y asi realizar las funciones evitando errores de escritura.

### Estructuras condicionales
Por último hemos realizado control de algunos errores evitando que se produzcan a través de bloques
condicionales que nos devuelve un mensaje de aviso si algo ha ido mal.

## Trabajo en Equipo:
### Flujo de trabajo en GitHub
Para la realización de este proyecto cada integrante del grupo ha ido trabajando individualmente en las
funcionalidades que se le asignaron y una vez que tenía esa funcionalidad completa se realizaba un `commit`
y `push`, para posteriormente realizar un `pull-request`, resolver los conflictos pertinentes y una vez revisado
el código y corregido los conflictos realizar `merge` con la rama main.  
Una vez realizado merge con la rama main, cada uno de los integrantes en su IDE particular lleva a cabo un
`pull` de la rama main para tener todos los cambios hasta el momento.  
Este flujo se ha realizado hasta asegurarnos de que el proyecto funciona correctamente según los criterios establecidos.

### Enlaces
[Enlace a Pull Requests del proyecto](https://github.com/martitavm/juego-tierra-media/pulls?q=is%3Apr+is%3Aclosed)
### Trabajo por miembro
|                                   |   Ana    |  Ismael  |  Marta   | Alejandro |
|-----------------------------------|:--------:|:--------:|:--------:|:---------:|
| Menú                              |          |          | &#x2714; |           |
| Resgistrar Personaje              |          |          | &#x2714; |           |
| Añadir Equipamiento               | &#x2714; |          |          |           |
| Equipar Arma                      | &#x2714; |          |          |           |
| Establecer Relaciones             |          | &#x2714; |          |           |
| Nueva Localización                |          | &#x2714; |          |           |
| Simular Batalla                   |          |          |          | &#x2714;  |
| Listar Personajes por Facción     |          |          | &#x2714; |           |
| Buscar Personaje por Equipamiento |          |          |          | &#x2714;  |
| Mostrar Personajes                |          |          |          | &#x2714;  |
| Documentación                     | &#x2714; |          |          | &#x2714;  |

![](forodo.gif)
