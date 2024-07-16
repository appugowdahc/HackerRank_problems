def maximumToys(prices, k):
    # Write your code here
    prices.sort()
    res = 0
    count = 0
    for i in prices:
        res+=i
        if res >k:
            return count 
        count += 1
    return count


def maximumToys(prices, k):
    prices.sort()
    
    count = 0
    total_spent = 0
    
    for price in prices:
        if total_spent + price <= k:
            total_spent += price
            count += 1
        else:
            break
    
    return count

prices = [1, 12, 5, 111, 200, 1000, 10]
k = 50
print(maximumToys(prices, k))  
