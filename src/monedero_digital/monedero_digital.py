from src.models.Usuario import Usuario
import src.monedero_digital.acciones
from src.models.api_criptomoneda import ApiBinance
from src.models.moneda_digital import MonedaDigital
from src.models.tipo_operacion import TipoOperacion
from src.models.transaccion import Transaccion
from src.monedero_digital.acciones.mostrar_usuarios import mostrar_usuarios
from src.monedero_digital.acciones.recibir_dinero import recibir_dinero
from src.monedero_digital.opciones import Opcion


class MonederoDigital(object):
    def __init__(self):
        self._usuario = Usuario("Martin", "A01")
        self._usuarios = []
        user2 = Usuario("Andres", "A02")
        self._usuarios.extend([user2])

        transaccion = Transaccion(MonedaDigital.BITCONNECT,
                                  TipoOperacion.RECIBIR_TRANSFERENCIA,
                                  self._usuario, user2,
                                  10,
                                  10)
        self._usuario.agregar_transaccion(transaccion)

    def iniciar(self):
        finalized = False
        self._limpiar_pantalla()
        while finalized is not True:
            self._mostrar_opciones()
            option = self._ingresar_opcion()
            self._limpiar_pantalla()
            finalized = self._accion(option)

    @staticmethod
    def _mostrar_opciones():
        string = "********* Menu ************* \n"  # \n salta al renglon de abajo \t hace una tabulacion
        string += "1_ RECIBIR DINERO\n"
        string += "2_ ENVIAR DINERO\n"
        string += "3_ MOSTRAR VALANCE GENERAL\n"
        string += "4_ MOSTRAR VALANCE MONEDA\n"
        string += "5_ MOSTRAR HISTORIAL DE TRANSACCIONES\n"
        string += "6_ SALIR\n"
        string += "7_ MOSTRAR_USUARIOS(PROVISORIO)\n"

        print(string)

    @staticmethod
    def _ingresar_opcion():
        opcion = int(input("Elija una opcion"))
        return opcion

    def _accion(self, opcion: int):
        finalized = False
        if opcion == Opcion.RECIBIR_DINERO:
            codigo_remitente = input("Ingrese el Codigo del Usuario Remitente")
            usuario: Usuario
            usuarioEncontrado = False
            index = 0
            while usuarioEncontrado is not True and index < len(self._usuarios):
                if self._usuarios[index].codigo == codigo_remitente:
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

                if self._usuarios[indexUsuario].restar_monedas(moneda_enum, cantindad_monedas ):
                    if self._usuario.sumar_monedas(moneda_enum, cantindad_monedas):
                        print("Transaccion realizada")
                else:
                    print("error de transaccion")




        elif opcion == Opcion.ENVIAR_DINERO:
            print("ingresaste ")


        elif opcion == Opcion.MOSTRAR_VALANCE_GENERAL:
            print("ingresaste 3")

        elif opcion == Opcion.MOSTRAR_VALANCE_MONEDA:
            print("ingresaste 4")

        elif opcion == Opcion.MOSTRAR_HISTORIAL_TRANSACCIONES:
            print("ingresaste 5")

        elif opcion == Opcion.MOSTRAR_USUARIOS:
            mostrar_usuarios(self._usuario, self._usuarios)

        elif opcion == Opcion.SALIR:
            print("Adios :)")
            finalized = True

        else:
            print("ingresaste una opcion no valida")

        return finalized

    def _buscar_usuario(self, codigo):
        usuario_encontrado = None
        for usuario in self._usuarios:
            if usuario.codigo == codigo:
                usuario_encontrado = usuario
        return usuario_encontrado

    @staticmethod
    def _limpiar_pantalla():
        # subprocess.run("clear")
        pass
