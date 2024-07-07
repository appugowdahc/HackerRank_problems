def stringConstruction(s):
    # Write your code here
    res = 0
    p = ""
    for i in s:
        if i not in p:
            res+=1
            p+= i
            
    return res

s = "abcd"
print(stringConstruction(s))

########################################
def min_cost_to_copy(P):
    n = len(P)
    dp = [0] * (n + 1)
    dp[1] = 1

    for i in range(2, n + 1):
        # Start by assuming we append the i-th character individually
        dp[i] = dp[i - 1] + 1
        for j in range(1, i):
            # Check if substring P[j:i] can be appended at no cost
            if P[:i-j] == P[j:i]:
                dp[i] = min(dp[i], dp[j])

    return dp[n]

# Example usage:
P = "abcdabc"
print(min_cost_to_copy(P))  # Output: 4 (a,b,c,d, then append "abc" at no cost)

P = "abcabc"
print(min_cost_to_copy(P))  # Output: 3 (a,b,c, then append "abc" at no cost)

P = "a"
print(min_cost_to_copy(P))  # Output: 1 (only one character)

##########################################################