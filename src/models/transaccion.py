from datetime import datetime

from src.models.moneda_digital import MonedaDigital
from src.models.tipo_operacion import TipoOperacion


class Transaccion(object):

    # como los parametros que recibe el constructor de la clase son muchos
    # y ademas le estamos agregando el tipo de dato
    # se puede partir la linea del constructor en varios renglones para que sea mas legible
    def __init__(self,
                 moneda: MonedaDigital,
                 operacion: TipoOperacion,
                 remitente, #Usuario
                 destinatario, #Usuario
                 monto: float,  # en dolares
                 cantidad_monedas
                 ):
        self._fecha: datetime = datetime.now()
        self._moneda: MonedaDigital = moneda
        self._tipo_operacion: TipoOperacion = operacion
        self._remitente = remitente
        self._destinatario = destinatario
        self._monto: float = monto  # US$
        self._cantidad_monedas = cantidad_monedas

    @property
    def fecha(self):
        # cuando usas fechas estas se almacenan en un numero largo llamado timestamp ej 1239890123848923
        # esta es la cantidad de segundos que pasaron desde un punto arbitrario
        # ( creo q era la fecha de nacimiento de linux)
        # python usa un datetime objet para almacenarlo
        # a ese valor le das formato con estas reglas https://www.programiz.com/python-programming/datetime/strftime
        formato_fecha = "%d/%m/%Y %H:%M:%S"
        return self._fecha.strftime(formato_fecha)

    @property
    def monto(self):
        return str(self._monto)

    @property
    def cantidad_monedas(self):
        return str(self._cantidad_monedas)

    # cuando se cree la funcion de descargar en archivo de texto se va a usar este mismo metodo para imprimirlo
    def __str__(self):
        transaccion = "Transaccion fecha: " + self.fecha + "\n" \
                      + "Moneda: " + self._moneda.value + "\n" \
                      + "\ttipo de operacion: " + self._tipo_operacion.value + "\n" \
                      + "\tcodigo del remitente: " + self._remitente.codigo + "\n" \
                      + "\tcodigo del destinatario: " + self._destinatario.codigo + "\n" \
                      + "\tMonto en Us$: " + str(self.monto) + "\n" \
                      + "\tCantidad de monedas:  " + str(self._cantidad_monedas)

        return transaccion
