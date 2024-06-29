def find_cavities(map_matrix):
    n = len(map_matrix)
    result = [list(row) for row in map_matrix]  # Create a copy of the map as a list of lists

    for i in range(1, n - 1):
        for j in range(1, n - 1):
            depth = int(map_matrix[i][j])
            if (int(map_matrix[i-1][j]) < depth and
                int(map_matrix[i+1][j]) < depth and
                int(map_matrix[i][j-1]) < depth and
                int(map_matrix[i][j+1]) < depth):
                result[i][j] = 'X'

    return [''.join(row) for row in result]

# Example usage
map_matrix = [
    "1112",
    "1912",
    "1892",
    "1234"
]

modified_map = find_cavities(map_matrix)
for row in modified_map:
    print(row)
