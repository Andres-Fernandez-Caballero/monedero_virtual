def descargar_historial_transacciones(usuario):
    ruta_archivo = usuario.nombre + ".txt"
    MODO_ESCRITURA = "w"
    file = open(ruta_archivo, MODO_ESCRITURA)
    try:
        file.write(usuario.historial_transacciones)
        print("historial descargado en la ruta: " + ruta_archivo)
    except:
        print("hubo un problema al descargar el historial... ")
    finally:
        file.close()
