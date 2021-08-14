from src.models.caja_moneda import CajaMoneda
from src.models.moneda_digital import MonedaDigital


class Usuario(object):
    def __init__(self, nombre, codigo):
        self._nombre = nombre
        self._codigo = codigo
        self._caja_monedas = []
        self._historial_transacciones = []

        caja_bit = CajaMoneda(MonedaDigital.BITCOIN)  #metodo de la clase CajaMoneda
        caja_bit.agregar_monedas(10)  #metodo de la clase CajaMoneda
        self._caja_monedas.append(caja_bit)  #agrega a la lista un objeto

    def recibir_dinero(self, usuario_remitente, moneda_digital, cantidad):
        pass

    def dar_dinero(self, usuario_destinatario, moneda_digital, cantidad):
        pass

    def _agregar_moneda(self, moneda_digital, cantidad):
        posicion = self.buscar_caja_moneda(moneda_digital)
        if posicion is None:
            caja_moneda = CajaMoneda(moneda_digital)
            caja_moneda.agregar_monedas(cantidad)
            self._caja_monedas.append(caja_moneda)
        else:
            self._caja_monedas[posicion].agregar_monedas(cantidad)  # agrega una moneda con el metodo Agregar moneda de la clase CajaMoneda

    def buscar_caja_moneda(self, moneda_digital):
        posicion = None
        for caja in self._caja_monedas:
            if caja.moneda() is moneda_digital.value:
                posicion = self._caja_monedas.index(caja)
        return posicion

    @property
    def caja_monedas(self):
        return self._caja_monedas

    @property
    def nombre(self):
        return self._nombre

    @property
    def codigo(self):
        return self._codigo

    def __str__(self) -> str:
        string = "Usuario \n nombre: " + self._nombre + "\n" + "Cajas:\n"
        for caja in self._caja_monedas:
            string += caja.__str__()
        return string


