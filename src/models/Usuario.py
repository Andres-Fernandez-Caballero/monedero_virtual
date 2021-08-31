from src.models.caja_moneda import CajaMoneda
from src.models.moneda_digital import MonedaDigital
from src.models.tipo_operacion import TipoOperacion
from src.models.transaccion import Transaccion


class Usuario(object):
    def __init__(self, nombre, codigo):
        self._nombre = nombre
        self._codigo = codigo
        self._caja_monedas = []
        self._historial_transacciones = []

        self._caja_monedas = self.iniciar_lista_monedas(100)

    def iniciar_lista_monedas(self, cantidad_monedas_inicial):
        cajas = []
        for moneda in MonedaDigital:
            caja = CajaMoneda(moneda)
            caja.sumar_cantidad_monedas(cantidad_monedas_inicial)
            cajas.append(caja)
        return cajas

    def agregar_transaccion(self, transaccion):
        self._historial_transacciones.append(transaccion)

    def restar_monedas(self, moneda_digital, cantidad):
        position = self.buscar_pocicion(moneda_digital)
        accion_realizada = False

        if position is not None:
            if cantidad <= self._caja_monedas[position].cantidad:
                self._caja_monedas[position].restar_cantidad_monedas(cantidad)
                accion_realizada = True
        return accion_realizada

    def sumar_monedas(self, moneda_digital, cantidad):
        posicion = self.buscar_pocicion(moneda_digital)
        accion_realizada = False
        if posicion is not None:
            self._caja_monedas[posicion].sumar_cantidad_monedas(cantidad)
            accion_realizada = True
        return accion_realizada

    # busca en la lista de caja_monedas y devuelve
    # si encontro la monedaDigital devuelve su posicion
    # si no encotro una monedaDIgital devuelve None
    def buscar_pocicion(self, moneda_digital: MonedaDigital):
        position = None
        for caja in self._caja_monedas:
            if caja.moneda is moneda_digital.value:
                position = self._caja_monedas.index(caja)
        return position

    def __str__(self):
        mensaje = "Usuario \n nombre: " + self._nombre + "\n" + "Cajas:\n"
        for caja in self._caja_monedas:
            mensaje += "* " + caja.__str__()
        mensaje += "Transacciones\n"
        if len(self._historial_transacciones) == 0:
            mensaje += "No hay Transacciones monetarias"
        else:
            for transaccion in self._historial_transacciones:
                mensaje += "* " + transaccion.__str__()
        return mensaje

    @property
    def caja_monedas(self):
        return self._caja_monedas

    @property
    def nombre(self):
        return self._nombre

    @property
    def codigo(self):
        return self._codigo
