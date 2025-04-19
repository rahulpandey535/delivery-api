from itertools import permutations

product_centers = {
    'A': ['C1'], 'B': ['C1'], 'C': ['C1', 'C3'],
    'D': ['C2'], 'E': ['C2'], 'F': ['C2', 'C3'],
    'G': ['C3'], 'H': ['C3'], 'I': ['C3']
}

# Distances between centers and L1
distances_to_l1 = {
    'C1': 10,
    'C2': 30,
    'C3': 33
}

# Distances between centers (assumed symmetric for simplicity)
center_distances = {
    ('C1', 'C2'): 20,
    ('C1', 'C3'): 25,
    ('C2', 'C3'): 15
}
# Add reverse mappings
for (a, b), d in list(center_distances.items()):
    center_distances[(b, a)] = d

COST_PER_KM = 2

def calculate_minimum_delivery_cost(order):
    # Step 1: Find which centers are needed based on the order
    centers_needed = set()

    for product, qty in order.items():
        if qty > 0 and product in product_centers:
            best_center = min(product_centers[product], key=lambda c: distances_to_l1[c])
            centers_needed.add(best_center)

    if not centers_needed:
        return 0

    min_cost = float("inf")

    # Step 2: Try all permutations of centers to find optimal delivery path
    for perm in permutations(centers_needed):
        cost = 0
        route = list(perm) + ['L1']

        for i in range(len(route) - 1):
            from_loc = route[i]
            to_loc = route[i + 1]

            if to_loc == 'L1':
                cost += distances_to_l1[from_loc] * COST_PER_KM
            else:
                cost += center_distances.get((from_loc, to_loc), float("inf")) * COST_PER_KM

        min_cost = min(min_cost, cost)

    return min_cost
