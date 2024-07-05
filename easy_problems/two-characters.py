def alternate(s):
    # Step 1: Get unique characters
    unique_chars = list(set(s))
    
    # Step 2: Initialize max length to 0
    max_length = 0
    
    # Step 3: Generate all possible pairs of unique characters
    for i in range(len(unique_chars)):
        for j in range(i + 1, len(unique_chars)):
            char1 = unique_chars[i]
            char2 = unique_chars[j]
            
            # Step 4: Filter the string to only include the two characters
            filtered = [c for c in s if c == char1 or c == char2]
            
            # Step 5: Check if the filtered string alternates between char1 and char2
            if all(filtered[k] != filtered[k + 1] for k in range(len(filtered) - 1)):
                # Step 6: Update max length if the alternating string is longer
                max_length = max(max_length, len(filtered))
    
    return max_length

# Example usage
s = "beabeefeab"
print(alternate(s))  # Output: 5


def alternate(s):
    # Step 1: Get unique characters
    unique_chars = list(set(s))
    
    # Step 2: Initialize max length to 0
    max_length = 0
    
    # Step 3: Generate all possible pairs of unique characters
    for i in range(len(unique_chars)):
        for j in range(i + 1, len(unique_chars)):
            char1 = unique_chars[i]
            char2 = unique_chars[j]
            
            # Step 4: Iterate through the string and build the filtered string
            filtered = []
            for c in s:
                if c == char1 or c == char2:
                    if filtered and filtered[-1] == c:
                        break
                    filtered.append(c)
            else:
                # Step 5: Update max length if the alternating string is valid
                max_length = max(max_length, len(filtered))
    
    return max_length

# Example usage
s = "beabeefeab"
print(alternate(s))  # Output: 5
