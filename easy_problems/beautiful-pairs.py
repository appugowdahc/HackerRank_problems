def max_beautiful_pairs(A, B):
    from collections import Counter
    
    # Count frequencies of elements in A and B
    count_A = Counter(A)
    count_B = Counter(B)
    
    # Calculate the initial number of pairwise disjoint beautiful pairs
    common = sum((count_A & count_B).values())
    
    # We can change exactly one element in A
    if common == len(A):
        # If all elements are already matching, we need to break one pair
        return common - 1
    else:
        # Else, we can create one more beautiful pair by changing an element in A
        return common + 1

# Example usage
A = [1, 2, 3, 4]
B = [1, 2, 2, 3]
print(max_beautiful_pairs(A, B))  # Output should be 3
