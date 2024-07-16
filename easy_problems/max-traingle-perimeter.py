def maximum_perimeter_triangle(sticks):
    sticks.sort()
    
    for i in range(len(sticks) - 3, -1, -1):
        if sticks[i] + sticks[i + 1] > sticks[i + 2]:
            return [sticks[i], sticks[i + 1], sticks[i + 2]]
    
    return [-1]


sticks = [3, 9, 2, 15, 3, 8, 5]
result = maximum_perimeter_triangle(sticks)
if result == [-1]:
    print("No non-degenerate triangle can be formed")
else:
    print("The sides of the triangle with maximum perimeter are:", result)
    print("The maximum perimeter is:", sum(result))


######################################
def max_perimeter_triangle(sides):
    # Sort the sides in descending order
    sides.sort(reverse=True)
    
    # Traverse the sorted list to find the first valid triangle
    for i in range(len(sides) - 2):
        if sides[i] < sides[i+1] + sides[i+2]:
            return sides[i] + sides[i+1] + sides[i+2]
    
    return 0  # If no valid triangle is found


sides = [10, 21, 22, 100, 101, 200, 300]
print(max_perimeter_triangle(sides))  
