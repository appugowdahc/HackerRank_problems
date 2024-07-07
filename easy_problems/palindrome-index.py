def is_palindrome(s):
    return s == s[::-1]

def palindrome_index(s):
    if is_palindrome(s):
        return -1
    
    n = len(s)
    for i in range(n // 2):
        if s[i] != s[n - 1 - i]:
            if is_palindrome(s[i+1:n-i]):
                return i
            elif is_palindrome(s[i:n-1-i]):
                return n - 1 - i
            else:
                return -1
    return -1

# Example usage:
s = "abca"
result = palindrome_index(s)
print(result)  # Output: 1 (removing 'b' makes it "aca")

s = "racecar"
result = palindrome_index(s)
print(result)  # Output: -1 (it's already a palindrome)
