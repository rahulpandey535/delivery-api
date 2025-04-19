from itertools import permutations

product_centers = {
    'A': ['C1'], 'B': ['C1'], 'C': ['C1', 'C3'],
    'D': ['C2'], 'E': ['C2'], 'F': ['C2', 'C3'],
    'G': ['C3'], 'H': ['C3'], 'I': ['C3']
}

distances = {
    'C1': 10,
    'C2': 30,
    'C3': 33
}

COST_PER_KM = 2

def calculate_minimum_delivery_cost(order):
    centers_needed = set()
    
    for product, qty in order.items():
        if qty > 0 and product in product_centers:
            # Choose the center with the shortest distance if multiple
            best_center = min(product_centers[product], key=lambda c: distances[c])
            centers_needed.add(best_center)

    if not centers_needed:
        return 0

    min_cost = float('inf')

    for perm in permutations(centers_needed):
        cost = 0
        for center in perm:
            cost += 2 * distances[center] * COST_PER_KM  # round trip
        min_cost = min(min_cost, cost)

    return min_cost
