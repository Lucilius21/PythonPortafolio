#  Crear clase y definir métodos
class Traslado:
    def __init__(self, id, nombre, importe, provincia, pago):
        self.id = id
        self.nombre = nombre
        self.importe = importe
        self.provincia = provincia  # 0 - 23
        self.pago = pago  # 0 - 4


#  Mostrar un registro por linea con un for
def to_string(reg):
    #  Se pone una cadena por cada método
    return '{} - {} - {} - {} - {}'.format(reg.id, reg.nombre, reg.importe, reg.provincia, reg.pago)


#  Cabecera. Solo lo usamos en el punto 2
def titulo():
    return '{} - {} - {} - {} - {}'.format('id', 'nombre', 'importe', 'provincia', 'pago')
