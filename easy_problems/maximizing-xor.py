def maximizingXor(l, r):
    # Write your code here
    res = float('-inf')
    for i in range(l,r+1):
        for j in range(l,r+1):
            val = i ^ j
            res  = max(res,val)
    return res

def maximizingXor(L, R):
    # Calculate the XOR of L and R
    xor_value = L ^ R
    
    # Find the position of the most significant bit
    msb_position = 0
    while xor_value > 0:
        msb_position += 1
        xor_value >>= 1
    
    # Maximum XOR value for the given range
    max_xor = (1 << msb_position) - 1
    
    return max_xor

# Example usage
L = 10
R = 15
print(maximizingXor(L, R))  # Output: 7
