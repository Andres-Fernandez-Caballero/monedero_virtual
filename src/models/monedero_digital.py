from src.models.Usuario import Usuario
from src.models.opciones import Opcion
import subprocess


class MonederoDigital(object):
    def __init__(self):
        self._usuarios = []
        user1 = Usuario("Martin", "A01")
        user2 = Usuario("Andres", "A02")
        self._usuarios.extend([user1, user2])

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
        string = "********* Menu ************* \n"  # \n salta al renglon de abajo
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
            print("ingresaste 1")

        elif opcion == Opcion.ENVIAR_DINERO:
            print("ingresaste ")

        elif opcion == Opcion.MOSTRAR_VALANCE_GENERAL:
            print("ingresaste 3")

        elif opcion == Opcion.MOSTRAR_VALANCE_MONEDA:
            print("ingresaste 4")

        elif opcion == Opcion.MOSTRAR_HISTORIAL_TRANSACCIONES:
            print("ingresaste 5")

        elif opcion == Opcion.MOSTRAR_USUARIOS:
            print("****** Lista de Usuarios ******")
            for usuario in self._usuarios:
                print(usuario.__str__())

        elif opcion == Opcion.SALIR:
            print("Adios :)")
            finalized = True

        else:
            print("ingresaste una opcion no valida")

        return finalized

    def _buscar_usuario(self, codigo):
        usuario_encontrado = None
        for usuario in self._usuarios:
            if usuario.codigo is codigo:
                usuario_encontrado = usuario
        return usuario_encontrado
    
    @staticmethod
    def _limpiar_pantalla():
        subprocess.run("clear")
