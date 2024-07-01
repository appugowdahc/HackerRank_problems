"""

Insertion Sort Algorithm

--> Insertion sort is a simple sorting algorithm that works by iteratively inserting 
    each element of an unsorted list into its correct position in a sorted portion of 
    the list. It is a stable sorting algorithm, meaning that elements with equal values 
    maintain their relative order in the sorted output.

--> Insertion sort is like sorting playing cards in your hands. You split the cards 
    into two groups: the sorted cards and the unsorted cards. Then, you pick a card 
    from the unsorted group and put it in the right place in the sorted group.

Insertion Sort Algorithm:

    Insertion sort is a simple sorting algorithm that works by building a sorted array one element at a time. It is considered an ” in-place ” sorting algorithm, meaning it doesn’t require any additional memory space beyond the original array.

Algorithm:
    To achieve insertion sort, follow these steps:

    1. We have to start with second element of the array as first element in the array is assumed to be sorted.
    2. Compare second element with the first element and check if the second element is smaller then swap them.
    3. Move to the third element and compare it with the second element, then the first element and swap as necessary to put it in the correct position among the first three elements.
    4. Continue this process, comparing each element with the ones before it and swapping as needed to place it in the correct position among the sorted elements.
    5. Repeat until the entire array is sorted

"""


def insertion_sort(arr):
    #start from second element of array
    for i in range(1,len(arr)):
        key = arr[i]
        j = i-1
        # keep comparing the key and  elements to left side from ith element, shifting them
        while j>=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        # reach the correct position where element should sit
        arr[j+1] = key

    return arr

arr = [10,9,8.7,6,5,4,3,2]
print(insertion_sort(arr))