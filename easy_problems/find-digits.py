
# find the number of digits that can be a devisor of n
def findDigits(n):
    # Write your code here
    res = 0
    a = n
    while a >0:
        #get last digit of n
        rem = a%10
        # handle zero value for avoiding error and check if rem is devisor
        if rem != 0 and n%rem == 0:
            res += 1
            
        a =a//10
    return res

n = 10240
print(findDigits(n))