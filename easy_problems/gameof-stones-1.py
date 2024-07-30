def game_winner(n):
    # Initialize a dp array where dp[i] is True if the first player can win with i stones
    dp = [False] * (n + 1)
    
    # Base cases
    if n == 0:
        return "Second"
    if n == 1:
        return "Second"
    if n == 2:
        return "First"
    if n == 3:
        return "First"
    if n == 4:
        return "First"
    if n == 5:
        return "First"
    
    # Initialize known results based on base cases
    dp[0] = False  # No stones left, player loses
    dp[1] = False  # One stone left, player loses
    dp[2] = True   # First player takes 2 stones and wins
    dp[3] = True   # First player takes 3 stones and wins
    dp[4] = True   # First player can take 2 stones (leaving 2 stones) or 3 stones (leaving 1 stone) and win
    dp[5] = True   # First player takes 5 stones and wins

    # Fill the dp array for all values from 6 to n
    for i in range(6, n + 1):
        # If removing 2, 3, or 5 stones leaves the opponent in a losing position, current player wins
        if not dp[i - 2] or not dp[i - 3] or not dp[i - 5]:
            dp[i] = True
        else:
            dp[i] = False

    return "First" if dp[n] else "Second"

# Example usage
n = 10
print(game_winner(n))  # Output: "First"

