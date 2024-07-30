def nim_game(piles):
    # Calculate the Nim-sum of all piles
    nim_sum = 0
    for stones in piles:
        nim_sum ^= stones
    
    # Determine the winner based on the Nim-sum
    if nim_sum == 0:
        return "Second"  # If Nim-sum is 0, the second player wins
    else:
        return "First"  # If Nim-sum is not 0, the first player wins

# Example usage
piles = [3, 2, 4]
print(nim_game(piles))  # Output: "First"

piles = [1, 1, 1]
print(nim_game(piles))  # Output: "Second"
