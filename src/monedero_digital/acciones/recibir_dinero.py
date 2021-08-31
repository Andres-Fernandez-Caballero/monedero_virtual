from src.models.Usuario import Usuario
from src.models.api_criptomoneda import ApiBinance
from src.models.moneda_digital import MonedaDigital
from src.models.tipo_operacion import TipoOperacion
from src.models.transaccion import Transaccion


def recibir_dinero(usuario, usuarios):
    codigo_remitente = input("Ingrese el Codigo del Usuario Remitente")
    usuario: Usuario
    usuarioEncontrado = False
    index = 0
    while usuarioEncontrado is not True and index < len(usuarios):
        if usuarios[index].codigo == codigo_remitente:
            usuarioEncontrado = True
            indexUsuario = index
        index += 1
    if usuarioEncontrado:
        print(MonedaDigital.lista())
        moneda_validada = False
        moneda = input("Ingrese la moneda a recibir")
        moneda_enum = MonedaDigital.get_enum_from_string(moneda)
        monto_dolares = input("Ingrese el monto en dolares a recibir")

        cantindad_monedas = float(monto_dolares) * ApiBinance.get_price(moneda)

        if usuarios[indexUsuario].restar_monedas(moneda_enum, cantindad_monedas):
            if usuario.sumar_monedas(moneda_enum, cantindad_monedas):
                transac1 = Transaccion(moneda_enum, TipoOperacion.RECIBIR_TRANSFERENCIA,
                                       usuarios[indexUsuario],
                                       usuario, monto_dolares, cantindad_monedas)
                transac2 = Transaccion(moneda_enum, TipoOperacion.ENVIARTRANSFERENCIA,
                                       usuarios[indexUsuario],
                                       usuario, monto_dolares, cantindad_monedas)

                usuario.agregar_transaccion(transac1)
                usuarios[indexUsuario].agregar_transaccion(transac2)

                print("Transaccion realizada")
        else:
            print("error de transaccion")
