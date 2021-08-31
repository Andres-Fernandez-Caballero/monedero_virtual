from src.models.moneda_digital import MonedaDigital


class CajaMoneda(object):
    def __init__(self, moneda_digital: MonedaDigital):
        self._moneda = moneda_digital
        self._cantidad: float = 0

    @property
    def moneda(self):
        return str(self._moneda.value)

    @property
    def cantidad(self):
        return self._cantidad

    def sumar_cantidad_monedas(self, cantidad):
        self._cantidad += cantidad

    def restar_cantidad_monedas(self, cantidad):
        self._cantidad -= cantidad

    def __str__(self):
        texto = "Caja de " + self.moneda + " -> Cantidad: " + str(self.cantidad) + "\n"
        return texto
