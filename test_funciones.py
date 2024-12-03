import os

from administrador import cargar_datos_administrador
from producto import buscar_producto, guardar_productos


def test_cargar_datos_admin_defecto():


    os.remove('administrador.csv')

    datos = cargar_datos_administrador()

    assert datos['nombre'] == 'admin'
    assert datos['contrasena'] == 'admin123'


def test_cargar_datos_admin_ingresados():

    try:
        with open('administrador.csv', 'w') as archivo:
            archivo.write('joaco,entest')

        datos = cargar_datos_administrador()


        assert datos['nombre'] == 'joaco'
        assert datos['contrasena'] == 'entest'
    except:
        print('Algo salio mal en el test')


def test_buscar_producto():

    guardar_productos([
        ['manzana',1.20, 2, 'MA25'],
        ['pera',1.60, 2, 'PE45'],
    ])


    producto = buscar_producto('manzana')

    assert producto[0] == 'manzana'
    assert producto[3] == 'MA25'

    producto = buscar_producto('PE45')

    assert producto[0] == 'pera'
    assert producto[3] == 'PE45'

    producto = buscar_producto('no existo')

    assert producto is None