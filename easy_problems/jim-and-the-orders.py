def jimOrders(orders):
    # Calculate delivery times and associate with original order index
    delivery_times = [(i + 1, order[0] + order[1]) for i, order in enumerate(orders)]

    print(delivery_times)
    # Sort based on delivery times and then by original order index
    delivery_times.sort(key=lambda x: (x[1], x[0]))
    print(delivery_times)
    
    # Extract the customer indices in the order they receive their orders
    return [index for index, _ in delivery_times]

orders = [
    [8, 10], 
    [5,6], 
    [4, 6],[7,9],[9,12],[1,5],[2,10],[10,15],[1,7,[2,1]] 
]
print(jimOrders(orders))


def jimOrders(orders):
    # Calculate the delivery time for each customer and store along with their index
    delivery_times = [(i + 1, orders[i][0] + orders[i][1]) for i in range(len(orders))]
    
    # Manual sorting using a nested loop (Bubble Sort for simplicity)
    n = len(delivery_times)
    for i in range(n):
        for j in range(0, n - i - 1):
            # Compare by delivery time first, then by customer index
            if (delivery_times[j][1] > delivery_times[j + 1][1] or 
                (delivery_times[j][1] == delivery_times[j + 1][1] and delivery_times[j][0] > delivery_times[j + 1][0])):
                # Swap if the current pair is out of order
                delivery_times[j], delivery_times[j + 1] = delivery_times[j + 1], delivery_times[j]

    # Extract and return the sorted customer indices
    result = [customer[0] for customer in delivery_times]
    return result

# Example usage
orders = [
    [1, 3],  # Customer 1: Order number 1, Preparation time 3
    [2, 3],  # Customer 2: Order number 2, Preparation time 3
    [3, 3],  # Customer 3: Order number 3, Preparation time 3
    [4, 1]   # Customer 4: Order number 4, Preparation time 1
]

# print(jimOrders(orders))  # Output: [4, 1, 2, 3]
  
