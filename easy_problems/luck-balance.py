def luck_balance(k, contests):
    important = []
    unimportant = []
    
    # Separate the contests into important and unimportant
    for luck, importance in contests:
        if importance == 1:
            important.append(luck)
        else:
            unimportant.append(luck)
    
    # Sort important contests by their luck in descending order
    important.sort(reverse=True)
    print(unimportant,"unimp***********")
    print(important,"imp**********")
    # Calculate the initial luck balance from unimportant contests
    luck_balance = sum(unimportant)
    
    # Add luck from the most valuable k important contests
    luck_balance += sum(important[:k])
    print(important[:k],"important[:k]")
    print(important[k:],"important[k:]")
    # Subtract luck from the remaining important contests (those she must win)
    luck_balance -= sum(important[k:])
    
    return luck_balance


k = 3
contests = [[5, 1], [2, 1], [1, 1], [8, 1], [10, 0], [5, 0]]

print(luck_balance(k, contests))
