"""
Submissions	Leaderboard	Discussions	Editorial	Topics
Taum is planning to celebrate the birthday of his friend, Diksha. There are two types of gifts that Diksha wants from Taum: one is black and the other is white. To make her happy, Taum has to buy  black gifts and  white gifts.

The cost of each black gift is  units.
The cost of every white gift is  units.
The cost to convert a black gift into white gift or vice versa is  units.
Determine the minimum cost of Diksha's gifts.

"""

def taumBday(b, w, bc, wc, z):
    # Write your code here
    
    #check if black gift price greater than white gift price plus conversion price
    if bc > (wc+z) :
        return ((b+w)*wc+(b*z))
    #check if white gift price greater than black gift price plus conversion price
    elif wc > (bc+z):
        return ((b+w)*bc+(w*z))
    else:
        return (b*bc)+(w*wc)
    
def taum_birthday(B, W, X, Y, Z):
    # Calculate the three possible costs
    cost1 = B * X + W * Y
    cost2 = B * X + W * (X + Z)
    cost3 = B * (Y + Z) + W * Y
    
    # Return the minimum cost
    return min(cost1, cost2, cost3)

# Example usage
B = 10  # Number of black gifts
W = 10  # Number of white gifts
X = 1   # Cost of black gift
Y = 1   # Cost of white gift
Z = 1   # Cost to convert a gift

print(taum_birthday(B, W, X, Y, Z))  # Output: 20

    
