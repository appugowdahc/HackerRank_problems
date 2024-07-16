def min_containers(weights):
    weights.sort()  # Step 1: Sort the weights
    num_containers = 0
    i = 0
    n = len(weights)
    
    while i < n:
        num_containers += 1  # Step 2: Start a new container
        min_weight = weights[i]
        
        # Step 3: Pack items into the current container
        while i < n and weights[i] <= min_weight + 4:
            i += 1
    
    return num_containers

# Example usage
weights = [1, 2, 3, 21, 22, 23, 24, 25]
print(min_containers(weights))  # Output should be 4
