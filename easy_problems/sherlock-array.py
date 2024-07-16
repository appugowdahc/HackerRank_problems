def balancedSums(arr):
    # Write your code here
    summ  = sum(arr)
    left = 0
    for i in range(len(arr)):
        val = summ - (left+arr[i])
        if val == left:
            return "YES"
        left += arr[i]
    return "NO"

arr = [1,2,3,3]
print(balancedSums(arr))