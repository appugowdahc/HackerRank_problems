def check_kaprekar_num(n):

    squared = n ** 2
    
    # Step 2: Convert the squared number to a string
    squared_str = str(squared)
    
    # Step 3: Determine the length of the original number
    num_digits = len(str(n))
    
    # Step 4: Split the string representation of the square
    right_part = squared_str[-num_digits:]
    left_part = squared_str[:-num_digits] if squared_str[:-num_digits] else '0'
    
    # Step 5: Convert the parts back to integers
    left_int = int(left_part)
    right_int = int(right_part)
    
    # Step 6: Check if their sum equals the original number
    return (left_int + right_int) == n
def kaprekarNumbers(p, q):
    res = []
    # Write your code here
    for i in range(p,q+1):
        if check_kaprekar_num(i):
            res.append(i)
    # print(res)
    if len(res) == 0:
        print("INVALID RANGE")
    else:
        print(*res)
kaprekarNumbers(1,100)

