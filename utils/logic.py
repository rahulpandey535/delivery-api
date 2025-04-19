from itertools import permutations, product

product_centers = {
    'A': ['C1'], 'B': ['C1'], 'C': ['C1', 'C3'],
    'D': ['C2'], 'E': ['C2'], 'F': ['C2', 'C3'],
    'G': ['C3'], 'H': ['C3'], 'I': ['C3']
}

# Distance from centers to L1
distances_to_l1 = {
    'C1': 10,
    'C2': 30,
    'C3': 33
}

# Distance between centers (bidirectional)
center_distances = {
    ('C1', 'C2'): 20,
    ('C1', 'C3'): 25,
    ('C2', 'C3'): 15
}
# Add reverse
for (a, b), d in list(center_distances.items()):
    center_distances[(b, a)] = d

COST_PER_KM = 2

def calculate_minimum_delivery_cost(order):
    centers_needed = set()

    # Step 1: Determine which centers to visit based on products
    for product, qty in order.items():
        if qty > 0 and product in product_centers:
            best_center = min(product_centers[product], key=lambda c: distances_to_l1[c])
            centers_needed.add(best_center)

    if not centers_needed:
        return 0

    min_cost = float("inf")

    # Step 2: Try all permutations of visiting centers
    for perm in permutations(centers_needed):
        n = len(perm)

        # Step 3: Try all combinations of when to drop at L1
        for drop_pattern in product([False, True], repeat=n):
            route = []

            for i in range(n):
                route.append(perm[i])
                if drop_pattern[i]:
                    route.append("L1")

            if route[-1] != "L1":
                route.append("L1")

            # Step 4: Calculate cost of this route
            cost = 0
            for i in range(len(route) - 1):
                src = route[i]
                dest = route[i + 1]

                if src in distances_to_l1 and dest == "L1":
                    cost += distances_to_l1[src] * COST_PER_KM
                elif src == "L1" and dest in distances_to_l1:
                    cost += distances_to_l1[dest] * COST_PER_KM
                elif src in distances_to_l1 and dest in distances_to_l1:
                    cost += center_distances.get((src, dest), float("inf")) * COST_PER_KM
                else:
                    cost = float("inf")
                    break

            min_cost = min(min_cost, cost)

    return min_cost
