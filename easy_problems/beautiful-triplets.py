def count_beautiful_triplets(arr, d):
    count = 0
    elements = set(arr)
    
    for x in arr:
        if (x + d in elements) and (x + 2 * d in elements):
            count += 1
    
    return count

# Example usage
arr = [1, 2, 4, 5, 7, 8, 10]
d = 3
print(count_beautiful_triplets(arr, d))  # Output: 3

################## brute force approach ####################
def count_beautiful_triplets(arr, d):
    count = 0
    n = len(arr)
    
    for i in range(n):
        for j in range(i + 1, n):
            if arr[j] - arr[i] == d:
                for k in range(j + 1, n):
                    if arr[k] - arr[j] == d:
                        count += 1
    
    return count

# Example usage
arr = [1, 2, 4, 5, 7, 8, 10]
d = 3
print(count_beautiful_triplets(arr, d))  # Output: 3

