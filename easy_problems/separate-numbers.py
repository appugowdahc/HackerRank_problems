def is_beautiful_string(s):
    # Try all possible lengths for the first number
    for length in range(1, len(s) // 2 + 1):
        first_num = int(s[:length])
        current_num = first_num
        idx = length
        while idx < len(s):
            next_num = current_num + 1
            next_num_str = str(next_num)
            next_num_len = len(next_num_str)
            if s[idx:idx + next_num_len] == next_num_str:
                current_num = next_num
                idx += next_num_len
            else:
                break
        if idx == len(s):
            return "YES", first_num
    return "NO", None

# Example usage
strings = ["1234", "91011", "99100", "101103"]
for s in strings:
    result, first_number = is_beautiful_string(s)
    if result == "YES":
        print(f"{s} is beautiful, starting with {first_number}")
    else:
        print(f"{s} is not beautiful")
