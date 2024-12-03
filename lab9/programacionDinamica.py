def trianguloPascal(numRows):
    triangle = [[1]]  # La primera fila siempre es [1]
    
    for i in range(1, numRows):
        prev_row = triangle[-1]  # Última fila generada
        new_row = [1]  # Primera posición de cada fila es 1
        
        # Calcular los valores intermedios
        
        for j in range(1, len(prev_row)):
            new_row.append(prev_row[j - 1] + prev_row[j])
        new_row.append(1)  # Última posición de cada fila es 1
        triangle.append(new_row)
    
    return triangle

# Ejemplo de uso
numRows = 5
print(trianguloPascal(numRows))
