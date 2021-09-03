from src.models.api_criptomoneda import ApiBinance
from src.models.caja_moneda import CajaMoneda
from src.models.moneda_digital import MonedaDigital


def balance_moneda(usuario):
    print(MonedaDigital.lista())
    moneda = input("indique la moneda que de desea hacer el balance")
    cotizacion = ApiBinance.get_price(moneda)
    enum_moneda = MonedaDigital.get_enum_from_string(moneda)
    indice = usuario.buscar_pocicion(enum_moneda)
    caja: CajaMoneda = usuario.caja_monedas[indice]
    cotizacion_total = caja.cantidad * cotizacion

    print("La cotizacion total de todas sus criptomonedas " + moneda + " es $Us " + str(cotizacion_total))
