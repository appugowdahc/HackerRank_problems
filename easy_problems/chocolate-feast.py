def chocolateFeast(n, c, m):
    # Write your code here
    #calculate how bars can buy from given n ruppes by c each bar rupee
    chocolates = n//c
    
    #chocolate bar wrapper you have, initially you will bought_bar wrapper that why you have same bought_bar wrapper
    wrappers = chocolates
    
    #how many bars you have bought and eat
    count = chocolates
    #run loop until you have enough wrappers buy chocolate bars; m is numbers of wrappers per chocolate(if you m wrappers you will get one bar)
    while wrappers >= m:
        #calculate how many bars you can take by remaining wrappers
        get_chocolate_by_wrappers = wrappers//m
        #add chocolate bars to total
        count += get_chocolate_by_wrappers
        #add wrappers that you have after eating offer choccolate bar
        wrappers = wrappers%m + get_chocolate_by_wrappers
    return count


###########################################
def chocolateFeast(n, c, m):
    # Calculate initial chocolates Bobby can buy
    chocolates = n // c
    wrappers = chocolates
    
    # Simulate the wrapper exchange process
    while wrappers >= m:
        # Exchange wrappers for new chocolates
        new_chocolates = wrappers // m
        chocolates += new_chocolates
        
        # Update the number of wrappers
        wrappers = wrappers % m + new_chocolates
    
    return chocolates

# Example usage
n = 15  # Total money Bobby has
c = 3   # Cost of each chocolate
m = 2   # Number of wrappers to exchange for one chocolate

print(chocolateFeast(n, c, m))  # Output: 9


