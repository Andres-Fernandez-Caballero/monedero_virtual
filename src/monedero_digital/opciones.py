# from enum import Enum # usamos la libreria Enum para poder "iterar" (recorrer) los elementos de un enumerado


# un enumerado es una clase especial que tiene valores fijos y constantes no se debe inicializar
# sirve para estandarizar valores evitando errores de tipeo (escribirlo mal")
class Opcion(enumerate):
    RECIBIR_DINERO = 1
    ENVIAR_DINERO = 2
    MOSTRAR_VALANCE_GENERAL = 3
    MOSTRAR_VALANCE_MONEDA = 4
    MOSTRAR_HISTORIAL_TRANSACCIONES = 5
    DESCARGAR_HISTORIAL_TRANSACCIONES = 6
    SALIR = 7
    MOSTRAR_USUARIOS = 8
