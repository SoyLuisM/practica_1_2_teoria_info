from archivo import leer_archivo
from obtener_slice import procesar_cadena
from probabilidad_espacio import probabilidad_de_espacio


saltos = 2

texto = leer_archivo("texto.txt")
matriz = procesar_cadena(texto, saltos)

matriz = probabilidad_de_espacio(matriz)

print(matriz)
