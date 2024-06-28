def minimumDistances(a):
    # Write your code here
    res = []
    for i in range(len(a)-1):
        for j in range(i+1,len(a)):
            if a[i] == a[j]:
                res.append(j-i)
                
    return min(res) if len(res) > 0 else -1

arr = [7,1,2,4,1,5,6,7]
print(minimumDistances(arr))


####################################################


def minimum_distances(arr):
    last_seen = {}
    min_distance = float('inf')
    for i, value in enumerate(arr):
        if value in last_seen:
            distance = i - last_seen[value]
            min_distance = min(min_distance, distance)
        last_seen[value] = i
    
    return min_distance if min_distance != float('inf') else -1

# Example usage
arr = [7, 1, 3, 4, 1, 7]
print(minimum_distances(arr))  # Output: 3
