from src.models.moneda_digital import MonedaDigital


class CajaMoneda(object):
    def __init__(self, moneda_digital: MonedaDigital):
        self._moneda: MonedaDigital = moneda_digital  # es un Enum
        self._cantidad: int = 0

    @property
    def moneda(self):
        return self._moneda.value

    @property
    def cantidad(self):
        return str(self._cantidad)

    def agregar_monedas(self, cantidad):
        self._cantidad += cantidad

    def retirar_monedas(self, cantidad):
        self._cantidad -= cantidad

    def __str__(self):
        texto = "Caja de " + self.moneda + " -> Cantidad: " + self.cantidad + "\n"
        return texto

