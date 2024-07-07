def twoStrings(s1, s2):
    # Write your code here
    for i in range(len(s1)):
        if s1[i] in s2:
            return "YES"
    return "NO"

s1= 'hello'
s2 = "world"
print(twoStrings(s1,s2))