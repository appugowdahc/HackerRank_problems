from collections import Counter

def can_be_palindrome(s):
    # Count character frequencies
    count = Counter(s)
    
    # Check the number of characters with odd frequencies
    odd_count = sum(1 for freq in count.values() if freq % 2 != 0)
    
    # A string can be rearranged into a palindrome if at most one character has an odd frequency
    if odd_count > 1:
        return "NO"
    else:
        return "YES"

# Example usage:
print(can_be_palindrome("aabb"))  # Output: "YES"
print(can_be_palindrome("abc"))   # Output: "NO"
print(can_be_palindrome("aaabbbb")) # Output: "YES"
print(can_be_palindrome("cdefghmnopqrstuvw")) # Output: "NO"