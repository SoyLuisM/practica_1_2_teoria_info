def leer_archivo(archivo = "texto.txt"):
    
    texto = open(archivo, mode="r")
    texto_memoria = texto.read()
    texto.close()

    return texto_memoria