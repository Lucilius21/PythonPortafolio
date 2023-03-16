#  Aqui voy a crear la clase PAQUETE
class Paquete:
    def __init__(self, id, descripcion, medio_transporte, monto, destino, nombre_cliente):
        self.id = id
        self.descripcion = descripcion
        self.medio_transporte = medio_transporte
        self.monto = monto
        self.destino = destino
        self.nombre_cliente = nombre_cliente


def to_string(reg):
    return"{} - {} - {} - {} - {} - {}".format(reg.id, reg.descripcion, reg.medio_transporte, reg.monto, reg.destino, reg.nombre_cliente)


def titulo():
    return "{} - {} - {} - {} - {} - {}".format("ID", "Descripcion", "Medio de transporte", "Monto", "Destino", 'Cliente')
