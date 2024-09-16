# Trabajo practico GRUPO 8

# Variables externas
usuarios = {
    "admin": "admin123",
    "juan": "juan123",
}
administrador = {"nombre": "admin", "contrasena": "admin123"}
productos = []  #productos matriz (lista de listas)

# Inicio de sesion, verifica usuarios
def iniciar_sesion():
    nombre_usuario = input("Ingrese su nombre de usuario: ")
    contrasena = input("Ingrese su contraseña: ")
    #si el nombre ingresado esta en el diccionario y coincide con su key, inicia sesion
    if nombre_usuario in usuarios and usuarios[nombre_usuario] == contrasena:
        print(f"Inicio de sesión exitoso. Bienvenido, {nombre_usuario}.")
        return nombre_usuario
    else:
        print("Nombre de usuario o contraseña incorrectos.")
        return None

# Menú principal
def menu():
    usuario_actual = None
    # While infinito para menu
    while True:
        if usuario_actual is None: # si no hay un usuario conectado muestra el menu de inicio
            print("\n--- Menú de inicio de sesión ---")
            print("1. Iniciar sesión")
            print("2. Salir")
            opcion = input("Seleccione una opción (1-2): ")

            if opcion == "1":
                usuario_actual = iniciar_sesion() # ejecuta iniciar secion y verifica usuario y contraseña
            elif opcion == "2":
                print("Saliendo del programa.")
                break
            else:
                print("Opción no válida, intente de nuevo.")
        else: # si hay un usuario conectado te muestra el menu principal con las opciones para trabajar
            print(f"\n--- Menú principal (Usuario actual: {usuario_actual}) ---")
            print("1. Mostrar usuarios registrados")
            print("2. Buscar productos")
            print("3. Cargar venta")
            # si el usuario es el administrador podrá ver más opciones
            if usuario_actual == administrador["nombre"]:
                print("4. Modificar datos del administrador")
                print("5. Agregar/Modificar datos de productos")
                print("6. Registrar/Modificar usuarios")
            print("7. Cerrar sesión")

            opcion = input("Seleccione una opción (1-7): ")

            # Selección de opciones del menú
            if opcion == "1":
                mostrar_usuarios()
            elif opcion == "2":
                nombre_producto = input("Ingrese el nombre del producto a buscar: ")
                buscadorProductos(productos, nombre_producto)
            elif opcion == "3":
                pass
            elif opcion == "4" and usuario_actual == administrador["nombre"]:
                pass
            elif opcion == "5" and usuario_actual == administrador["nombre"]:
                Registrar_producto(productos)
            elif opcion == "6" and usuario_actual == administrador["nombre"]:
                registrarusuario()
            elif opcion == "7":
                usuario_actual = None
                print("Sesión cerrada.")
            else:
                print("Opción no válida.")

# Definimos mostrar usuarios
def mostrar_usuarios():
    print("\n--- Usuarios registrados ---")
    for usuario in usuarios:
        print(f"Usuario: {usuario}")

# Definimos cómo registrar usuarios
def registrarusuario():
    nombre = input("Ingrese el nombre del usuario: ")
    contraseña = input("Ingrese una contraseña: ")

    if nombre in usuarios:
        print("El usuario ya existe.")
    else:
        usuarios[nombre] = contraseña
        print("Usuario registrado con éxito.")

# Definimos cómo registrar productos (matriz)
def Registrar_producto(productos):
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    cantidad = int(input("Ingrese la cantidad del producto: "))
    codigo = input("Ingrese el código del producto: ")

    nuevo_producto = [nombre, precio, cantidad, codigo]  # Almacenamos en una lista (fila)
    productos.append(nuevo_producto)  # Agregamos la fila a la matriz

    print(f"Producto {nombre} registrado correctamente.")

# Definimos cómo buscar productos (matriz)
def buscadorProductos(productos, nombre):
    nombre = nombre.upper()
    encontrado = False

    for producto in productos:
        if nombre in producto[0].upper():  # Buscamos en el nombre del producto (columna 0)
            print(f"Producto encontrado: Nombre: {producto[0]}, Precio: {producto[1]}, Cantidad: {producto[2]}, Código: {producto[3]}")
            encontrado = True

    if not encontrado:
        print(f"Producto {nombre} no encontrado.")

# Funciones a desarrollar en la siguiente entrega
def modificarProducto():
    pass

def modifcarUsuario():
    pass

def facturacion():
    pass

def modAdmin():
    pass

def modDescuentos():
    pass

# Función descuentos a desarrollar en lambda
descuento = lambda x, y: x * y
recargo = lambda x, z: x * z

# Ejecutar el menú
menu()
