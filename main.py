from archivo import leer_archivo
from obtener_slice import procesar_cadena


saltos = 2

texto = leer_archivo("texto.txt")
matriz = procesar_cadena(texto, saltos)


