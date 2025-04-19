from itertools import permutations, product

product_centers = {
    'A': ['C1'], 'B': ['C1'], 'C': ['C1', 'C3'],
    'D': ['C2'], 'E': ['C2'], 'F': ['C2', 'C3'],
    'G': ['C3'], 'H': ['C3'], 'I': ['C3']
}

distances_to_l1 = {
    'C1': 10,
    'C2': 30,
    'C3': 33
}

center_distances = {
    ('C1', 'C2'): 20,
    ('C1', 'C3'): 25,
    ('C2', 'C3'): 15
}
for (a, b), d in list(center_distances.items()):
    center_distances[(b, a)] = d

COST_PER_KM = 2

def calculate_minimum_delivery_cost(order):
    centers_needed = set()

    for product, qty in order.items():
        if qty > 0 and product in product_centers:
            best_center = min(product_centers[product], key=lambda c: distances_to_l1[c])
            centers_needed.add(best_center)

    if not centers_needed:
        return 0

    min_cost = float('inf')

    # Build all permutations of center visit orders
    for perm in permutations(centers_needed):
        # Now for each permutation, try adding L1 in different places
        for drop_pattern in product([True, False], repeat=len(perm)):
            cost = 0
            route = []
            for i, center in enumerate(perm):
                route.append(center)
                if drop_pattern[i]:  # Drop at L1 after this center
                    route.append('L1')

            # Always end with L1 if not already
            if route[-1] != 'L1':
                route.append('L1')

            # Compute total cost of this route
            for i in range(len(route)-1):
                src = route[i]
                dest = route[i+1]

                if src in ['C1', 'C2', 'C3'] and dest == 'L1':
                    cost += distances_to_l1[src] * COST_PER_KM
                elif src in ['C1', 'C2', 'C3'] and dest in ['C1', 'C2', 'C3']:
                    cost += center_distances.get((src, dest), float('inf')) * COST_PER_KM
                elif src == 'L1' and dest in ['C1', 'C2', 'C3']:
                    cost += distances_to_l1[dest] * COST_PER_KM
                else:
                    cost = float('inf')
                    break

            min_cost = min(min_cost, cost)

    return min_cost
