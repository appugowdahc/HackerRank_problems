def countingSort(arr):
    # Write your code here
    count = [ 0]*100
    for i in arr:
        count[i] +=1
    res = []
    for i in range(len(count)):
        j =count[i]
        while j>0:
            res.append(i)
            j -=1
    return res
