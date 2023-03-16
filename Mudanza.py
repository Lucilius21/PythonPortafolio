"""
Una empresa de mudanzas mantiene informacion sobre los distintos trabajos de traslado que debe realizar.
Por cada traslado se registran los datos siguientes: numero de identificacion del traslado (un número entero), nombre
del cliente (una cadena), importe a facturar por el traslado, provincia destino del traslado (un valor entre 0 y 22
incluidos) y forma de pago (un numero entre 0 y 4)).

Se pide definir un tipo de registro Traslado con los campos que se indicaron, y un programa completo con menu de
opciones para hacer lo siguiente:

1.	Cargar los datos de n registros de tipo Traslado en un arreglo de registros (cargue n por teclado). El arreglo debe
crearse de forma que siempre quede ordenado de menor a mayor, segun el número de identificación de los traslados.

2.	Mostrar el arreglo creado en el punto 1, a razón de un registro por linea.

3. 	Buscar en el arreglo creado en el punto 1 un registro en el cual el nombre del cliente sea igual a nom (cargar nom
por teclado). Si no existe informar con un mensaje. Si existe, mostrar el registro y validar que el nombre esté
compuesto sólo por letras y espacios(procesando los caracteres uno por uno); en caso de no ser válido, agregar un
asterisco al final del nombre.

4.	A partir del arreglo, crear un archivo de registros en el cual se copien los datos de todos los traslados cuya forma
de pago sea 0 y cuyo importe a facturar se encuentre entre dos valores a y b que se cargan por teclado

5.	Mostrar el archivo creado en el punto anterior, a razón de un registro por linea en pantalla.

6. Informar la cantidad de provincias por forma de pago, solo cuando el importe sea mayor a 0.
"""
from RegistroMudanza import *
import random
import pickle
import os


def mostrar_menu():
    print('=' * 156)
    print('\n\t☰ Menu')
    print('\t1. Cargar')
    print('\t2. Mostrar')
    print('\t3. Buscar')
    print('\t4. Crear archivo')
    print('\t5. Mostrar archivo')
    print('\t6. Mostrar cantidad segun provincia y forma de pago')
    print('\t0. Salir')
    print('=' * 156)
    opcion = int(input('Seleccione una opción >_'))
    print('=' * 156)
    return opcion


def validar(desde, mensaje):
    num = int(input(mensaje))
    while num <= desde:
            num = int(input('Error '+mensaje))
    return num


# Insercion binaria
def add_in_order(v, nuevo):
    pos = 0
    izq, der = 0, len(v)-1
    while izq <= der:
        c = (izq + der) // 2
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


#  Insercion ordenada por cada vez que se le pida que se debe mantener el vec ordenado
def cargar_vector(v, n):
    nombres = 'Paula', 'Jose', 'Ana', 'Juan', 'Pabl0'
    apellidos = 'Alvarez', 'Gomez', 'Addams', 'Martinez'
    for i in range(n):
        id = 100+i
        nombre = random.choice(nombres)+ ' '+ random.choice(apellidos)
        importe = round((random.randint(10000, 50000)/7), 2)
        provincia = random.randint(0,22)
        pago = random.randint(0,4)
        add_in_order(v, Traslado(id, nombre,importe,provincia,pago))


def mostrar_vector(v):
    print(titulo())
    for i in v:
        print(to_string(i))

#  Para el punto de busqueda hay que plantearse si es
#  Busqueda binaria: para cuando se usa el mismo campo que se uso para insercion ordenada, este caso id
#  Busqueda secuencial: para cuando no se usa el mismo campo que uso para insercion ordenada

# Busqueda secuencial
def buscar_nombre(v, nom):
    for i in range(len(v)):
        if v[i].nombre == nom:
            return i
    return -1


def es_letra(car):
    if (car >= 'A' and car <= 'Z') or (car >= 'a' and car <= 'z'):
        return True
    return False


def validar_nombre(nom):
    cant = 0
    for car in nom:
        if car == ' ' or es_letra(car):
            cant += 1
    if cant == len(nom):
        return True
    else:
        return False

#  ASI SE PASA UN TODOS LOS REGISTROS A UN ARCHIVO
#def generar_archivo(v,fd):
    #  Si el archivo es de registros es binario.
    # w para escribir solamente, con a se modifican
    #f = open(fd, 'wb')
    #  Recorrer el vector que tiene la informacion
    #for reg in v:
        #pickle.dump(reg,f)
    #f.close()


def generar_archivo(v,fd,a,b):
    #  Si el archivo es de registros es binario.
    #  w para escribir solamente, con a se modifican
    f = open(fd, 'wb')
    #  Contador para retornar algo, en este caso cuantos registros se grabaron
    cant = 0
    #  Recorrer el vector que tiene la informacion
    for reg in v:
        # Condicional de la consigna que pago sea igual a 0 y el importe pasado por parametro sea igual al a y b
        if reg.pago == 0 and reg.importe >= a and reg.importe <= b:
            pickle.dump(reg, f)
            cant += 1
    f.close()
    return cant


def mostrar_archivo(fd):
    # Puede suceder que el archivo exista pero este vacio entonces usamos un contador
    cont = 0
    #  Si el arch no existe
    if not os.path.exists(fd):
        print('El archivo no existe')
    else:
        #  Abrirlo en formato lectura binaria
        f = open(fd, 'rb')
        #  Tomar con la libreria os el tamaño del archivo
        tam = os.path.getsize(fd)
        #  Mientras la posicion actual del arch que se toma con tell, se mantenga menor  que tam: existe algo para leer
        while f.tell() < tam:
            reg = pickle.load(f)
            print(to_string(reg))
            cont += 1
        #  Cerrar archivo despues de usarlo
        f.close()
    print('Se leyeron: ', cont, ' de registros')


def generar_matriz(v):
    # columna * fila
    # pago * provincia
    conteo = [[0] * 5 for i in range(24)]
    for reg in v:
        #  Recorrido secuencial. Acceso directo
        #  Acumulador fila * columna
        conteo[reg.provincia][reg.pago] += 1
        #  Una opciones puede ser que nos pida que se acumule segun provincia y medio de pago, los importes
        #  conteo[reg.provincia][reg.pago] += reg.importe
    return conteo


def mostrar_matriz(conteo):
    # Si pide que las provincias o pagos esten sean mayor a un numero. Provincia mayor a 10
    # for f in range(11,len(conteo)):
    for f in range(len(conteo)):
        for c in range(len(conteo[f])):
            if conteo[f][c] != 0:
                print('Provincia: ', f, 'Pago:', c, '--', conteo[f][c])


def principal():
    #  Definir un vector vacio para insertarle elementos a trabajar
    v = []
    #  Para asegurar que por lo menos entre una vez
    opcion = -1
    #  Para usar el mismo nombre para el archivo
    fd = 'traslados.dat'

    #  Mientras la opcion sea distinta a la de salir, realiza:
    while opcion != 0:
        opcion = mostrar_menu()
        if opcion == 1:
            n = validar(0, 'Ingrese cantidad de registros >_')
            cargar_vector(v, n)
        elif len(v) == 0:
            print('Pasar a op 1')
        elif opcion == 2:
            mostrar_vector(v)
        elif opcion == 3:
            nom = input('Ingrese nombre a buscar >_')
            pos = buscar_nombre(v, nom)
            if pos == -1:
                print('No existe')
            else:
                validacion = validar_nombre(v[pos].nombre)
                if validacion ==  False:
                    # Para hacer una corroboracion agregar en la creacion automatica por ejemplo Pabl0

                    # Cuando en busqueda hay que modificar algo no se hace en el metodo de busqueda,
                    # sino en un variable como se muestra abajo
                    v[pos].nombre = v[pos].nombre + '*'
                print(to_string(v[pos]))
        elif opcion == 4:
            a = validar(0, 'Ingrese importe minimo >_')
            #  Como tiene que ser mayor que el minimo usamos la funcion validar con parametro a
            b = validar(a, 'Ingrese importe maximo >_')
            cant = generar_archivo(v, fd, a, b)
            print('Se grabaron: ', cant, ' de registros')
        elif opcion == 5:
            mostrar_archivo(fd)
        elif opcion == 6:
            #  Hay que generar una matriz de provincia [24] * pago [5]
            #  Hay que llenar inicialmente la matriz con [0] * columna[prov] for i in range fila[pago]
            conteo = generar_matriz(v)
            mostrar_matriz(conteo)


if __name__ == '__main__':
    principal()
