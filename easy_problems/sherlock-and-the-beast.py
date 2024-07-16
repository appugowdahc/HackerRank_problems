def find_decent_number(n):
    # Start with the maximum number of 5's that is divisible by 3
    count_of_fives = (n // 3) * 3
    
    while count_of_fives >= 0:
        count_of_threes = n - count_of_fives
        if count_of_threes % 5 == 0:
            # If valid, construct the number and return it
            return '5' * count_of_fives + '3' * count_of_threes
        count_of_fives -= 3
    
    return '-1'


n = 15  
print(find_decent_number(n))

#########################################
def decent_number(n):
    fives = n
    while fives >= 0:
        if fives % 3 == 0 and (n - fives) % 5 == 0:
            return '5' * fives + '3' * (n - fives)
        fives -= 5
    return '-1'


print(decent_number(11))  
print(decent_number(1))  
print(decent_number(3))  
print(decent_number(5))   

##################################
def find_decent_number(n):
    for i in range(n, -1, -5):
        if i % 3 == 0 and (n - i) % 5 == 0:
            return '5' * i + '3' * (n - i)
    return '-1'

# Example usage
n = 11
print(find_decent_number(n))  # Output should be '55555533333'

