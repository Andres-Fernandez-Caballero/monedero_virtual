from src.models.Usuario import Usuario
import src.monedero_digital.acciones
from src.models.api_criptomoneda import ApiBinance
from src.models.moneda_digital import MonedaDigital
from src.models.tipo_operacion import TipoOperacion
from src.models.transaccion import Transaccion
from src.monedero_digital.acciones.descargar_historial_transacciones import descargar_historial_transacciones
from src.monedero_digital.acciones.enviar_dinero import enviar_dinero
from src.monedero_digital.acciones.mostrar_historial_transacciones import mostrar_historial_transacciones
from src.monedero_digital.acciones.mostrar_usuarios import mostrar_usuarios
from src.monedero_digital.acciones.recibir_dinero import recibir_dinero
from src.monedero_digital.opciones import Opcion


class MonederoDigital(object):
    def __init__(self):
        self._usuario = Usuario("Martin", "A01")
        self._usuarios = []
        user2 = Usuario("Andres", "A02")
        self._usuarios.extend([user2])

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
        string += "6_ DESCARGAR HISTORIAL DE TRANSACCIONES \n"
        string += "7_ SALIR\n"
        string += "8_ MOSTRAR_USUARIOS(PROVISORIO)\n"

        print(string)

    @staticmethod
    def _ingresar_opcion():
        opcion = int(input("Elija una opcion"))
        return opcion

    def _accion(self, opcion: int):
        finalized = False
        if opcion == Opcion.RECIBIR_DINERO:
            recibir_dinero(self._usuario, self._usuarios)
        elif opcion == Opcion.ENVIAR_DINERO:
            enviar_dinero(self._usuario, self._usuarios)


        elif opcion == Opcion.MOSTRAR_VALANCE_GENERAL:
            print("ingresaste 3")

        elif opcion == Opcion.MOSTRAR_VALANCE_MONEDA:
            print("ingresaste 4")

        elif opcion == Opcion.MOSTRAR_HISTORIAL_TRANSACCIONES:
            mostrar_historial_transacciones(self._usuario)

        elif opcion == Opcion.DESCARGAR_HISTORIAL_TRANSACCIONES:
            descargar_historial_transacciones(self._usuario)

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
