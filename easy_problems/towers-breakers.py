def tower_breakers(n, m):
    # If the height of the towers is 1, the second player wins since the first player can't make a move.
    if m == 1:
        return 2
    # If there is an even number of towers, the second player can always mirror the first player's moves.
    elif n % 2 == 0:
        return 2
    # If there is an odd number of towers and the height is greater than 1, the first player wins.
    else:
        return 1

# Example usage
n = 3  # Number of towers
m = 2  # Height of towers
print(tower_breakers(n, m))  # Output: 1 (First player wins)
