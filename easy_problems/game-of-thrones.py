from collections import Counter
def gameOfThrones(s):
    # Write your code here
    d = Counter(s)
    odd = True if len(s)%2 != 0 else False
    res = "YES"
    for key,val in d.items():
        if val%2 !=0 and not odd:
            return "NO"
        if val%2 !=0 :
            odd = False
        print(f" d val is {d[key]} odd value is {odd} and key is { key}")
    return "YES"

s = "cdefghmnopqrstuvw"
print(gameOfThrones(s))


################################
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
