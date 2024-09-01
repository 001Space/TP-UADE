ids = [1, 2, 3, 4, 5]
nombres = ["Manzana", "Leche", "Pan", "Arroz", "Queso"]
categorias = ["Frutas", "Lácteos", "Panadería", "Cereales", "Lácteos"]
precios = [1030, 500, 1500, 2000, 2900]

def buscar_producto(termino, nombres):
    indices_resultados = []
    for i, nombre in enumerate(nombres):
        if termino.lower() in nombre.lower():
            indices_resultados.append(i)
    return indices_resultados

def main():
    termino_busqueda = input("Ingrese el nombre del producto que desea buscar: ")
    indices_resultados = buscar_producto(termino_busqueda, nombres)

    if indices_resultados:
        print("\nProductos encontrados:")
        for i in indices_resultados:
            print(f"ID: {ids[i]}, Nombre: {nombres[i]}, Categoría: {categorias[i]}, Precio: ${precios[i]:.2f}")
    else:
        print("No se encontraron productos que coincidan con su búsqueda.")

if __name__ == "__main__":
    main()
