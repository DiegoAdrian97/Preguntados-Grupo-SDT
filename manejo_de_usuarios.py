from file_system import *

def crear_usuario(datos: dict) -> dict:
    '''
    ¿Qué hace?: Permite al usuario crear un nuevo usuario con nombre y contraseña válidos.
    
    ¿Qué recibe?: Diccionario que contiene los datos de usuarios existentes.
    
    ¿Qué retorna?: Diccionario actualizado con el nuevo usuario.
    '''
    
    print("Debes tener en cuenta que tu nuevo usuario y contraseña deben contener mínimo 5 caracteres y no caracteres especiales.")
    
    nombre = input("Ingrese el nombre de usuario: ")
    while not nombre.isalnum() or len(nombre) < 5:
        if len(nombre) < 5:
            print("El nombre debe tener al menos 5 caracteres.")
        else:
            print("El nombre debe ser alfanumérico.")
        nombre = input("Intente nuevamente: ")
    
    # Verificar si el usuario ya existe
    for user in datos["usuarios"]:
        if user["nombre"] == nombre:
            print(f"El usuario '{nombre}' ya existe. Intente con otro nombre.")
            return datos

    # Solicitar contraseña válida
    contraseña = input("Ingrese la contraseña: ")
    while not contraseña.isalnum() or len(contraseña) < 5:
        if len(contraseña) < 5:
            print("La contraseña debe tener al menos 5 caracteres.")
        else:
            print("La contraseña no debe contener caracteres especiales.")
        contraseña = input("Intente nuevamente: ")

    # Crear y agregar el nuevo usuario
    nuevo_usuario = {
        "nombre": nombre,
        "contrasenia": contraseña,
        "puntuaciones": 0  # Ajustado según el JSON inicial
    }
    datos["usuarios"].append(nuevo_usuario)
    guardar_datos(datos)
    print("Se ha creado el usuario correctamente.")
    return datos