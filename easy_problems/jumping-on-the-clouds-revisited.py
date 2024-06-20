def cloud_hopping_energy(c, k, E):
    n = len(c)  # Number of clouds
    position = 0  # Starting at the first cloud
    energy = E
    
    while True:
        # Jump to the next cloud
        position = (position + k) % n
        # Reduce energy by 1 unit for the jump
        energy -= 1
        # Reduce additional 2 units if it's a thundercloud
        if c[position] == 1:
            energy -= 2
        # Check if the character has returned to the starting position
        if position == 0:
            break
    
    return energy

# Example usage:
c = [0, 0, 1, 0, 0, 1, 1, 0]
k = 2
E = 100
print(cloud_hopping_energy(c, k, E))  # Output should be 92
