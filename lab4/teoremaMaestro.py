import math
import time

# Función para calcular la distancia euclidiana entre dos puntos
def distancia_euclidiana(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Función auxiliar para encontrar la mínima distancia en una lista de puntos (fuerza bruta)
def distancia_minima_fuerza_bruta(puntos, n):
    min_dist = float('inf')
    for i in range(n):
        for j in range(i + 1, n):
            dist = distancia_euclidiana(puntos[i], puntos[j])
            if dist < min_dist:
                min_dist = dist
    return min_dist

# Función para encontrar la mínima distancia en el strip
def distancia_en_strip(strip, size, d):
    min_dist = d
    # Ordenar el strip por coordenada Y
    strip.sort(key=lambda punto: punto[1])
    for i in range(size):
        j = i + 1
        while j < size and (strip[j][1] - strip[i][1]) < min_dist:
            dist = distancia_euclidiana(strip[i], strip[j])
            if dist < min_dist:
                min_dist = dist
            j += 1
    return min_dist

# Función recursiva que implementa la solución de división y conquista
def distancia_minima_recursiva(puntos_x, puntos_y, n):
    # Caso base: si hay menos de 4 puntos, usar la fuerza bruta
    if n <= 3:
        return distancia_minima_fuerza_bruta(puntos_x, n)
    
    # Encuentra el punto medio
    mitad = n // 2
    punto_medio = puntos_x[mitad]
    
    # Dividir el conjunto en dos mitades
    puntos_y_izq = []
    puntos_y_der = []
    for punto in puntos_y:
        if punto[0] <= punto_medio[0]:
            puntos_y_izq.append(punto)
        else:
            puntos_y_der.append(punto)
    
    # Distancia mínima en las mitades izquierda y derecha
    dist_izq = distancia_minima_recursiva(puntos_x[:mitad], puntos_y_izq, mitad)
    dist_der = distancia_minima_recursiva(puntos_x[mitad:], puntos_y_der, n - mitad)
    
    # Distancia mínima de ambas mitades
    dist_min = min(dist_izq, dist_der)
    
    # Crear el strip con los puntos cercanos a la línea divisoria
    strip = [punto for punto in puntos_y if abs(punto[0] - punto_medio[0]) < dist_min]
    
    # Encontrar la mínima distancia en el strip
    return min(dist_min, distancia_en_strip(strip, len(strip), dist_min))

# Función principal para encontrar la mínima distancia
def distancia_minima(puntos, n):
    puntos_x = sorted(puntos, key=lambda punto: punto[0])
    puntos_y = sorted(puntos, key=lambda punto: punto[1])
    return distancia_minima_recursiva(puntos_x, puntos_y, n)

# Función para generar puntos aleatorios
import random
def generar_puntos(n):
    return [(random.uniform(-100, 100), random.uniform(-100, 100)) for _ in range(n)]

# Función para medir los tiempos de ejecución
def medir_tiempos(n):
    puntos = generar_puntos(n)
    inicio = time.time()
    min_dist = distancia_minima(puntos, n)
    fin = time.time()
    
    print(f"Para n = {n}, la distancia mínima es {min_dist:.6f}")
    print(f"Tiempo de ejecución: {fin - inicio:.6f} segundos\n")

# Pruebas con diferentes tamaños de n
for n in [10, 100, 1000, 10000, 100000]:
    medir_tiempos(n)
