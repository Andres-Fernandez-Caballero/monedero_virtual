from src.models.Usuario import Usuario
from src.models.api_criptomoneda import ApiBinance
from src.models.moneda_digital import MonedaDigital


def recibir_dinero(usuario, usuarios):
    codigo = input("ingrese el codigo del remitente")
    remitente: Usuario
    for remitente in usuarios:
        if remitente.codigo == codigo:
            print("monedas disponibles")
            for moneda in MonedaDigital:
                print(moneda.value)

            moneda = input("ingrese moneda a utilizar")  # //TODO: validad moneda y si esta en mayusculas o no

            monto = input("ingrese el monto en dolares a recibir")
            cantidad_monedas = ApiBinance.get_price(moneda) * monto
            remitente.recibir_dinero(usuario, moneda, float(monto), float(cantidad_monedas))
            usuario.enviar_dinero(remitente, moneda, float(monto), float(cantidad_monedas))
