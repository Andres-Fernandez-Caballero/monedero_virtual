from src.models.Usuario import Usuario


class MonederoDigital(object):
    def __init__(self):
        self._usuarios = []
        user1 = Usuario("Martin", "A01")
        user2 = Usuario("Andres", "A02")
        self._usuarios.extend([user1, user2])

    def iniciar(self):
        finalized = False
        while finalized is not True:
            self._mostrar_opciones()
            option = self._ingresar_opcion()
            finalized = self._accion(option)

    @staticmethod
    def _mostrar_opciones():
        string = ""
        string += "********* Menu ************* \n"  # \n salta al renglon de abajo
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
        if opcion == 1:
            print("ingresaste 1")
        elif opcion == 2:
            print("ingresaste 2")
        elif opcion == 3:
            print("ingresaste 3")
        elif opcion == 4:
            print("ingresaste 4")
        elif opcion == 5:
            print("ingresaste 5")
        elif opcion == 7:
            print("Usuarios\n")
            for usuario in self._usuarios:
                print(usuario.__str__())

        elif opcion == 6:
            print("Adios :)")
            finalized = True
        else:
            print("ingresaste una opcion no valida")

        return finalized
