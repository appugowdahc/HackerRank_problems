def fairRations(loaves):
    total_loaves = 0

    for i in range(len(loaves) - 1):
        if loaves[i] % 2 != 0:
            loaves[i] += 1
            loaves[i + 1] += 1
            total_loaves += 2
            print(i,loaves)

    if loaves[-1] % 2 != 0:
        return "NO"

    return str(total_loaves)


loaves = [ 4, 5, 6,7]  # Example list of loaves
print(fairRations(loaves))  # Output: 4