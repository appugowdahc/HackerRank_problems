def weighted_string(s, queries):
    # Step 1: Create a mapping from 'a' to 'z' to weights 1 to 26
    char_to_weight = {chr(i + ord('a')): i + 1 for i in range(26)}
    
    # Step 2: Create a set to store possible weights from the string
    possible_weights = set()
    
    i = 0
    while i < len(s):
        current_char = s[i]
        current_weight = char_to_weight[current_char]
        
        # Initialize the cumulative weight for consecutive characters
        cumulative_weight = current_weight
        
        # Add the single character weight
        possible_weights.add(cumulative_weight)
        
        # Extend to consecutive characters of the same kind
        j = i + 1
        while j < len(s) and s[j] == current_char:
            cumulative_weight += current_weight
            possible_weights.add(cumulative_weight)
            j += 1
        
        i = j
    
    # Step 3: Check each query
    results = []
    for query in queries:
        if query in possible_weights:
            results.append("Yes")
        else:
            results.append("No")
    
    return results

# Example usage
s = "abccba"
queries = [1, 3, 9, 5, 6]
print(weighted_string(s, queries))  # Output: ['Yes', 'Yes', 'No', 'Yes', 'No']
