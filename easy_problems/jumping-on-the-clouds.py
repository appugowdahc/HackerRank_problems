def jumpingOnClouds(c):
    # Write your code here
    l = len(c)
    i = 0
    count_jump = 0
    
    while True:
        #check if it possible to jump cumulus cloud(it should have value zero) to seconf cloud
        if i+2 <l and c[i+2] == 0:
            i+= 2
        else:
            i += 1
        count_jump += 1

        if i == l-1:
            break
        
    return count_jump


def min_jumps_to_win(clouds):
    n = len(clouds)
    current_position = 0
    jumps = 0

    while current_position < n - 1:
        if current_position + 2 < n and clouds[current_position + 2] == 0:
            current_position += 2
        else:
            current_position += 1
        jumps += 1

    return jumps

# Example usage
clouds = [0, 1, 0, 0, 0, 1, 0]
print(min_jumps_to_win(clouds))  # Output: 3
