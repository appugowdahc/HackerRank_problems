def cutTheSticks(arr):
    # Write your code here
    
    res = []    
    arr1 = arr
    next_arr = []
    while len(arr1) > 1:
        res.append(len(arr1))
        minn = min(arr1)
        for i in arr1:
            val = i-minn
            if val >0:
                next_arr.append(val)
        arr1 =next_arr

        next_arr = []
    if len(arr1) >0:
        res.append(1)
    return res

def cut_sticks(arr):
    # Sort the array to handle the sticks in ascending order
    arr.sort()
    
    # Initialize the result list
    result = []
    
    # Previous length to track the current position in the sorted array
    previous_length = 0
    n = len(arr)
    
    for i in range(n):
        # If the current stick length is different from the previous stick length
        if arr[i] != previous_length:
            # Append the number of remaining sticks
            result.append(n - i)
            previous_length = arr[i]
    
    return result
            

arr = [1,13, 3, 8, 14, 9, 4, 4]
print(cutTheSticks(arr))