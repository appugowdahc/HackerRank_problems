def lonelyinteger(a):
    # Write your code here
    for i in a:
        if a.count(i) ==1:
            return i
        
        
a = [1,2,1,1,2,3,3,4,5,6,4,5]
print(lonelyinteger(a))




a = [1, 2, 3, 4, 3, 2, 1]
print(lonelyinteger(a)) 
