from datetime import datetime

from src.models.moneda_digital import MonedaDigital
from src.models.tipo_operacion import TipoOperacion


class Transaccion(object):
    def __init__(self):
        self.fecha = datetime.now()
        self.moneda: MonedaDigital
        self.tipo_operacion: TipoOperacion
        self.codigoRemitente:str
        self.codigoDestinatario: str
        self._monto:float  # US$
