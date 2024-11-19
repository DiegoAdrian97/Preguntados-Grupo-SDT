from file_system import *

def crear_usuario(datos: dict) -> dict:
    """
    ¿Qué hace?: permite al usuario crear un usuario y contraseña para ingresar al sistema.
    ¿Qué recibe?: Recibe una lista que contendrá los datos del usuario en modo diccionario.
    ¿Qué retorna?: Retorna el diccionario con los datos de los usuarios.
    """
    print("Debes tener en cuenta que tu nuevo usuario y contraseña deben contener mínimo 5 caracteres y no caracteres especiales.")
    
    nombre = input("Ingrese el nombre de usuario: ")
    while not nombre.isalnum() or len(nombre) < 5:  
        if len(nombre) < 5:
            nombre = input("Debe contener más de 5 caracteres, intente nuevamente: ")
        else:
            nombre = input("Intente nuevamente, el nombre debe ser alfanumérico: ")

    contraseña = input("Ingresa la contraseña del usuario: ")
    while not contraseña.isalnum() or len(contraseña) < 5: 
        if len(contraseña) < 5:
            contraseña = input("La contraseña debe contener más de 5 caracteres, intente nuevamente: ")
        else:
            contraseña = input("No se permiten caracteres especiales, intente nuevamente: ")
    
    usuario = {
        "nombre": nombre,
        "contrasenia": contraseña,
        "puntuacion": 0
    }
    for user in datos["usuarios"]:
        if user["nombre"] == nombre:
            print("Ya existe un usuario con ese nombre")
            return
        else:
            datos["usuarios"].append(usuario)
            
    guardar_datos(datos)
    
    mensaje = print("Se ha creado el usuario correctamente")
    return mensaje
    

    
def iniciar_sesion(datos: dict) -> str:
    """
    ¿Qué hace?: Permite al usuario intentar iniciar sesión con su nombre de usuario y contraseña.
    ¿Qué recibe?: Recibe la lista de usuarios creada por la función crear_usuario.
    ¿Qué retorna?: Retorna un mensaje dependiendo si el inicio de sesión fue exitoso o no.
    """
    

    usuarios = datos.get("usuarios")
    while True:
        nombre = input("Ingrese su nombre de usuario: ")
        contrasenia = input("Ingrese su contraseña: ")

        for jugador in usuarios:
            if jugador.get("nombre") != nombre:
                continue

            # Si estamos aquí, el nombre coincide. Validamos la contraseña
            if jugador.get("contrasenia") != contrasenia:
                print("Contraseña incorrecta. Intente nuevamente.")
                break 

            print("¡Sesión iniciada correctamente!")
            return datos

        print("Usuario no encontrado. Por favor, intente nuevamente.")