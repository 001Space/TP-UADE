# Trabajo practico GRUPO 8

# Variables, listas, diccionarios y matrices globales
usuarios = [
    ["Juan", "Juan123", 130],  # [Nombre, Contraseña, N°Legajo]
    ["Pepe", "Pepe123", 140]
]

administrador = {"nombre": "admin", "contrasena": "admin123"}

#Productos es una matriz (lista de listas)
productos = [
    ["Manzana", 0.50, 100, "A001"],   # [nombre, precio, cantidad, código]
    ["Banana", 0.30, 150, "A002"],
    ["Naranja", 0.60, 200, "A003"]
]

# Inicio de sesion, verifica usuarios
def iniciar_sesion():
    nombre_usuario = input("Ingrese su nombre de usuario: ")
    contrasena = input("Ingrese su contraseña: ")

    # Verificamos si es un usuario registrado
    for usuario in usuarios:
        if usuario[0] == nombre_usuario and usuario[1] == contrasena:
            print(f"Inicio de sesión exitoso. Bienvenido, {nombre_usuario}.")
            return nombre_usuario

    # Verificamos si es el administrador
    if nombre_usuario == administrador["nombre"] and contrasena == administrador["contrasena"]:
        print(f"Inicio de sesión exitoso. Bienvenido, {nombre_usuario}.")
        return nombre_usuario

    # Si no es un usuario o administrador válido
    print("Nombre de usuario o contraseña incorrectos.")
    return None

# Menú principal
def menu():
    usuario_actual = None
    # While para menu
    while True:
        if usuario_actual is None:
            print("\n--- Menú de inicio de sesión ---")
            print("1. Iniciar sesión")
            print("2. Salir")
            opcion = input("Seleccione una opción (1-2): ")

            if opcion == "1":
                usuario_actual = iniciar_sesion()
            elif opcion == "2":
                print("Saliendo del programa.")
                break
            else:
                print("Opción no válida, intente de nuevo.")
        else:
            print(f"\n--- Menú principal (Usuario actual: {usuario_actual}) ---")
            print("1. Mostrar usuarios registrados")
            print("2. Buscar productos")
            print("3. Cargar venta")
            # Si el usuario es el administrador podrá ver más opciones
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
                criterio_busqueda = input("¿Desea buscar por (1) Nombre o (2) Código?: ")
                if criterio_busqueda == "1":
                    nombre_producto = input("Ingrese el nombre del producto a buscar: ")
                    buscadorProductos(productos, nombre_producto, "nombre")
                elif criterio_busqueda == "2":
                    codigo_producto = input("Ingrese el código del producto a buscar: ")
                    buscadorProductos(productos, codigo_producto, "codigo")
                else:
                    print("Opción de búsqueda no válida.")
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
        print(f"Nombre: {usuario[0]}, N°Legajo: {usuario[2]}")

#Definimos registro de usuarios
def registrarusuario():
    nombre = input("Ingrese el nombre del usuario: ")
    contraseña = input("Ingrese una contraseña: ")
    legajo = int(input("Ingrese el número de legajo del usuario: "))

    # Verificar si el usuario ya existe
    for usuario in usuarios:
        if usuario[0] == nombre:
            print("El usuario ya existe.")
            return

    # Registrar nuevo usuario
    nuevo_usuario = [nombre, contraseña, legajo]
    usuarios.append(nuevo_usuario)
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

# Definimos cómo buscar productos por nombre o código (matriz)
def buscadorProductos(productos, busqueda, criterio):
    busqueda = busqueda.upper()
    encontrado = False

    for producto in productos:
        if criterio == "nombre":
            if busqueda in producto[0].upper():  # Buscamos en el nombre del producto (columna 0)
                print(f"Producto encontrado: Nombre: {producto[0]}, Precio: {producto[1]}, Cantidad: {producto[2]}, Código: {producto[3]}")
                encontrado = True
        elif criterio == "codigo":
            if busqueda == producto[3].upper():  # Buscamos en el código del producto (columna 3)
                print(f"Producto encontrado: Nombre: {producto[0]}, Precio: {producto[1]}, Cantidad: {producto[2]}, Código: {producto[3]}")
                encontrado = True

    if not encontrado:
        if criterio == "nombre":
            print(f"Producto con nombre '{busqueda}' no encontrado.")
        elif criterio == "codigo":
            print(f"Producto con código '{busqueda}' no encontrado.")

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
