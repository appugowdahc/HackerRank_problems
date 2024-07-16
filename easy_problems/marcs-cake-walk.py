def marcsCakewalk(calorie):
    
    # Write your code here
    calorie.sort()
    j = 0
    res = 0
    for i  in range(len(calorie)-1,-1,-1):
        res += (2**j)*calorie[i]
        j += 1
    return res

arr = [5,10,7]
print(marcsCakewalk(arr))

def min_miles_to_walk(calories):
    # Step 1: Sort the calories in descending order
    calories.sort(reverse=True)
    
    total_miles = 0
    
    for i in range(len(calories)):
        total_miles += calories[i] * (2 ** i)
    
    return total_miles

calories = [5, 10, 7]
print(min_miles_to_walk(calories)) 

calories = [1, 3, 2]
print(min_miles_to_walk(calories)) 
