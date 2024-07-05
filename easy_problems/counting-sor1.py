def countingSort(arr):
    # Write your code here

    res  = [0] *(100)
    for i in arr:
        print(i)
        res[i] = res[i] +1
    return res

arr = [1, 4, 1, 2, 7, 5, 2, 99, 99, 3, 3, 3, 0]
print(countingSort(arr))