def funnyString(s):
    # Write your code here
    rev = []
    forw = []
    for i in range( 1,len(s)):
        curr = ord(s[i])
        prev = ord(s[i-1])
        diff = abs(curr-prev)
        rev.append(diff)
        curr = ord(s[-i])
        prev = ord(s[-(i+1)])
        forw.append(abs(curr-prev))
    if rev==forw:
        return "Funny"
    return "Not Funny"
n = 10
arr = [

"ovyvzvptyvpvpxyztlrztsrztztqvrxtxuxq",
"holtm",
"uvzxrumuztyqyvpnji",
"tmruzxzuwoskqysxztuvosuyrswrnmtxvzsrqwytzrxpltrwusxupw",
"wxstwxuzuyuvyzrsxysxyuvyqxuxyskqwsyqumqrvopvowqumnvrxpwqpwsrnvrztxrxpvuxunvyzvupvupowvyzvzuzwvsrwv",
"yrzxrxskrtlpwpmtpxvowrxrpxq",
"pryumtuntmovpwvowslj",
"nosklrxrtyuxtmnurzsryuxtywqwqpxts",
"fmpszyvqwxrtvpuwqszvyvotmsxsxuvzyvpwzrpmuxqwtswvytytzsnuxuyrpvtysqoutzurqxury",
"jkmsxzwrxzy",

]
for i in arr:
    print(funnyString(i))
    # break

############################################
def is_funny_string(s):
    # Reverse the string
    r = s[::-1]
    
    # Compute the list of absolute differences for the original and reversed strings
    original_diffs = [abs(ord(s[i]) - ord(s[i - 1])) for i in range(1, len(s))]
    reversed_diffs = [abs(ord(r[i]) - ord(r[i - 1])) for i in range(1, len(r))]
    
    # Compare the lists of differences
    if original_diffs == reversed_diffs:
        return "Funny"
    else:
        return "Not Funny"

# Example usage
strings = ["acxz", "bcxz"]
for s in strings:
    # print(f"{s}: {is_funny_string(s)}")
    pass
