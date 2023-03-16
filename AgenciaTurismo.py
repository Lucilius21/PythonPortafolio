"""
Una agencia de turismo requiere un programa para gestionar los paquetes de viajes que vende a sus clientes. Por cada
paquete vendido se tienen los siguientes datos: número de identificación (un entero), nombre o título descriptivo (una
cadena), un número entre 0 y 9 para indicar medio de transporte (Por ejemplo: 0: aéreo, 1: ómnibus, etc.), un número
flotante para indicar el monto que se cobró, otro número entero pero entre 1 y 50 para indicar el destino final del viaje
pactado, y finalmente el nombre del cliente que compró el paquete (una cadena).
En base a lo anterior, desarrollar un programa completo que disponga al menos de dos módulos [Máximo 4 puntos
por este requerimiento, incluyendo también convenciones de estilo y otros aspectos del programa general]:
• En uno de ellos, definir la clase Paquete que represente al registro a usar en el programa, y las funciones
básicas para operar con registros de ese tipo.
• En otro módulo, incluir el programa principal y las funciones generales que sean necesarias. Para la carga de
datos, aplique las validaciones que considere necesarias. El programa debe basarse en un menú de opciones
para desarrollar las siguientes tareas:
[1]. Generar un arreglo de n registros de tipo Paquete que contenga los datos de los paquetes vendidos (cargue el
valor de n por teclado validando que sea correcto). Puede generar el arreglo cargando los datos en forma manual o
generando los datos en forma aleatoria. El arreglo debe permanecer en todo momento ordenado por el número
de ticket durante la carga. Cada vez que se seleccione esta opción, el arreglo debe ser generado nuevamente
desde cero. Será considerada la eficiencia de la estrategia de carga y los algoritmos que aplique. [Máximo 4 puntos
entre los ítems 1 y 2 juntos].
[2]. Mostrar todos los datos del arreglo generado en el punto 1, a razón de un registro por renglón. Al final del listado,
muestre una línea adicional con el la cantidad de registros que se mostraron. [Máximo 4 puntos entre los ítems 1
y 2 juntos].
[3]. En base al arreglo generado en el punto 1 determinar si existe un paquete cuyo título o descripción sea tit (cargar
tit por teclado). Si existe, informe solo el número de identificación de ese paquete y el nombre del cliente que lo
compró. Si no existe, informe con un mensaje. La búsqueda debe detenerse al encontrar el primer registro que
cumpla el criterio de busqueda pedido. [Máximo 4 puntos].
[4]. En base al arreglo generado en el punto 1, determinar cuántos paquetes hay para combinación entre tipo de
medio de transporte y destino final (un contador para los que sean tipo de transporte 0 y destino 1, otro para el
tipo 0 y destino 2, y así sucesivaente para las 10*50 = 500 combinaciones posibles). Mostrar solo los contadores
diferentes de cero. [Máximo 4 puntos].
[5]. En base al arreglo generado en el punto 1 determinar el monto acumulado que haya pagado el cliente cuyo
nombre es nom (cargue la cadena nom por teclado). Note que ese nombre podría estar varias veces en el vector, y
ahora sí se pide acumular todos sus pagos. Si no existe ningún cliente con ese nombre, informe con un mensaje.
[Máximo 4 puntos].
[6]. Grabar en un archivo binario los datos de los registros del arreglo generado en el punto 1 que correspondan a
paquetes cuyo monto sea mayor a 100000. [Máximo 4 puntos].
[7]. Mostrar el archivo generado en el punto 6. Muestre al final una línea extra indicando el monto acumulado entre
los registros que se mostraron. [Máximo 4 puntos]

"""


from RegistroAgenciaTurismo import *
import random
import pickle
import os


def menu():
    print('=' * 100)
    print("BIENVENIDO A LA AGENCIA DE TURISMO")
    print("1- Generar arreglo.  \n2- Mostrar arreglo. \n3- Buscar paquete. \n4- Generar matriz. \n5- Buscar cliente  \n6- Crear archivo \n7- Mostrar archivo \n0- Salir.")
    op = int(input('Ingrese una opcion: '))
    print('=' * 100)
    return op


def validar(desde, mensaje):
    n = int(input(mensaje))
    while n <= desde:
        n = int(input('Error' + mensaje))
    return n


def cargar_vector(v, n):
    desc = 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n'
    nom = 'ab', 'cd', 'ef', 'hi', 'jk', 'lm', 'nñ', 'op', 'qr'
    for i in range(n):
        id = 100 + i
        descripcion = random.choice(desc)
        medio_transporte = random.randint(0, 9)
        monto = round((random.randint(1000000, 10000000000)/7), 2)
        destino = random.randint(1, 50)
        nombre_cliente = random.choice(nom)
        add_in_order(v, Paquete(id, descripcion, medio_transporte, monto, destino, nombre_cliente))


def add_in_order(v, nuevo):
    pos = 0
    izq, der = 0, len(v) - 1
    while izq <= der:
        c = (izq + der) // 2
        if v[c].id == nuevo.id:
            pos = c
            break
        if nuevo.id > v[c]. id:
            izq = c + 1
        else:
            der = c - 1
    if izq > der:
        pos = izq
    v[pos:pos] = [nuevo]


def mostrar_vector(v):
    print(titulo())
    for i in v:
        print(to_string(i))


def buscar_titulo(v, tit):
    for i in range(len(v)):
        if v[i].descripcion == tit:
            return i
    return -1


def generar_matriz(v):
    conteo = [[0] * 50 for i in range(10)]
    for reg in v:
        conteo[reg.medio_transporte][reg.destino] += 1
    return conteo


def mostrar_matriz(conteo):
    for f in range(len(conteo)):
        for c in range(len(conteo[f])):
            if conteo[f][c] != 0:
                print('Medio de transporte: ', f, '\tDestino:', c, '--', conteo[f][c])


def buscar_monto(v,nom):
    suma = 0
    existe = False
    for i in range(len(v)):
        if v[i].nombre_cliente == nom:
            suma += v[i].monto
            existe = True
    if existe == True:
        print('\nEl monto acumulado que pago', nom, 'es: $', suma,'\n')
    else:
        print('\nNo existe ningun cliente con ese nombre\n')


def generar_archivo(v,fd):
    f = open(fd, 'wb')
    ct = 0
    for reg in v:
        if reg.monto > 100000:
            pickle.dump(reg, f)
            ct += 1
    f.close()
    return ct


def mostrar_archivo(fd):
    cont = 0
    acumulador_monto = 0
    if not os.path.exists(fd):
        print('El archivo no existe')
    else:
        f = open(fd, 'rb')
        tam = os.path.getsize(fd)
        while f.tell() < tam:
            reg = pickle.load(f)
            print(to_string(reg))
            cont += 1
            acumulador_monto += reg.monto
        f.close()
    print('Se grabaron: ', cont, 'archivos')
    print('Monto promedio: ', acumulador_monto)


def principal():
    op = -1
    vec = []
    fd = 'paquetes.dat'
    while op != 0:
        op = menu()
        if op == 1:
            vec = []
            n = validar(0, 'Ingrese cantidad de registros a cargar: ')
            print('=' * 100)
            print('Registro generado')
            cargar_vector(vec, n)
        elif len(vec) == 0:
            print('=' * 100)
            print('Pasar por la opcion 1')
        elif op == 2:
            mostrar_vector(vec)
        elif op == 3:
            tit = input('Ingrese un titulo descriptivo: ')
            pos = buscar_titulo(vec, tit)
            if pos == -1:
                print('No existe')
            else:
                print(to_string(vec[pos]))
                cad_ID = vec[pos].id
                nom_cliente = vec[pos].nombre_cliente
                print('Descripcion: ', cad_ID, 'Nombre Cliente: ', nom_cliente)
        elif op == 4:
            conteo = generar_matriz(vec)
            mostrar_matriz(conteo)
        elif op == 5:
            nom = input('Ingrese nmbre del cliente: ')
            buscar_monto(vec,nom)
        elif op == 6:
            arch = generar_archivo(vec, fd)
            print(arch)
        elif op == 7:
            if os.path.exists(fd):
                mostrar_archivo(fd)
            else:
                print('No existe el archivo')


if __name__ == '__main__':
    principal()

