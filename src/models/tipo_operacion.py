from enum import Enum # usamos la libreria Enum para poder "iterar" (recorrer) los elementos de un enumerado


# un enumerado es una clase especial que tiene valores fijos y constantes no se debe inicializar
# sirve para estandarizar valores evitando errores de tipeo (escribirlo mal")
class TipoOperacion(Enum):
    ENVIARTRANSFERENCIA = "TRANSFERENCIA"
    RECIBIR_TRANSFERENCIA = "DEPOSITO"
