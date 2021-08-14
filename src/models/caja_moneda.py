from src.models.moneda_digital import MonedaDigital


class CajaMoneda(object):
    def __init__(self, moneda_digital):
        self._moneda = moneda_digital  # es un Enum
        self._cantidad = 0

    @property
    def moneda(self):
        return self._moneda.value

    @property
    def cantidad(self):
        return self._cantidad

    def agregar_monedas(self, cantidad):
        self._cantidad += cantidad

    def retirar_monedas(self, cantidad):
        self._cantidad -= cantidad

    def __str__(self) -> str:
        string = "caja de " + self.moneda() + " -> " + "Cantidad: " + str(self.cantidad()) + "\n"
        return string

