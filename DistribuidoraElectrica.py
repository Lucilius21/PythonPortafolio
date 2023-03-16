"""
Una compañía distribuidora de electricidad requiere un programa para gestionar los cobros por los servicios que provee
a sus clientes. Por cada cliente se tienen los siguientes datos: número de identificación (un entero) del medidor,
nombre del cliente (una cadena), un número entre 0 y 9 para indicar tipo de servicio (Por ejemplo: 0: residencial, 1:
comercial, etc.), otro número entero pero entre 0 y 4 para indicar la categoría del cliente (0: consumo subsidiado, 1:
 consumo bajo, etc.), otro número entero para indicar la cantidad de kilowats consumidos, y finalmente un número
 flotante para indicar el monto que se cobró a ese cliente por el consumo medido en el período.
En base a lo anterior, desarrollar un programa completo que disponga al menos de dos módulos [Máximo 4 puntos por este
requerimiento, incluyendo también convenciones de estilo y otros aspectos del programa general]:
• En uno de ellos, definir la clase Cliente que represente al registro a usar en el programa, y las funciones básicas
para operar con registros de ese tipo.
• En otro módulo, incluir el programa principal y las funciones generales que sean necesarias. Para la carga de datos,
aplique las validaciones que considere necesarias. El programa debe basarse en un menú de opciones para desarrollar las
 siguientes tareas:
[1]. Generar un arreglo de n registros de tipo Cliente que contenga los datos de todos los clientes (cargue el valor de
n por teclado validando que sea correcto). Puede generar el arreglo cargando los datos en forma manual (y todo manual)
o bien generando los datos en forma aleatoria (pero todo en forma aleatoria/automática). El arreglo debe permanecer en
todo momento ordenado por número de identificación de medidor durante la carga. Cada vez que se seleccione esta opción,
el arreglo debe ser generado nuevamente desde cero. Será considerada la eficiencia de la estrategia de carga y los
algoritmos que aplique. [Máximo 4 puntos entre los ítems 1 y 2 juntos].
[2]. Mostrar todos los datos del arreglo generado en el punto 1, a razón de un registro por renglón. Al final del
listado, muestre una línea adicional con el promedio de kilowats consumidos entre todos los clientes que se mostraron.
[Máximo 4 puntos entre los ítems 1 y 2 juntos].
[3]. En base al arreglo generado en el punto 1 determinar si existe un registro cuyo número de medidor sea num (cargar
num por teclado). Si existe, muestre todos sus datos. Si no existe, informe con un mensaje. La búsqueda debe detenerse
al encontrar el primer registro que cumpla el criterio de busqueda pedido. [Máximo 4 puntos].
[4]. En base al arreglo generado en el punto 1, determinar el monto acumulado que se pagó para cada combinación entre
tipo de servicio y categoría de cliente (un acumulador de montos para los que sean tipo de servicio 0 y categoría 0,
otro para el tipo 0 y categoría 1, y así sucesivaente para las 5*10 = 50 combinaciones posibles). Mostrar solo los
acumuladores diferentes de cero. [Máximo 4 puntos].
[5]. En base al arreglo generado en el punto 1 determinar si existe un cliente cuyo nombre sea nom. Si existe mostrar
solo la cantidad de kilowats que consumió y el monto que pagó. Si no existe ningún cliente con ese nombre, informe con
un mensaje. La búsqueda debe detenerse al encontrar el primer cliente con el nombre pedido. [Máximo 4 puntos].
[6]. Grabar en un archivo binario los datos de los registros del arreglo generado en el punto 1 que correspondan a
clientes cuyo monto pagado sea mayor o igual a 10000. [Máximo 4 puntos].
[7]. Mostrar el archivo generado en el punto 6. Muestre al final una línea extra indicando la cantidad de registros
que se mostraron. [Máximo 4 puntos].

mesa 02/03/23
"""
from RegistroMontarce import *
import random
import pickle
import os


def validar(desde, mensaje):
    n = int(input(mensaje))
    if desde >= n:
        print('Error' + mensaje)
    return n


def menu():
    print('=' * 100)
    print('MENU')
    print('1 Crear vector')
    print('2 Mostrar vector')
    print('3 Buscar número de medidor ')
    print('4 Generar Matriz ')
    print('5 Buscar cliente ')
    print('6 Crear archivo ')
    print('7 Mostrar archivo ')
    print('0 Salir ')
    n = int(input('Ingrese una opcion: '))
    print('=' * 100)
    return n


def add_in_order(v, nuevo):
    pos = 0
    izq, der = 0, len(v)-1
    while izq <= der:
        c = (izq + der) //2
        if v[c].id == nuevo.id:
            pos = c
            break
        if nuevo.id > v[c].id:
            izq = c + 1
        else:
            der = c - 1
    if izq > der:
        pos = izq
    v[pos:pos] = [nuevo]


def crear_vector(v, n):
    name = 'Gustavo', 'Fabricio', 'Camila', 'Nadia', 'Selena', 'Hernan', 'Agustin', 'Sebastian', 'Raul'
    for reg in range(n):
        id = 100 + reg
        cliente = random.choice(name)
        tipo_servi = random.randint(0,9)
        categoria_cliente = random.randint(0,4)
        kilowats = random.randint(100, 500)
        monto = round(random.randint(10000, 400000)//7, 2)
        add_in_order(v, Cliente(id, cliente, tipo_servi, categoria_cliente, kilowats, monto))


def mostrar_vector(v):
    ct = 0
    vuelta = 0
    print(titulo())
    for reg in v:
        print(to_string(reg))
        ct += reg.kilowats
        vuelta += 1
    promedio_kw = (ct / vuelta)
    print('Promedio kw: ', promedio_kw)


def buscar_id(v, num):
    for reg in range(len(v)):
        if v[reg].id == num:
            return reg
    return -1


def crear_matriz(v):
    conteo = [[0] * 5 for i in range(10)]
    for reg in v:
        conteo[reg.tipo_servi][reg.categoria_cliente] += reg.monto
    return conteo


def mostrar_matriz(conteo):
    for f in range(len(conteo)):
        for c in range(len(conteo[f])):
            if conteo[f][c] != 0:
                print('Tipo de servicio: ', f, 'Categoria Cliente: ', c, '--', conteo[f][c])


def buscar_nom(v, nom):
    for reg in range(len(v)):
        if v[reg].nombre == nom:
            return reg
    return -1


def crear_arch(v, fd):
    f = open(fd, 'wb')
    for reg in v:
        if reg.monto >= 10000:
            pickle.dump(reg, f)
    print('Archivo creado')
    f.close()


def mostrar_arch(fd):
    ct = 0
    if not os.path.exists(fd):
        print('Archivo inexistente')
    else:
        f = open(fd, 'rb')
        tam = os.path.getsize(fd)
        while f.tell() < tam:
            reg = pickle.load(f)
            ct += 1
            print(to_string(reg))
        f.close()
        print('Se cargo: ', ct)


def principal():
    opc = -1
    v = []
    fd = 'clientes.dat'
    while opc != 0:
        opc = menu()
        if opc == 1:
            v = []
            n = validar(0, 'Ingrese cantidad de registros a cargar: ')
            crear_vector(v, n)
            print('Registros cargados')
        elif len(v) == 0:
            print('Pase por la opcion 1')
        elif opc == 2:
            mostrar_vector(v)
        elif opc == 3:
            num = int(input('Ingrese ID a buscar: '))
            pos = buscar_id(v, num)
            if pos == -1:
                print('No se encontró ID')
            else:
                print(to_string(v[pos]))
        elif opc == 4:
            cont = crear_matriz(v)
            mostrar_matriz(cont)
        elif opc == 5:
            nom = input('Ingrese nombre del cliente a buscar: ')
            ps = buscar_nom(v, nom)
            if ps == -1:
                print('No se encontró cliente')
            else:
                print('Kw consumidos: ', v[ps].kilowats, 'Monto: ', v[ps].monto)
        elif opc == 6:
            crear_arch(v, fd)
        elif opc == 7:
            mostrar_arch(fd)
        elif opc == 0:
            break


if __name__ == '__main__':
    principal()


