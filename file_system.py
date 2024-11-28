import json

def leer_datos() -> dict:  
    '''
        ¿Que hace?: Lee los datos de los usuarios, y sus puntuaciones
        ¿Que recibe?: El JSON con los datos de los usuarios
        ¿Que retorna?: Diccionario con los usuarios leidos
    '''
    with open("./pygame/usuarios.json", "r") as archivo:
        users_data = json.load(archivo)
    return users_data
    
def guardar_datos(datos: dict) -> str:
    '''
        ¿Que hace?: Guarda los datos del nuevo usuario creado
        ¿Que recibe?: El JSON con los datos de los usuarios, los datos del nuevo usuario
        ¿Que retorna?: Nada.
    '''
    with open("./pygame/usuarios.json", "w") as archivo:
        json.dump(datos, archivo, ensure_ascii=False)

def eliminar_datos_previos(datos: dict) -> str:
    '''
        ¿Que hace?: Elimina los usuarios creados previamente
        ¿Que recibe?: El JSON de los usuarios y el diccionario datos vacío.
        ¿Que retorna?: Mensaje de OK
    '''
    with open("./pygame/usuarios.json","w") as archivo:
        json.dump(datos, archivo)
        
    mensaje = "\nPartidas eliminadas con exito."
    print(mensaje.center(60))
    
    return True


def cargar_preguntas() -> dict:
    '''
    ¿Que hace?: Carga las preguntas de la base de preguntas
    ¿Que recibe?: El JSON de las preguntas
    ¿Que retorna?: Diccionario con las preguntas
    '''
    with open("./pygame/preguntas.json", "r", encoding="utf-8") as archivo:
        data = json.load(archivo)
        preguntas = data.get("preguntas", {}) 
    return preguntas



def agregar_pregunta_a_archivo(categoria, nueva_pregunta) -> str:
    '''
        ¿Que hace?: Agrega una nueva pregunta a la base de preguntas
        ¿Que recibe?: El JSON de las preguntas y la pregunta a agregar
        ¿Que retorna?: Mensaje de OK
    '''
    with open("./pygame/preguntas.json", "r") as archivo:
        data = json.load(archivo)
        
    data["preguntas"][categoria].append(nueva_pregunta)
    with open("./pygame/preguntas.json", "w") as archivo:
        json.dump(data, archivo, indent=4, ensure_ascii=False)
        
    mensaje = "\nPregunta agregada con exito"
    
    print(mensaje.center(60))
    
    return mensaje