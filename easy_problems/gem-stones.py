def gemstones(arr):
    # Initialize a set with all possible minerals 'a' to 'z'
    gemstone_set = set(arr[0])
    
    # Iterate through each rock's minerals
    for minerals in arr:
        # Convert the current rock's minerals into a set
        rock_minerals = set(minerals)
        # Update the gemstone set by taking intersection with the current rock's minerals
        gemstone_set.intersection_update(rock_minerals)
    
    # The size of the gemstone set is the number of types of gemstones
    return len(gemstone_set)

# Example usage:
rocks = ["abcdde", "baccd", "eeabg"]
result = gemstones(rocks)
print(result)  # Output: 2


#######################
def gemstones(arr):
    n = len(arr)  # Number of rocks
    freq = [0] * 26  # Frequency array for 'a' to 'z'
    
    for minerals in arr:
        seen = set()  # Use a set to track minerals seen in current rock
        for mineral in minerals:
            if mineral not in seen:
                idx = ord(mineral) - ord('a')
                freq[idx] += 1
                seen.add(mineral)
    
    gemstone_count = 0
    for count in freq:
        if count == n:
            gemstone_count += 1
    
    return gemstone_count

# Example usage:
rocks = ["abcdde", "baccd", "eeabg"]
result = gemstones(rocks)
print(result)  # Output: 2
