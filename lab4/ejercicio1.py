import random
import math
import time

# Función para generar n puntos aleatorios en 2D
def generar_puntos(n):
    puntos = [(random.uniform(-100, 100), random.uniform(-100, 100)) for _ in range(n)]
    return puntos

# Función para calcular la distancia euclidiana entre dos puntos
def distancia_euclidiana(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Función para encontrar los dos puntos más cercanos
def puntos_mas_cercanos(puntos):
    min_dist = float('inf')
    punto1, punto2 = None, None
    n = len(puntos)
    
    for i in range(n):
        for j in range(i + 1, n):
            dist = distancia_euclidiana(puntos[i], puntos[j])
            if dist < min_dist:
                min_dist = dist
                punto1, punto2 = puntos[i], puntos[j]
    
    return punto1, punto2, min_dist

# Función para medir el tiempo de ejecución
def medir_tiempos(n):
    puntos = generar_puntos(n)
    inicio = time.time()
    punto1, punto2, min_dist = puntos_mas_cercanos(puntos)
    fin = time.time()
    
    print(f"Para n = {n}, los puntos más cercanos son {punto1} y {punto2} con una distancia de {min_dist:.6f}")
    print(f"Tiempo de ejecución: {fin - inicio:.6f} segundos\n")

# Pruebas con diferentes tamaños de n
for n in [10, 100, 1000, 10000, 100000]:
    medir_tiempos(n)
