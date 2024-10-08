
# Función para cargar los datos del administrador desde el archivo CSV
def cargar_datos_administrador():
    try:
        with open("administrador.csv", "r") as archivo:
            nombre, contrasena = archivo.readline().strip().split(",")
            return {"nombre": nombre, "contrasena": contrasena}
    except FileNotFoundError:
        print("Archivo de administrador no encontrado, se cargarán valores por defecto.")
        return {"nombre": "admin", "contrasena": "admin123"}  # Valores por defecto

# Función para guardar los datos del administrador en el archivo CSV
def guardar_datos_administrador(administrador):
    with open("administrador.csv", "w") as archivo:
        archivo.write(f"{administrador['nombre']},{administrador['contrasena']}\n")

# Inicializar el archivo del administrador si no existe
def inicializar_administrador():
    try:
        with open("administrador.csv", "r") as archivo:
            pass  # Si existe el archivo, no hacemos nada
    except FileNotFoundError:
        # Si el archivo no existe, creamos uno con valores por defecto
        administrador = {"nombre": "admin", "contrasena": "admin123"}
        guardar_datos_administrador(administrador)
        print("Archivo del administrador creado con valores por defecto.")

# Llamar a la función de inicialización al inicio del programa
inicializar_administrador()

# Función para modificar datos del administrador
def modificar_datos_administrador():
    administrador = cargar_datos_administrador()  # Cargar los datos actuales desde el archivo

    nuevo_nombre = input("Ingrese el nuevo nombre del administrador (o presione Enter para no cambiar): ")
    nueva_contrasena = input("Ingrese la nueva contraseña (o presione Enter para no cambiar): ")

    if nuevo_nombre:
        administrador["nombre"] = nuevo_nombre
    if nueva_contrasena:
        administrador["contrasena"] = nueva_contrasena
    
    # Guardar los datos modificados en el archivo CSV
    guardar_datos_administrador(administrador)
    
    print("Datos del administrador actualizados y guardados.")

# Función para iniciar sesión
def iniciar_sesion():
    nombre_usuario = input("Ingrese su nombre de usuario: ")
    contrasena = input("Ingrese su contraseña: ")

    usuarios = cargar_usuarios()
    admin_datos = cargar_datos_administrador()  # Cargar datos del administrador desde el archivo CSV

    # Comprobar si el usuario es un usuario normal
    for usuario in usuarios:
        if usuario[0] == nombre_usuario and usuario[1] == contrasena:
            print(f"Inicio de sesión exitoso. Bienvenido, {nombre_usuario}.")
            return nombre_usuario

    # Comprobar si el usuario es el administrador
    if nombre_usuario == admin_datos["nombre"] and contrasena == admin_datos["contrasena"]:
        print(f"Inicio de sesión exitoso. Bienvenido, {nombre_usuario}.")
        return nombre_usuario

    print("Nombre de usuario o contraseña incorrectos.")
    return None

# Función para cargar usuarios desde el archivo CSV
def cargar_usuarios():
    usuarios = []
    try:
        with open("usuarios.csv", "rt") as archivo_usuarios:
            for linea in archivo_usuarios:
                nombre, contrasena, legajo = linea.strip().split(",")
                usuarios.append([nombre, contrasena, int(legajo)])
    except FileNotFoundError:
        print("Archivo de usuarios no encontrado.")
    return usuarios

# Función para guardar usuarios en el archivo CSV
def guardar_usuarios(usuarios):
    with open("usuarios.csv", "w") as archivo_usuarios:
        for usuario in usuarios:
            archivo_usuarios.write(f"{usuario[0]},{usuario[1]},{usuario[2]}\n")

# Función para cargar productos desde el archivo CSV
def cargar_productos():
    productos = []
    try:
        with open("productos.csv", "rt") as archivo_productos:
            for linea in archivo_productos:
                nombre, precio, cantidad, codigo = linea.strip().split(",")
                productos.append([nombre, float(precio), int(cantidad), codigo])
    except FileNotFoundError:
        print("Archivo de productos no encontrado.")
    return productos

# Función para guardar productos en el archivo CSV
def guardar_productos(productos):
    with open("productos.csv", "w") as archivo_productos:
        for producto in productos:
            archivo_productos.write(f"{producto[0]},{producto[1]},{producto[2]},{producto[3]}\n")

# Función para registrar un usuario
def registrarusuario():
    usuarios = cargar_usuarios()
    nombre = input("Ingrese el nombre del usuario: ")
    contraseña = input("Ingrese una contraseña: ")
    legajo = int(input("Ingrese el número de legajo del usuario: "))

    for usuario in usuarios:
        if usuario[0] == nombre:
            print("El usuario ya existe.")
            return

    nuevo_usuario = [nombre, contraseña, legajo]
    usuarios.append(nuevo_usuario)
    guardar_usuarios(usuarios)
    print("Usuario registrado con éxito.")

# Función para registrar productos
def Registrar_producto():
    productos = cargar_productos()
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    cantidad = int(input("Ingrese la cantidad del producto: "))
    codigo = input("Ingrese el código del producto: ")

    nuevo_producto = [nombre, precio, cantidad, codigo]
    productos.append(nuevo_producto)
    guardar_productos(productos)
    print(f"Producto {nombre} registrado correctamente.")

# Función para mostrar todos los productos
def mostrar_productos():
    productos = cargar_productos()  # Cargar los productos desde el archivo CSV
    
    if not productos:
        print("No hay productos disponibles.")
        return
    
    print("\n--- Lista de productos ---")
    for producto in productos:
        print(f"Nombre: {producto[0]}, Precio: {producto[1]}, Cantidad: {producto[2]}, Código: {producto[3]}")

# Menú principal
def menu():
    usuario_actual = None
    salir = False

    while not salir:
        if usuario_actual is None:
            print("\n--- Menú de inicio de sesión ---")
            print("1. Iniciar sesión")
            print("2. Salir")
            opcion = input("Seleccione una opción (1-2): ")

            if opcion == "1":
                usuario_actual = iniciar_sesion()
            elif opcion == "2":
                print("Saliendo del programa.")
                salir = True
            else:
                print("Opción no válida, intente de nuevo.")
        else:
            print(f"\n--- Menú principal (Usuario actual: {usuario_actual}) ---")
            print("1. Mostrar usuarios registrados")
            print("2. Buscar productos")
            print("3. Mostrar todos los productos")
            if usuario_actual == cargar_datos_administrador()["nombre"]:  # Usar datos cargados
                print("4. Modificar datos del administrador")
                print("5. Agregar/Modificar datos de productos")
                print("6. Registrar/Modificar usuarios")
                print("7. Eliminar usuario")
                print("8. Eliminar producto")
                print("9. Modificar producto")
            print("10. Cerrar sesión")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                mostrar_usuarios()
            elif opcion == "2":
                criterio_busqueda = input("¿Desea buscar por (1) Nombre o (2) Código?: ")
                if criterio_busqueda == "1":
                    nombre_producto = input("Ingrese el nombre del producto a buscar: ")
                    buscadorProductos(nombre_producto, "nombre")
                elif criterio_busqueda == "2":
                    codigo_producto = input("Ingrese el código del producto a buscar: ")
                    buscadorProductos(codigo_producto, "codigo")
                else:
                    print("Opción de búsqueda no válida.")
            elif opcion == "3":
                mostrar_productos()  # Llamada a la nueva función
            elif opcion == "4" and usuario_actual == cargar_datos_administrador()["nombre"]:
                modificar_datos_administrador()
            elif opcion == "5" and usuario_actual == cargar_datos_administrador()["nombre"]:
                Registrar_producto()
            elif opcion == "6" and usuario_actual == cargar_datos_administrador()["nombre"]:
                registrarusuario()
            elif opcion == "7" and usuario_actual == cargar_datos_administrador()["nombre"]:
                eliminar_usuario()
            elif opcion == "8" and usuario_actual == cargar_datos_administrador()["nombre"]:
                eliminar_producto()
            elif opcion == "9" and usuario_actual == cargar_datos_administrador()["nombre"]:
                modificar_producto()
            elif opcion == "10":
                usuario_actual = None
                print("Sesión cerrada.")
            else:
                print("Opción no válida.")

# Ejecutar el menú
menu()
