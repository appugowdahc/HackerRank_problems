def non_divisible_subset(k, s):
    # Create a list to count remainders
    remainder_count = [0] * k
    
    # Count occurrences of each remainder
    for num in s:
        remainder_count[num % k] += 1
    
    # Start with min(remainder_count[0], 1) to handle the zero remainder case
    count = min(remainder_count[0], 1)
    
    # Loop through possible remainders and handle pairs
    for i in range(1, (k // 2) + 1):
        if i != k - i:
            count += max(remainder_count[i], remainder_count[k - i])
        else:
            # When i == k - i (which is possible only if k is even)
            count += min(remainder_count[i], 1)
    
    return count

# Example usage
k = 3
s = [1, 7, 2, 4]
print(non_divisible_subset(k, s))  # Output: 3

k = 4
s = [19, 10, 12, 10, 24, 25, 22]
print(non_divisible_subset(k, s))  # Output: 3
