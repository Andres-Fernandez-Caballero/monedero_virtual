import requests
from src.models.moneda_digital import MonedaDigital


class ApiBinance:

    @staticmethod
    def get_price(moneda_digital):
        DOLARES = 'USD'
        moneda = moneda_digital
        url = 'https://api.binance.com/api/v3/ticker/price?symbol=' + moneda + DOLARES +'T'
        data = requests.get(url).json()

        return float(data['price'])
