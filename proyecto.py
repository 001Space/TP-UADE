from rich import print
from rich.panel import Panel
from rich.console import Console
from rich.table import Table

#Imports relacionados a usuarios
from usuario import cargar_usuarios
from usuario import guardar_usuarios
from usuario import mostrar_usuarios
from usuario import registrarusuario
from usuario import eliminar_usuario

#Imports relacionados al administrador
from administrador import cargar_datos_administrador
from administrador import guardar_datos_administrador
from administrador import inicializar_administrador
from administrador import modificar_datos_administrador

#Imports relacionados a los productos
from producto import cargar_productos
from producto import guardar_productos
from producto import mostrar_productos
from producto import buscar_producto
from producto import registrar_producto
from producto import modificar_producto
from producto import eliminar_producto

console = Console()

#FUNCIONES PRINCIPALES
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
