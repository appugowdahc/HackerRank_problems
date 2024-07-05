def alternatingCharacters(s):
    # Write your code here
    d = 0
    for i in range(1,len(s)):
        if s[i] ==s[i-1]:
            d += 1
    return d

"""
5
AAAA
BBBBB
ABABABAB
BABABA
AAABBB
"""