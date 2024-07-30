def calculate_grundy(n, m):
    # Initialize the Grundy number table
    grundy = [[0] * (m + 1) for _ in range(n + 1)]
    
    # Compute the Grundy numbers for each cell
    for x in range(n + 1):
        for y in range(m + 1):
            # Find Grundy numbers for reachable cells
            moves = []
            if x >= 2 and y + 1 <= m:
                moves.append(grundy[x - 2][y + 1])
            if x >= 1 and y + 2 <= m:
                moves.append(grundy[x - 1][y + 2])
            if x + 1 <= n and y + 2 <= m:
                moves.append(grundy[x + 1][y + 2])
            if x + 2 <= n and y + 1 <= m:
                moves.append(grundy[x + 2][y + 1])
            
            # Compute the minimum excludant (mex)
            mex = 0
            while mex in moves:
                mex += 1
            
            grundy[x][y] = mex
    
    return grundy

def coin_game_winner(n, m, x, y):
    grundy = calculate_grundy(8, 8)
    return "First" if grundy[x][y] != 0 else "Second"

# Example usage
n = 5  # number of rows
m = 5  # number of columns
x = 2  # starting x position
y = 2  # starting y position
print(coin_game_winner(n, m, x, y))  # Output: "First" or "Second" depending on the position
