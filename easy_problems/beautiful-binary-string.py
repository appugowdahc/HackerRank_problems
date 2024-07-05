def beautifulBinaryString(b):
    count = 0
    i = 0
    while i <= len(b) - 3:
        if b[i:i+3] == "010":
            count += 1
            i += 3  # Move past this occurrence of "010"
        else:
            i += 1
    return count

# Example usage:
binary_string = "0101010"
result = beautifulBinaryString(binary_string)
print(result)  # Output: 2
