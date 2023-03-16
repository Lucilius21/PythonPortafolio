class Cliente:
    def __init__(self, id, nombre, tipo_servi, categoria_cliente, kilowats, monto):
        self.id = id
        self.nombre = nombre
        self.tipo_servi = tipo_servi
        self.categoria_cliente = categoria_cliente
        self.kilowats = kilowats
        self.monto = monto


def to_string(reg):
    return '{} - {} - {} - {} - {} - {}'.format(reg.id, reg.nombre, reg.tipo_servi, reg.categoria_cliente, reg.kilowats, reg.monto)


def titulo():
    return '{} - {} - {} - {} - {} - {}'.format('ID', 'Nombre', 'Tipo de servicio', 'Categoria del cliente', 'Consumo KW', 'Monto')
