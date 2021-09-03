from src.models.api_criptomoneda import ApiBinance
from src.models.caja_moneda import CajaMoneda


def balance_general(usuario):
    cotizacion_total = 0

    caja: CajaMoneda
    for caja in usuario.caja_monedas:
        cotizacion_moneda = ApiBinance.get_price(caja.moneda)
        cotizacion_moneda * caja.cantidad
        cotizacion_total += cotizacion_moneda
        print("moneda " + caja.moneda + " --> cotizacion $Us" + str(cotizacion_moneda))
    print("La cotizacion total de todas sus criptomonedas es $Us " + str(cotizacion_total))