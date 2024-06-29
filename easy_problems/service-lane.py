def serviceLane(n, cases,width):
    # Write your code here
    print(n)
    print(cases)
    res = []
    def helper(case,width):
        min_wide = float('inf')
        for i in range(case[0],case[1]+1):
            min_wide = min(min_wide,width[i])
        return min_wide
    for case in cases:
        res.append(helper(case,width))
    return res

n = 8
width = [2, 3, 1, 2, 3, 2, 3, 3]
cases = [(0, 3), (4, 6), (6, 7), (3, 5), (0, 7)]

print(serviceLane(n, width, cases)) 

########################################################################

def serviceLane(n, width, cases):
    results = []
    for case in cases:
        entry, exit = case
        min_width = min(width[entry:exit + 1])
        results.append(min_width)
    return results

# Example usage
n = 8
width = [2, 3, 1, 2, 3, 2, 3, 3]
cases = [(0, 3), (4, 6), (6, 7), (3, 5), (0, 7)]

print(serviceLane(n, width, cases))  # Output: [1, 2, 3, 2, 1]
