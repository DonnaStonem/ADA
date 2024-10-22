import heapq

def mergeKLists(lists):
    # Min-heap
    heap = []
    
    # Insertar el primer elemento de cada lista en el heap
    for i in range(len(lists)):
        if lists[i]:  # Si la lista no está vacía
            heapq.heappush(heap, (lists[i][0], i, 0))  # (valor, índice de la lista, índice del elemento en la lista)
    
    result = []
    
    # Procesar el heap
    while heap:
        val, list_idx, element_idx = heapq.heappop(heap)
        result.append(val)
        
        # Insertar el siguiente elemento de la misma lista en el heap
        if element_idx + 1 < len(lists[list_idx]):
            next_val = lists[list_idx][element_idx + 1]
            heapq.heappush(heap, (next_val, list_idx, element_idx + 1))
    
    return result

lists = [[1,4,5], [1,3,4], [2,6]]
print(mergeKLists(lists))

lists = []
print(mergeKLists(lists))

lists = [[]]
print(mergeKLists(lists))
