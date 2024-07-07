def icecreamParlor(m, arr):
    # Write your code here
    d = {}
    for i in range(len(arr)):
        d[arr[i]] = i+1
    for i in range(len(arr)):
        tar = m-arr[i]
        for j in range(i+1,len(arr)):
            if tar == arr[j]:
                return [i+1,j+1]


m = 5
arr = [1,2,4,6,7,3]
print(icecreamParlor(m,arr))

#############################################
def find_flavors(arr, p):
    # Dictionary to store price and its index
    price_dict = {}
    
    for i, price in enumerate(arr):
        complement = p - price
        
        if complement in price_dict:
            # Return the one-based indices of the two flavors
            return price_dict[complement] + 1, i + 1
        
        price_dict[price] = i

# Example usage:
prices = [2, 4, 3, 5, 7]
money = 8
print(find_flavors(prices, money))  # Output: (2, 4) since prices[1] + prices[3] == 4 + 4 == 8
