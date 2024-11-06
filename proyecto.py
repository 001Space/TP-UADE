from rich import print
from rich.panel import Panel
from rich.console import Console
from rich.table import Table

console = Console()

# Función para cargar los datos del administrador desde el archivo CSV
def cargar_datos_administrador():
    try:
        with open("administrador.csv", "r") as archivo:
            nombre, contrasena = archivo.readline().strip().split(",")
            return {"nombre": nombre, "contrasena": contrasena}
    except FileNotFoundError:
        console.print("[bold red]Archivo de administrador no encontrado, se cargarán valores por defecto.[/bold red]")
        return {"nombre": "admin", "contrasena": "admin123"}  # Valores por defecto
    except Exception as e:
        console.print(f"[bold red]Error al leer el archivo del administrador: {str(e)}[/bold red]")
        return {"nombre": "admin", "contrasena": "admin123"}

# Función para guardar los datos del administrador en el archivo CSV
def guardar_datos_administrador(administrador):
    with open("administrador.csv", "w") as archivo:
        archivo.write(f"{administrador['nombre']},{administrador['contrasena']}\n")
    console.print(f"[bold green]Datos del administrador actualizados correctamente.[/bold green]")

# Inicializar el archivo del administrador si no existe
def inicializar_administrador():
    administrador = cargar_datos_administrador()
    if administrador['nombre'] == 'admin' and administrador['contrasena'] == 'admin123':
        guardar_datos_administrador(administrador)
        console.print("[bold green]Archivo del administrador creado con valores por defecto.[/bold green]")

# Función para cargar usuarios desde el archivo CSV
def cargar_usuarios():
    usuarios = []
    try:
        with open("usuarios.csv", "rt") as archivo_usuarios:
            for linea in archivo_usuarios:
                campos = linea.strip().split(",")
                if len(campos) == 3:
                    nombre, contrasena, legajo = campos
                    usuarios.append([nombre, contrasena, int(legajo)])
                else:
                    console.print(f"[bold red]Línea ignorada por formato incorrecto: {linea.strip()}[/bold red]")
    except FileNotFoundError:
        console.print("[bold red]Archivo de usuarios no encontrado.[/bold red]")
    return usuarios

# Función para guardar usuarios en el archivo CSV
def guardar_usuarios(usuarios):
    with open("usuarios.csv", "w") as archivo_usuarios:
        for usuario in usuarios:
            archivo_usuarios.write(f"{usuario[0]},{usuario[1]},{usuario[2]}\n")

# Función para iniciar sesión
def iniciar_sesion():
    console.print(Panel("[bold cyan]--- Iniciar Sesión ---[/bold cyan]", expand=False))
    nombre_usuario = input("Ingrese su nombre de usuario: ")
    contrasena = input("Ingrese su contraseña: ")

    usuarios = cargar_usuarios()
    admin_datos = cargar_datos_administrador()

    for usuario in usuarios:
        if usuario[0] == nombre_usuario and usuario[1] == contrasena:
            console.print(f"[bold green]Inicio de sesión exitoso. Bienvenido, {nombre_usuario}.[/bold green]")
            return nombre_usuario

    if nombre_usuario == admin_datos["nombre"] and contrasena == admin_datos["contrasena"]:
        console.print(f"[bold blue]Inicio de sesión exitoso. Bienvenido, {nombre_usuario} (Administrador).[/bold blue]")
        return nombre_usuario

    console.print("[bold red]Nombre de usuario o contraseña incorrectos.[/bold red]")
    return None

# Función para mostrar todos los usuarios registrados
def mostrar_usuarios():
    usuarios = cargar_usuarios()
    if not usuarios:
        console.print("[bold red]No hay usuarios registrados.[/bold red]")
        return

    tabla = Table(title="Usuarios Registrados")
    tabla.add_column("Nombre", style="cyan", justify="center")
    tabla.add_column("Legajo", style="magenta", justify="center")

    for usuario in usuarios:
        tabla.add_row(usuario[0], str(usuario[2]))

    console.print(tabla)

# Función para cargar productos desde el archivo CSV
def cargar_productos():
    productos = []
    try:
        with open("productos.csv", "rt") as archivo_productos:
            for linea in archivo_productos:
                nombre, precio, cantidad, codigo = linea.strip().split(",")
                productos.append([nombre, float(precio), int(cantidad), codigo])
    except FileNotFoundError:
        console.print("[bold red]Archivo de productos no encontrado.[/bold red]")
    return productos

# Función para guardar productos en el archivo CSV
def guardar_productos(productos):
    with open("productos.csv", "w") as archivo_productos:
        for producto in productos:
            archivo_productos.write(f"{producto[0]},{producto[1]},{producto[2]},{producto[3]}\n")

# Función para mostrar todos los productos
def mostrar_productos():
    productos = cargar_productos()
    if not productos:
        console.print("[bold red]No hay productos disponibles.[/bold red]")
        return

    tabla = Table(title="Lista de Productos")
    tabla.add_column("Nombre", style="cyan", justify="center")
    tabla.add_column("Precio", style="magenta", justify="center")
    tabla.add_column("Cantidad", style="green", justify="center")
    tabla.add_column("Código", style="yellow", justify="center")

    for producto in productos:
        tabla.add_row(producto[0], str(producto[1]), str(producto[2]), producto[3])

    console.print(tabla)

# Función unificada para buscar un producto por nombre o código
def buscar_producto(nombre_o_codigo):
    productos = cargar_productos()
    
    for producto in productos:
        if producto[0].lower() == nombre_o_codigo.lower() or producto[3] == nombre_o_codigo:
            # Retorna el producto completo como una lista [nombre, precio, cantidad, código]
            return producto

# Función para registrar un usuario
def registrarusuario():
    usuarios = cargar_usuarios()
    nombre = input("Ingrese el nombre del usuario: ")
    contraseña = input("Ingrese una contraseña: ")
    legajo = int(input("Ingrese el número de legajo del usuario: "))

    for usuario in usuarios:
        if usuario[0] == nombre:
            console.print("[bold red]El usuario ya existe.[/bold red]")
            return

    nuevo_usuario = [nombre, contraseña, legajo]
    usuarios.append(nuevo_usuario)
    guardar_usuarios(usuarios)
    console.print("[bold green]Usuario registrado con éxito.[/bold green]")

# Función para eliminar un usuario
def eliminar_usuario():
    usuarios = cargar_usuarios()
    nombre_usuario = input("Ingrese el nombre del usuario a eliminar: ")

    for usuario in usuarios:
        if usuario[0] == nombre_usuario:
            usuarios.remove(usuario)
            guardar_usuarios(usuarios)
            console.print(f"[bold green]Usuario {nombre_usuario} eliminado con éxito.[/bold green]")
            return

    console.print("[bold red]Usuario no encontrado.[/bold red]")

# Función para registrar un producto
def registrar_producto():
    productos = cargar_productos()
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    cantidad = int(input("Ingrese la cantidad del producto: "))
    codigo = input("Ingrese el código del producto: ")

    nuevo_producto = [nombre, precio, cantidad, codigo]
    productos.append(nuevo_producto)
    guardar_productos(productos)
    console.print(f"[bold green]Producto {nombre} registrado correctamente.[/bold green]")

def modificar_producto():
    productos = cargar_productos()  # Cargamos la lista de productos
    nombre_o_codigo = input("Ingrese el nombre o código del producto a modificar: ")

    producto = buscar_producto(nombre_o_codigo)  # Buscamos el producto por nombre o código

    if producto:
        # Encontramos el índice del producto en la lista de productos
        index = productos.index(producto)
        
        nuevo_nombre = input("Ingrese el nuevo nombre (o presione Enter para no cambiar): ")
        nuevo_precio = input("Ingrese el nuevo precio (o presione Enter para no cambiar): ")
        nueva_cantidad = input("Ingrese la nueva cantidad (o presione Enter para no cambiar): ")

        # Modificamos los datos si el usuario proporciona nuevos valores
        if nuevo_nombre:
            productos[index][0] = nuevo_nombre
        if nuevo_precio:
            try:
                productos[index][1] = float(nuevo_precio)  # Intentamos convertir el nuevo precio a float
            except ValueError:
                console.print("[bold red]Precio inválido, no se modificó.[/bold red]")
                return  # Salimos si el precio no es válido
        if nueva_cantidad:
            try:
                productos[index][2] = int(nueva_cantidad)  # Intentamos convertir la nueva cantidad a int
            except ValueError:
                console.print("[bold red]Cantidad inválida, no se modificó.[/bold red]")
                return  # Salimos si la cantidad no es válida

        # Guardamos los cambios en el archivo
        guardar_productos(productos)
        console.print(f"[bold green]Producto '{nombre_o_codigo}' modificado correctamente.[/bold green]")
    else:
        console.print("[bold red]Producto no encontrado.[/bold red]")



# Función para eliminar un producto
def eliminar_producto():
    productos = cargar_productos()
    nombre_o_codigo = input("Ingrese el nombre o código del producto a eliminar: ")

    producto = buscar_producto(nombre_o_codigo)

    if producto:
        productos.remove(producto)
        guardar_productos(productos)
        console.print(f"[bold green]Producto '{nombre_o_codigo}' eliminado con éxito.[/bold green]")
    else:
        console.print("[bold red]Producto no encontrado.[/bold red]")

# Función para modificar datos del administrador
def modificar_datos_administrador():
    administrador = cargar_datos_administrador()
    console.print(Panel("[bold cyan]--- Modificar Datos del Administrador ---[/bold cyan]", expand=False))

    nuevo_nombre = input("Ingrese el nuevo nombre (o presione Enter para no cambiar): ")
    nuevo_contrasena = input("Ingrese la nueva contraseña (o presione Enter para no cambiar): ")

    if nuevo_nombre:
        administrador["nombre"] = nuevo_nombre
    if nuevo_contrasena:
        administrador["contrasena"] = nuevo_contrasena

    guardar_datos_administrador(administrador)


multiplicar = lambda x, y: x * y

# Función para cargar ventas 
def cargar_venta():
    fac = 0

    console.print(Panel("[bold cyan]-- Factura Iniciada --[/bold cyan]", expand=False))
    tabla = Table(title="Factura de venta")
    tabla.add_column("Nombre", style="magenta", justify="center")
    tabla.add_column("Cantidad", style="magenta", justify="center")
    tabla.add_column("Precio Un.", style="magenta", justify="center")
    tabla.add_column("Precio Total", style="magenta", justify="center")

    total_factura = 0  # Variable para acumular el total

    # Cargar los productos al inicio para poder actualizarlos
    productos = cargar_productos()

    # Crear un diccionario para almacenar las cantidades vendidas
    cantidades_vendidas = {}

    while fac != '-1':
        nombre_o_codigo = input("Ingrese el nombre o codigo del producto a buscar: ")
        producto = buscar_producto(nombre_o_codigo)

        if producto:
            cantidad = int(input("Ingrese la cantidad del producto: "))  # Convertir a entero
            if cantidad > producto[2]:
                console.print(f"[bold red]No hay suficiente stock para {producto[0]}.[/bold red]")
                continue
            precio_total = multiplicar(producto[1], cantidad)
            total_factura += precio_total  # Sumar al total de la factura
            tabla.add_row(producto[0], str(cantidad), f"{producto[1]:.2f}", f"{precio_total:.2f}")  # Formato de precios
            console.print(tabla)  # Imprimir la tabla después de agregar cada producto
            
            # Actualizar el stock de producto en el diccionario de cantidades vendidas
            if producto[3] in cantidades_vendidas:
                cantidades_vendidas[producto[3]] += cantidad
            else:
                cantidades_vendidas[producto[3]] = cantidad
        else:
            console.print(f"[bold red]Producto no encontrado: {nombre_o_codigo}[/bold red]")
        fac = input("Presione Enter si desea cargar más productos, ingrese -1 para cerrar la factura: ")

    continuar = True

    while continuar:
        met_pago = input("Seleccione metodo de pago: 1.Credito - 2.Efectivo - 3.Debito \n")
        
        if met_pago == '1':
            total_factura = multiplicar(total_factura, 1.1)
            continuar = False
        elif met_pago == '2':
            total_factura = multiplicar(total_factura, 0.9)
            continuar = False
        elif met_pago == '3':
            continuar = False
        else:
            print("Valor invalido")

# Agregar el total al final de la tabla
    tabla.add_row("[bold yellow]Total[/bold yellow]", "", "", f"[bold green]{total_factura:.2f}[/bold green]")  
    console.print(tabla)  # Imprimir la tabla final con el total

# Actualizar las cantidades en el archivo CSV
    for producto in productos:
        if producto[3] in cantidades_vendidas:
            producto[2] -= cantidades_vendidas[producto[3]]  # Descontar la cantidad vendida

# Guardar las cantidades actualizadas en el archivo CSV
    guardar_productos(productos)

    console.print(Panel("[bold green]-- Factura finalizada --[/bold green]", expand=False))


# Menú principal actualizado
def menu():
    usuario_actual = None
    salir = False

    while not salir:
        if usuario_actual is None:
            console.print(Panel("[bold cyan]--- Menú de inicio de sesión ---[/bold cyan]", expand=False))
            print("1. Iniciar sesión")
            print("2. Salir")
            opcion = input("Seleccione una opción (1-2): ")

            if opcion == "1":
                usuario_actual = iniciar_sesion()
            elif opcion == "2":
                console.print("[bold green]Saliendo del programa.[/bold green]")
                salir = True
            else:
                console.print("[bold red]Opción no válida, intente de nuevo.[/bold red]")
        else:
            console.print(Panel(f"[bold cyan]--- Menú principal (Usuario actual: {usuario_actual}) ---[/bold cyan]", expand=False))
            print("1. Mostrar usuarios registrados")
            print("2. Productos")
            print("3. Cargar venta")

            admin_datos = cargar_datos_administrador()
            if usuario_actual == admin_datos["nombre"]:
                print("4. Modificar datos del administrador")
                print("5. Registrar un producto")
                print("6. Registrar un usuario")
                print("7. Eliminar un usuario")
                print("8. Eliminar un producto")
                print("9. Modificar un producto")

            print("10. Cerrar sesión")

            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                mostrar_usuarios()
            elif opcion == "2":
                criterio = input("Seleccione: 1. Mostrar todos los productos 2. Buscar producto: ")
                if criterio == "1":
                    mostrar_productos()
                elif criterio=="2":
                    nombre_o_codigo = input("Ingrese el nombre o codigo del producto a buscar: ")
                    producto = buscar_producto(nombre_o_codigo)
                    if producto:
                        console.print(f"[bold green]Producto encontrado: {producto[0]}, Precio: {producto[1]}, Cantidad: {producto[2]}, Código: {producto[3]}[/bold green]")
                    else:
                        console.print("[bold red]Producto no encontrado[/bold red]")
                else:
                    console.print("[bold red] Valor ingresado invalido [bold red]")
            elif opcion == "3":
                cargar_venta()
            elif opcion == "4" and usuario_actual == cargar_datos_administrador()["nombre"]:
                modificar_datos_administrador()
            elif opcion == "5" and usuario_actual == cargar_datos_administrador()["nombre"]:
                registrar_producto()
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
                console.print("[bold green]Sesión cerrada.[/bold green]")
            else:
                console.print("[bold red]Opción no válida.[/bold red]")

# Inicializar y ejecutar el menú
inicializar_administrador()
menu()
