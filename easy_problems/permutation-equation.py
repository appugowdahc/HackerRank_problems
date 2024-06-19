"""
To solve this problem, we need to find a sequence of values 
�
(
�
)
p(k) for each 
�
k where 
1
≤
�
≤
�
1≤k≤n, such that 
1
≤
�
(
�
)
≤
�
1≤p(k)≤n and store the history of these values in a return array. The input sequence is such that every element is distinct and satisfies 
1
≤
�
�
≤
�
1≤a 
i
​
 ≤n.

Here's how we can approach the problem step by step:

Initialize the Output Array:

Create an output array result of size 
�
n to store the history of 
�
(
�
)
p(k).
Map Elements to Their Indices:

Create a dictionary index_map where the keys are the elements of the array a and the values are their respective indices. This will help us quickly find the index of any element in the array.
Generate the Output Sequence:

For each 
�
k from 1 to 
�
n:
Find the element 
�
k in the array a using the index_map.
The position of 
�
k in the array a gives us the value of 
�
(
�
)
p(k).
Return the Result:

Store the values of 
�
(
�
)
p(k) in the result array and return it.

"""

def find_p_values(a):
    n = len(a)
    result = [0] * n
    
    # Create a map from elements to their indices
    index_map = {a[i]: i+1 for i in range(n)}
    
    # Generate the sequence p(k)
    for k in range(1, n+1):
        result[k-1] = index_map[k]
    
    return result

# Example usage:
a = [2, 3, 1]
print(find_p_values(a))  # Output: [3, 1, 2]

a = [4, 2, 1, 3]
print(find_p_values(a))  # Output: [3, 2, 4, 1]