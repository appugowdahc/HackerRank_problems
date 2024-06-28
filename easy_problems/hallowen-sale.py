def how_many_games(p, d, m, s):
    count = 0  # Number of games bought
    current_price = p  # Initial price of the game

    while s >= current_price:
        s -= current_price
        count += 1
        current_price = max(current_price - d, m)  # Decrease price but not below m

    return count

# Example usage
p = 20  # Initial price of the game
d = 3   # Discount per subsequent game
m = 6   # Minimum price of the game
s = 80  # Total money available

print(how_many_games(p, d, m, s))  # Output: 6
