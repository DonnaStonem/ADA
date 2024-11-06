def max_area(altura):
    izquierda, derecha = 0, len(altura) - 1
    max_area = 0
    
    while izquierda < derecha:
        # Calcula el área usando la altura mínima entre las dos líneas
        area_actual = (derecha - izquierda) * min(altura[izquierda], altura[derecha])
        # Actualiza el área máxima
        max_area = max(max_area, area_actual)
        
        # Mueve el puntero de la altura menor
        if altura[izquierda] < altura[derecha]:
            izquierda += 1
        else:
            derecha -= 1
            
    return max_area

altura = [1,8,6,2,5,4,8,3,7]
print(max_area(altura))  # Salida esperada: 49
