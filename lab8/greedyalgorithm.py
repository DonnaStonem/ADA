def numOfSubarrays(arr, k, threshold):
    target = k * threshold  
    current_sum = sum(arr[:k])  # Suma inicial de la primera ventana
    count = 1 if current_sum >= target else 0  # Verifica si la primera ventana cumple la condición
    
    for i in range(k, len(arr)):
        # Actualiza la suma deslizando la ventana
        current_sum += arr[i] - arr[i - k]
        if current_sum >= target:
            count += 1
    
    return count

print(numOfSubarrays([2, 2, 2, 2, 5, 5, 5, 8], 3, 4))  # Salida: 3
print(numOfSubarrays([11, 13, 17, 23, 29, 31, 7, 5, 2, 3], 3, 5))  # Salida: 6
