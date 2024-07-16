def gridChallenge(grid):
    # Write your code here
    sorted_grid = [''.join(sorted(row)) for row in grid]
    for i in range(len(grid[0])):
        for j in range(1,len(grid)):
            if ord(sorted_grid[j][i]) < ord(sorted_grid[j-1][i]):
                # print(f"the ascii values for {grid[j][i]} is {ord(grid[j][i])} the ascii values for {grid[j-1][i]} {ord(grid[j-1][i])}")
                return "NO"
                
    return "YES"

grid = ['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv']
print(gridChallenge(grid))
#########################################

def grid_challenge(grid):
    # Step 1: Sort each row
    sorted_grid = [''.join(sorted(row)) for row in grid]

    # Step 2: Check each column
    n = len(sorted_grid)
    for col in range(len(sorted_grid[0])):
        for row in range(1, n):
            if sorted_grid[row][col] < sorted_grid[row - 1][col]:
                return "NO"
    return "YES"


grid = ["cba", "daf", "ghi"]
print(grid_challenge(grid))  

grid = ["abc", "ade", "efg"]
print(grid_challenge(grid)) 
