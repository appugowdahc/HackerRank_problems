def can_convert(s, t, k):
    common_length = 0
    
    # Find the length of the common prefix
    for i in range(min(len(s), len(t))):
        if s[i] == t[i]:
            common_length += 1
        else:
            break
    
    # Calculate the number of operations needed
    num_deletes = len(s) - common_length
    num_appends = len(t) - common_length
    total_operations = num_deletes + num_appends
    print(total_operations,k)
    # Check if the transformation is possible with exactly k operations
    if total_operations < k:
        return "Yes"
    # elif (k - total_operations) % 2 == 0:
    #     return "Yes"
    # elif len(s) + len(t) <= k:
    #     return "Yes"
    else:
        return "No"

# Example usage
s = "y"
t = "yu"
k = 2
print(can_convert(s, t, k))  # Output: Yes

# s = "aba"
# t = "aba"
# k = 7
# print(can_convert(s, t, k))  # Output: Yes

# s = "ashley"
# t = "ash"
# k = 2
# print(can_convert(s, t, k))  # Output: No
