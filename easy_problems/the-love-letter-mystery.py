def theLoveLetterMystery(s):
    n = len(s)
    operations = 0
    
    for i in range(n // 2):
        left_char = s[i]
        right_char = s[n - 1 - i]
        if left_char != right_char:
            operations += abs(ord(left_char) - ord(right_char))
    
    return operations

# Example usage:
s = "abc"
result = theLoveLetterMystery(s)
print(result)  # Output: 2 (change 'c' to 'a' or 'b' to 'c')

s = "abcd"
result = theLoveLetterMystery(s)
print(result)  # Output: 4 (change 'd' to 'a' and 'c' to 'b')
