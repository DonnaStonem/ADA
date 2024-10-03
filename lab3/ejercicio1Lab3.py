import time

# Función para ordenar los arreglos
def sort_array(arr):
    return sorted(arr)

# Función para encontrar la mediana de dos arreglos
def median_arrays(nu1, nu2):
    # Ordenar ambos arreglos si no están ya ordenados
    nu1 = sort_array(nu1)
    nu2 = sort_array(nu2)
    
    merged = sorted(nu1 + nu2) # Fusionar ambos arreglos
  
    total_length = len(merged) # Calcula la longitud total
    
    if total_length % 2 == 1:
        return merged[total_length // 2] # Si la longitud es impar, la mediana es el elemento del medio
    else:

        mid1 = total_length // 2
        mid2 = mid1 - 1
        return (merged[mid1] + merged[mid2]) / 2 # Si la longitud es par, la mediana es el promedio de los dos elementos del medio

# Función principal que mide el tiempo de ejecución
def main():
    # Ejemplos de entrada
    nums1_ex1 = [1, 3]
    nums2_ex1 = [2]
    
    nums1_ex2 = [1, 2]
    nums2_ex2 = [3, 4]

    start_time = time.time() # Medir el tiempo de ejecución

    # Ejemplo 1
    median_ex1 = median_arrays(nums1_ex1, nums2_ex1)

    # Ejemplo 2
    median_ex2 = median_arrays(nums1_ex2, nums2_ex2)

    end_time = time.time()

    execution_time = end_time - start_time # Tiempo total de ejecución

    # Resultados
    print(f"Mediana para ejemplo 1: {median_ex1:.5f}")
    print(f"Mediana para ejemplo 2: {median_ex2:.5f}")
    print(f"Tiempo de ejecución: {execution_time:.5f} segundos")

# Ejecutar el programa principal
main()
