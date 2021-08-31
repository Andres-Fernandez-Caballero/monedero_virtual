from enum import Enum, EnumMeta  # usamos la libreria Enum para poder "iterar" (recorrer) los elementos de un enumerado


# un enumerado es una clase especial que tiene valores fijos y constantes no se debe inicializar
# sirve para estandarizar valores evitando errores de tipeo (escribirlo mal")
from typing import Union, Any


class MonedaDigital(Enum):
    BITCOIN = "BTC"
    ETHEREUM = "ETH"
    BITCONNECT = "BCC"
    LITECOIN = "LTC"
    ETC_CLASSIC = "ETC"
    RIPLE = "XRP"

    @staticmethod
    def lista():
        lista = ""
        for moneda in MonedaDigital:
            lista += moneda.value + " "
        return lista

    @staticmethod
    def get_enum_from_string(moneda_str):
        moneda_digital = None

        for moneda in MonedaDigital:
            if moneda.value == moneda_str:
                moneda_digital = moneda
        return moneda_digital
