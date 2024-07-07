def min_changes_to_make_anagram(s):
    n = len(s)
    if n % 2 != 0:
        return -1  # It's impossible to split s into two equal parts
    
    # Split the string into two equal parts
    s1 = s[:n//2]
    s2 = s[n//2:]
    
    # Count character frequencies in both substrings
    from collections import Counter
    count1 = Counter(s1)
    count2 = Counter(s2)
    
    # Calculate the differences in character counts
    diff = 0
    for char in count1:
        if count1[char] > count2[char]:
            diff += count1[char] - count2[char]
    
    return diff

# Example usage:
s = "aaabbb"
print(min_changes_to_make_anagram(s))  # Output: 3

s = "ab"
print(min_changes_to_make_anagram(s))  # Output: 1

s = "abc"
print(min_changes_to_make_anagram(s))  # Output: -1 (odd length string)
