def super_reduced_string(s):
    stack = []

    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)

    result = ''.join(stack)
    print(result)
    return result if result else "Empty String"

# Example usage
s = "ararabccddd"
print(super_reduced_string(s))  # Output: "abd"
