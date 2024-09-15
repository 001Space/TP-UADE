productos = {
    1: {"nombre": "Manzana", "categoria": "Frutas", "precio": 1030},
    2: {"nombre": "Leche", "categoria": "Lácteos", "precio": 500},
    3: {"nombre": "Pan", "categoria": "Panadería", "precio": 1500},
    4: {"nombre": "Arroz", "categoria": "Cereales", "precio": 2000},
    5: {"nombre": "Queso", "categoria": "Lácteos", "precio": 2900}
}

def buscarproducto(termino):
    for idproducto, detalles in productos.items():
        if termino.lower() in detalles["nombre"].lower():
            return idproducto
    return None

def main():
    termino_busqueda = input("Ingrese el nombre del producto que desea buscar: ")
    idresultado = buscarproducto(termino_busqueda)

    if idresultado:
        detalles = productos[idresultado]
        print(f"ID: {idresultado}, Nombre: {detalles['nombre']}, Categoría: {detalles['categoria']}, Precio: ${detalles['precio']:.2f}")
    else:
        print("No se encontraron productos que coincidan con su búsqueda.")

main()
