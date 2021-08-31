def mostrar_usuarios(usuario_titular, usuarios):
    print("****** Usuario Activo ******")
    print(usuario_titular.__str__())

    print("****** Lista de Usuarios ******")
    for usuario in usuarios:
        print(usuario.__str__())