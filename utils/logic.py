from itertools import permutations, product

product_centers = {
    'A': ['C1'], 'B': ['C1'], 'C': ['C1', 'C3'],
    'D': ['C2'], 'E': ['C2'], 'F': ['C2', 'C3'],
    'G': ['C3'], 'H': ['C3'], 'I': ['C3']
}

# Distance to L1 from each center
to_l1 = {
    'C1': 10,
    'C2': 30,
    'C3': 33
}

# Distance between centers
between_centers = {
    ('C1', 'C2'): 20,
    ('C1', 'C3'): 25,
    ('C2', 'C3'): 15
}
# Add reverse paths
for (a, b), d in list(between_centers.items()):
    between_centers[(b, a)] = d

COST_PER_KM = 2

def calculate_minimum_delivery_cost(order):
    centers_needed = set()

    for product, qty in order.items():
        if qty > 0:
            available_centers = product_centers.get(product, [])
            chosen_center = min(available_centers, key=lambda c: to_l1[c])
            centers_needed.add(chosen_center)

    if not centers_needed:
        return 0

    min_cost = float('inf')

    for perm in permutations(centers_needed):
        # Try all ways of inserting L1 after 1 or more pickups
        # Ex: C1 → L1 → C3 → L1 or C1 → C3 → L1
        n = len(perm)
        # Generate all drop patterns (where L1 will be dropped after pickup)
        for drop_pattern in product([False, True], repeat=n):
            path = []
            for i in range(n):
                path.append(perm[i])
                if drop_pattern[i]:
                    path.append('L1')
            # Always end with L1 if not already
            if path[-1] != 'L1':
                path.append('L1')

            # Now calculate cost of this route
            cost = 0
            for i in range(len(path) - 1):
                src, dest = path[i], path[i + 1]

                if src in to_l1 and dest == 'L1':
                    cost += to_l1[src] * COST_PER_KM
                elif src == 'L1' and dest in to_l1:
                    cost += to_l1[dest] * COST_PER_KM
                elif src in to_l1 and dest in to_l1:
                    cost += between_centers.get((src, dest), float('inf')) * COST_PER_KM
                else:
                    cost = float('inf')
                    break

            min_cost = min(min_cost, cost)

    return min_cost
