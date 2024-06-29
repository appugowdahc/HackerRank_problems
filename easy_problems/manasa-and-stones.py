def possible_last_stone_values(n, a, b):
    possible_values = set()

    for i in range(n):
        last_stone = i * a + (n - 1 - i) * b
        possible_values.add(last_stone)

    return sorted(possible_values)

# Example usage
n = 4  # Number of stones
a = 10  # First possible difference
b = 100  # Second possible difference

print(possible_last_stone_values(n, a, b))  # Output: [30, 120, 210, 300]
########################brute force#############
def brute_force_last_stone_values(n, a, b):
    possible_values = set()

    # Iterate over all combinations of a and b
    for i in range(n):
        for j in range(n - i - 1, n):
            value = i * a + j * b
            possible_values.add(value)

    return sorted(possible_values)

# Example usage
n = 4  # Number of stones
a = 10  # First possible difference
b = 100  # Second possible difference

print(brute_force_last_stone_values(n, a, b))
