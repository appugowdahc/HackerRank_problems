def sumXor(n):
    # Write your code here
    count = 0
    for i in range(n+1):
        if n+i == n^i:
            count +=1 
    return count 

n= 10
# print(sumXor(n))

def count_ys(x):
    # Count the number of zero bits in the binary representation of x
    zero_bits = 0
    while x > 0:
        
        if (x & 1) == 0:
            # print(x)
            zero_bits += 1
        x >>= 1
    
    # The number of y values satisfying the condition is 2^zero_bits
    return 2 ** zero_bits


x = 5  
print(count_ys(x)) 
