from collections import Counter

def missing_numbers(arr1, arr2):
    # Count frequencies of each number in both arrays
    count1 = Counter(arr1)
    count2 = Counter(arr2)
    
    # Find missing numbers
    missing = []
    for num in count2:
        if count2[num] > count1.get(num, 0):
            missing.append(num)
    
    # Sort the result in ascending order
    missing.sort()
    
    return missing

# Example usage
arr1 = [7, 2, 5, 3, 5, 3]
arr2 = [7, 2, 5, 4, 6, 3, 5, 3]
print(missing_numbers(arr1, arr2)) 
