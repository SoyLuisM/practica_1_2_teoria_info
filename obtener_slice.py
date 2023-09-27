def procesar_cadena(cadena, numero_saltos):
    matriz = []
    
    
    for i in range(numero_saltos, len(cadena)):
        caracter_actual = cadena[i]
        saltos_anteriores = cadena[i - numero_saltos:i]
        contador = 1
        
        # Buscar el caracter actual y saltos anteriores en la matriz
        encontrado = False
        for elemento in matriz:
            if elemento[0] == caracter_actual and elemento[1] == saltos_anteriores:
                # Si lo encontramos, incrementamos el contador
                elemento[2] += 1
                encontrado = True
                break
        
        # Si no encontramos la combinación, la agregamos como una nueva entrada en la matriz
        if not encontrado:
            matriz.append([caracter_actual, saltos_anteriores, contador])
    
    return matriz
