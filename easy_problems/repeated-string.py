def repeatedString(s, n):
    # Write your code here
    #if s is "a" and length is 1 no needd to do anything just return n
    if len(s)==1 and s[0] == 'a':
        return n
    l = len(s)
    res = []
    count = 0
    #first count "a" letter in given string s and keep index of a
    for i in range(l):
        if s[i] == 'a':
            count += 1
            res.append(i)
    #find how many time "a" will be there in give "n" string length 
    total = (n//l)*count
    for j in range(n%l):
        if j in res:
            print(j)
            total += 1
    return  total

# Example usage
s = "abcac"
n = 10
print(repeatedString(s, n))  

def count_as_in_infinite_string(s, n):
    L = len(s)
    full_repeats = n // L
    remainder = n % L

    # Count 'a's in the full string s
    count_a_in_full_s = s.count('a')

    # Count 'a's in the remaining part
    count_a_in_remainder = s[:remainder].count('a')

    # Total 'a's is the sum of 'a's from full repeats and remainder part
    total_as = full_repeats * count_a_in_full_s + count_a_in_remainder
    
    return total_as

s = "abcac"
n = 10
print(count_as_in_infinite_string(s, n)) 
