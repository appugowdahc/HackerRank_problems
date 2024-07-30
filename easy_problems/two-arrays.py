def can_permute_to_satisfy_k(n, k, A, B):
    # Sort A in ascending order
    A.sort()
    # Sort B in descending order
    B.sort(reverse=True)
    
    # Check if A[i] + B[i] >= k for all i
    for i in range(n):
        if A[i] + B[i] < k:
            return "NO"
    
    return "YES"

# Example usage
n = 3
k = 10
A = [2, 1, 3]
B = [7, 8, 9]
print(can_permute_to_satisfy_k(n, k, A, B))  # Output: YES
