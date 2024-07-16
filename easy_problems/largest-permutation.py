def largestPermutation(k, arr):
    n = len(arr)
    if k == 0:
        return arr
    # A dictionary to quickly find the index of each value
    value_index = {value: index for index, value in enumerate(arr)}
    
    for i in range(n):
        if k == 0:
            break
        
        # The value that should be ideally at position i
        ideal_value = n - i
        
        # If the value at position i is already the ideal value, continue
        if arr[i] == ideal_value:
            continue
        
        # Index of the ideal value
        ideal_index = value_index[ideal_value]
        
        # Swap the values
        arr[i], arr[ideal_index] = arr[ideal_index], arr[i]
        
        # Update the indices in the dictionary
        value_index[arr[ideal_index]] = ideal_index
        value_index[arr[i]] = i
        
        # Decrement the number of allowed swaps
        k -= 1
    
    return arr

# Example usage
n = 5
k = 1
arr = [4 ,2 ,3, 5 ,1]
print(largestPermutation(k, arr))  # Output: [5, 2, 3, 1, 4]
