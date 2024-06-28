from collections import Counter

def min_deletions_to_equalize(arr):
    # Count the frequency of each element in the array
    frequency = Counter(arr)
    
    # Find the maximum frequency
    max_frequency = max(frequency.values())
    
    # Calculate the minimum deletions
    min_deletions = len(arr) - max_frequency
    
    return min_deletions

# Example usage
arr = [1, 2, 2, 3]
print(min_deletions_to_equalize(arr))  # Output: 2


def equalizeArray(arr):
    # Write your code here
    arr.sort()
    max_occ = 1
    i = 1
    count = 1
    while i < len(arr):
        if arr[i] == arr[i-1]:
            count += 1
        else:
            max_occ = max(max_occ,count)
            count = 1
        i += 1
    max_occ = max(max_occ,count)
    return len(arr) - max_occ


print(equalizeArray(arr))