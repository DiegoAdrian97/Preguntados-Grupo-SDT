import random

# Preguntas organizadas por categorías 
preguntas = {
    "Geografía": [
        {
            "pregunta": "¿Cuál es el país más grande del mundo por superficie?",
            "opciones": ["Canadá", "Rusia", "China"],
            "respuesta": "B"
        },
        {
            "pregunta": "¿Cuál es el río más largo del mundo?",
            "opciones": ["Amazonas", "Nilo", "Yangtsé"],
            "respuesta": "A"
        },
        {
            "pregunta": "¿Dónde se encuentra el desierto del Sahara?",
            "opciones": ["Australia", "África", "Asia"],
            "respuesta": "B"
        },
        {
            "pregunta": "¿Cuál es la capital de Japón?",
            "opciones": ["Seúl", "Tokio", "Kioto"],
            "respuesta": "B"
        },
        {
            "pregunta": "¿En qué continente está Argentina?",
            "opciones": ["América", "Europa", "Oceanía"],
            "respuesta": "A"
        }
    ],
    "Ciencias": [
        {
            "pregunta": "¿Qué planeta es conocido como el planeta rojo?",
            "opciones": ["Marte", "Venus", "Júpiter"],
            "respuesta": "A"
        },
        {
            "pregunta": "¿Cuál es el elemento químico más abundante en la atmósfera?",
            "opciones": ["Oxígeno", "Nitrógeno", "Hidrógeno"],
            "respuesta": "B"
        },
        {
            "pregunta": "¿Cuál es la fórmula química del agua?",
            "opciones": ["CO2", "H2O", "NaCl"],
            "respuesta": "B"
        },
        {
            "pregunta": "¿Qué órgano es responsable de bombear la sangre?",
            "opciones": ["Pulmones", "Cerebro", "Corazón"],
            "respuesta": "C"
        },
        {
            "pregunta": "¿Qué tipo de animal es un delfín?",
            "opciones": ["Pez", "Mamífero", "Anfibio"],
            "respuesta": "B"
        }
    ],
    "Conocimiento General": [
        {
            "pregunta": "¿Cuál es el idioma más hablado en el mundo?",
            "opciones": ["Español", "Inglés", "Mandarín"],
            "respuesta": "C"
        },
        {
            "pregunta": "¿Cuántos días tiene un año bisiesto?",
            "opciones": ["366", "365", "364"],
            "respuesta": "A"
        },
        {
            "pregunta": "¿Cuál es el símbolo químico del oro?",
            "opciones": ["Au", "Ag", "Fe"],
            "respuesta": "A"
        },
        {
            "pregunta": "¿Cuál es la moneda de Japón?",
            "opciones": ["Yen", "Won", "Yuan"],
            "respuesta": "A"
        },
        {
            "pregunta": "¿Quién escribió 'Cien años de soledad'?",
            "opciones": ["Pablo Neruda", "Gabriel García Márquez", "Isabel Allende"],
            "respuesta": "B"
        }
    ],
    "Historia": [
        {
            "pregunta": "¿En qué año comenzó la Segunda Guerra Mundial?",
            "opciones": ["1939", "1941", "1945"],
            "respuesta": "A"
        },
        {
            "pregunta": "¿Quién fue el primer presidente de los Estados Unidos?",
            "opciones": ["Abraham Lincoln", "Thomas Jefferson", "George Washington"],
            "respuesta": "C"
        },
        {
            "pregunta": "¿En qué país se originó el Renacimiento?",
            "opciones": ["Francia", "Italia", "Alemania"],
            "respuesta": "B"
        },
        {
            "pregunta": "¿Quién fue el líder de la revolución rusa de 1917?",
            "opciones": ["Lenin", "Stalin", "Trotsky"],
            "respuesta": "A"
        },
        {
            "pregunta": "¿Qué civilización construyó las pirámides de Giza?",
            "opciones": ["Romanos", "Mayas", "Egipcios"],
            "respuesta": "C"
        }
    ],
    "Deportes": [
        {
            "pregunta": "¿En qué deporte se usa una pelota y un bate?",
            "opciones": ["Cricket", "Tenis", "Fútbol"],
            "respuesta": "A"
        },
        {
            "pregunta": "¿Quién tiene el récord de más goles en una Copa del Mundo?",
            "opciones": ["Pelé", "Miroslav Klose", "Cristiano Ronaldo"],
            "respuesta": "B"
        },
        {
            "pregunta": "¿Dónde se originó el rugby?",
            "opciones": ["Inglaterra", "Francia", "Sudáfrica"],
            "respuesta": "A"
        },
        {
            "pregunta": "¿Cuántos jugadores hay en un equipo de baloncesto en la cancha?",
            "opciones": ["5", "6", "11"],
            "respuesta": "A"
        },
        {
            "pregunta": "¿Cuál es el torneo de tenis más antiguo del mundo?",
            "opciones": ["Roland Garros", "Wimbledon", "US Open"],
            "respuesta": "B"
        }
    ]
}


def elegir_pregunta_aleatoria():
    '''
    ¿Que hace?: Selecciona aleatoriamente una categoría de preguntas y luego elige aleatoriamente una pregunta dentro de esa categoría.
    ¿Que recibe?: No recibe nada, pero utiliza el diccionario de preguntas, opciones y respuestas.
    ¿Que retorna?:
        - categoria (str): El nombre de la categoría seleccionada aleatoriamente.
        - pregunta_aleatoria (dict) La pregunta elegida aleatoriamente dentro de la categoría, que incluye el texto de la pregunta, las opciones y la respuesta correcta.
    '''
    categoria = random.choice(list(preguntas.keys()))
    pregunta_aleatoria = random.choice(preguntas[categoria])
    return categoria, pregunta_aleatoria

def mostrar_pregunta(pregunta):
    '''
    ¿Que hace?: Muestra en pantalla el texto de la pregunta, sus opciones (A, B o C) y define si es correcta o no lo es.
    ¿Que recibe?:      
            - pregunta (dict): Un diccionario con: pregunta["pregunta"] El texto de la pregunta (str), pregunta["opciones"]: Una lista de opciones de respuesta (list de str), pregunta["respuesta"]: La respuesta correcta (str).
    ¿Que retorna?: -
    '''
    print("Pregunta:", pregunta["pregunta"])

    # Lista de letras para las opciones
    letras_opciones = ["A", "B", "C"]
    
    # Bucle for para asociar una letra con una opcion
    for i in range(len(pregunta["opciones"])):
        letra = letras_opciones[i]
        opcion = pregunta["opciones"][i]
        print(f"{letra}. {opcion}")
    
    respuesta_usuario = input("Elige una opción (A, B o C): ").upper()
    while respuesta_usuario not in letras_opciones:
        respuesta_usuario = input("Opción inválida. Por favor, elige A, B o C: ").upper()
    
    indice = letras_opciones.index(respuesta_usuario)
    if pregunta["opciones"][indice] == pregunta["opciones"][letras_opciones.index(pregunta["respuesta"])]:
        print("Tu respuesta es... ¡CORRECTA!")
    else:
        print("Tu respuesta es... Incorrecta. La respuesta era la opción", pregunta["respuesta"])
        

categoria, pregunta = elegir_pregunta_aleatoria()
print("Categoria: ", categoria)
mostrar_pregunta(pregunta)