def contains_hackerrank(s):
    target = "hackerrank"
    target_index = 0
    
    for char in s:
        if char == target[target_index]:
            target_index += 1
        if target_index == len(target):
            return "YES"
    
    return "NO"

# Process multiple queries
def check_queries(queries):
    results = []
    for query in queries:
        result = contains_hackerrank(query)
        results.append(result)
    return results

# Example usage
queries = ["hereiamstackerrank", "hackerworld", "haacckkerrannkk"]
results = check_queries(queries)
for result in results:
    print(result)  # Output: YES, NO, YES


########################################
def hackerrankInString(s):
    # Write your code here
    pattern = "hackerrank"
    pl = len(pattern)
    if len(s) < pl:
        return "NO"
    i = 0
    j= 0
    while j < len(s):
        if s[j] == pattern[i]:
            j += 1
            i += 1
        else:
            j += 1
        if i == pl:
            return "YES"
    return "NO"
    