import math

def squares(a, b):
    # Find the smallest integer greater than or equal to the square root of a
    start = math.ceil(math.sqrt(a))
    # Find the largest integer less than or equal to the square root of b
    end = math.floor(math.sqrt(b))
    print(start,end)
    
    # The number of perfect squares in the range [a, b]
    count = max(0, end - start + 1)
    
    return count

# Example usage
a = 3
b = 9
# print(squares(a, b))  # Output: 2 (perfect squares are 4 and 9)

a = 17
b = 24
# print(squares(a, b))  # Output: 0 (no perfect squares in this range)
print(math.floor(math.sqrt(11)))
