from time import time

class Item:
    def __init__(self, profit, weight):
        self.profit = profit
        self.weight = weight

def cmp(item):
    # Retorna la relación beneficio/peso para ordenar los artículos
    return item.profit / item.weight

def fractional_knapsack(W, items):
    # Ordena los artículos por beneficio/peso en orden descendente
    items.sort(key=cmp, reverse=True)
    
    final_value = 0.0
    for item in items:
        if item.weight <= W:
            W -= item.weight
            final_value += item.profit
        else:
            final_value += item.profit * (W / item.weight)
            break
    return final_value

# Lista de artículos
items = [
    Item(100, 10), Item(280, 40), Item(120, 20), Item(120, 24), Item(100, 36),
    Item(150, 30), Item(180, 50), Item(40, 10), Item(60, 20), Item(90, 35),
    Item(200, 25), Item(300, 29), Item(90, 24), Item(40, 5), Item(30, 6),
    Item(10, 4), Item(70, 20), Item(80, 10), Item(50, 15), Item(110, 22)
]

# Capacidades de la mochila
capacities = [50, 80]

for W in capacities:
    start = time()
    max_profit = fractional_knapsack(W, items)
    end = time()
    duration = end - start
    print(f"Para W = {W}, máximo beneficio = {max_profit:.2f}, tiempo de ejecución = {duration:.6f} segundos")
