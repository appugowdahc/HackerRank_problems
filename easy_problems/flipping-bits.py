def flip_bits(n):
    # Flip all bits using the bitwise NOT operator
    flipped = ~n
    # Mask the result to ensure it is treated as a 32-bit unsigned integer
    result = flipped & 0xFFFFFFFF
    return result

# Example usage
n = 2147483647
print(flip_bits(n))  # Output: 2147483648

#############################################################3

def flip_bits_list(numbers):
    return [flip_bits(n) for n in numbers]

# Example usage
numbers = [2147483647, 1, 0]
print(flip_bits_list(numbers))  # Output: [2147483648, 4294967294, 4294967295]
