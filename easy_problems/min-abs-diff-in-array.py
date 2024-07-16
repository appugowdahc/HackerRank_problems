def minimumAbsoluteDifference(arr):
    # Write your code here
    arr.sort()
    minn = float('inf')
    for i in range(1,len(arr)):
        minn = min(minn,abs(arr[i]-arr[i-1]))
    return minn


arr = [-59, -36 ,-13, 1, -53, -92, -2 ,-96 ,-54, 75]
print(minimumAbsoluteDifference(arr))