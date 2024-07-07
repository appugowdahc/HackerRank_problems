def closestNumbers(arr):
    # Write your code here
    min = float('inf')
    res = []
    d = {}
    arr.sort()
    for i in range(1,len(arr)):
        key_diff = arr[i]-arr[i-1]
        print(key_diff,"****************************")
        if key_diff in d:
            d[key_diff].append(arr[i])
            d[key_diff].append(arr[i-1])
            # print(d)
        else:
            d[key_diff] = [arr[i],arr[i-1]]

    print(d,"*********************")
    minn = min(list(d.keys()))
    return d[minn]


arr = [-20, -3916237 ,-357920 ,-3620601, 7374819 ,-7330761, 30, 6246457, -6461594, 266854]
print(closestNumbers(arr))



#################################
def closestNumbers(arr):
    arr.sort()
    min_diff = float('inf')
    result = []
    
    for i in range(len(arr) - 1):
        diff = arr[i + 1] - arr[i]
        if diff < min_diff:
            min_diff = diff
            result = [(arr[i], arr[i + 1])]
        elif diff == min_diff:
            result.append((arr[i], arr[i + 1]))
    
    # Flatten the list of tuples for the final result
    final_result = [num for pair in result for num in pair]
    return final_result

# Example usage
arr = [4, 2, 1, 3]
print(closestNumbers(arr))
