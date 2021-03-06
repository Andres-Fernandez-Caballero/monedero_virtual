from src.models.Usuario import Usuario
from src.monedero_digital.acciones.balance_general import balance_general
from src.monedero_digital.acciones.balance_moneda import balance_moneda
from src.monedero_digital.acciones.descargar_historial_transacciones import descargar_historial_transacciones
from src.monedero_digital.acciones.enviar_dinero import enviar_dinero
from src.monedero_digital.acciones.mostrar_historial_transacciones import mostrar_historial_transacciones
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

    def _mostrar_opciones(self):
        string = "********* Menu ************* \n"  # \n salta al renglon de abajo \t hace una tabulacion
        string = "Usuario " + self._usuario.nombre + "Codigo: " + self._usuario.codigo + "\n"
        string += "1_ RECIBIR CANTIDAD\n"
        string += "2_ ENVIAR CANTIDAD\n"
        string += "3_ MOSTRAR VALANCE MONEDA\n"
        string += "4_ MOSTRAR VALANCE GENERAL\n"
        string += "5_ MOSTRAR HISTORIAL DE TRANSACCIONES\n"
        string += "6_ DESCARGAR HISTORIAL DE TRANSACCIONES \n"
        string += "7_ SALIR\n"
        string += "8_ MOSTRAR_USUARIOS(PROVISORIO)\n"

        print(string)

    @staticmethod
    def _ingresar_opcion():
        opcion_validada = False

        while opcion_validada is not True:
            opcion = input("Elija una opcion")
            if opcion.isnumeric():
                opcion_validada = True
            else:
                print("debe ingresar una opcion numerica")
        return int(opcion)

    def _accion(self, opcion: int):
        finalized = False
        if opcion == Opcion.RECIBIR_DINERO:
            recibir_dinero(self._usuario, self._usuarios)
        elif opcion == Opcion.ENVIAR_DINERO:
            enviar_dinero(self._usuario, self._usuarios)

        elif opcion == Opcion.MOSTRAR_VALANCE_MONEDA:
            balance_moneda(self._usuario)

        elif opcion == Opcion.MOSTRAR_VALANCE_GENERAL:
            balance_general(self._usuario)

        elif opcion == Opcion.MOSTRAR_HISTORIAL_TRANSACCIONES:
            mostrar_historial_transacciones(self._usuario)

        elif opcion == Opcion.DESCARGAR_HISTORIAL_TRANSACCIONES:
            descargar_historial_transacciones(self._usuario)

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
