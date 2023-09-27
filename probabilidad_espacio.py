def probabilidad_de_espacio(matriz):
   
    # Calcular el número de filas de la matriz
    num_filas = len(matriz)
    print(num_filas)
    for fila in matriz:
        columna_3 = fila[2]  # Obtener el valor de la tercera columna
        fila.append(columna_3 / num_filas)  # Agregar el producto como cuarta columna
    
    return matriz