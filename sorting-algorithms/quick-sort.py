"""

1. Quick Sort Algorithm:-
   QuickSort is a sorting algorithm based on the Divide and Conquer algorithm that picks
   an element as a pivot and partitions the given array around the picked pivot by 
   placing the pivot in its correct position in the sorted array.

2. How does QuickSort work?

   The key process in quickSort is a partition() . The target of partitions is to place 
   the pivot (any element can be chosen to be a pivot) at its correct position in the 
   sorted array and put all smaller elements to the left of the pivot, and all greater 
   elements to the right of the pivot.

Partition is done recursively on each side of the pivot after the pivot is placed in 
its correct position and this finally sorts the array.

3. Choice of Pivot:

  3.1 There are many different choices for picking pivots:-

    a. Always pick the first element as a pivot.
    b. Always pick the last element as a pivot (implemented below)
    c. Pick a random element as a pivot .
    d. Pick the middle as the pivot.
    
4. Partition Algorithm:
    The logic is simple, we start from the leftmost element and keep track of the index
    of smaller (or equal) elements as i . While traversing, if we find a smaller element,
    we swap the current element with arr[i]. Otherwise, we ignore the current element.

"""



# Function to find the partition position
def partition(array, low, high):

    # Choose the rightmost element as pivot
    pivot = array[high]

    # Pointer for greater element
    i = low - 1

    # Traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:

            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1

            # Swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])

    # Swap the pivot element with
    # the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])

    # Return the position from where partition is done
    return i + 1


# Function to perform quicksort
def quicksort(array, low, high):
    if low < high:

        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, low, high)

        # Recursive call on the left of pivot
        quicksort(array, low, pi - 1)

        # Recursive call on the right of pivot
        quicksort(array, pi + 1, high)




array = [10, 7, 8, 9, 1, 5]
N = len(array)

# Function call
quicksort(array, 0, N - 1)
print('Sorted array:')
for x in array:
    print(x, end=" ")


