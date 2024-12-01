from rich import print
from rich.panel import Panel
from rich.console import Console
from rich.table import Table

console = Console()

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
