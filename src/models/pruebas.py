from typing import List, Any

from src.models.Usuario import Usuario


class Prueba(object):
    _usuarios: list[Usuario]

    def __init__(self):
        self._usuarios = []

    def __str__(self):
        return "hola soy una prueba y tengo una lista " + str(len(self._usuarios))
