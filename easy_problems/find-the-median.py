def findMedian(arr):
    # Write your code here
    l = len(arr)
    mid = l//2 if l%2 == 0 else (l//2)
    arr.sort()
    return arr[mid]

arr = [4,2,5,6,8,1]
print(findMedian(arr))