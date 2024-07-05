def caesarCipher(s, k):
    # Write your code here
    alpha = "abcdefghijklmnopqrstuvwxyz"
    d = {alpha[i] : i for i in range(len(alpha))}
    res = ""
    for i in range(len(s)):
        if s[i].isalpha():
            s_val = s[i].lower()
            idx = (d[s_val] +k)%26
            val = alpha[idx] if s[i].islower() else alpha[idx].upper()
            res+=val
        else:
            res+=s[i]
    return res
        

s= "middle-Qutz"
k = 2
print(caesarCipher(s,k))

def caesar_cipher(s, k):
    result = []
    k = k % 26  # Ensure the shift is within the range of 0-25

    for char in s:
        if 'a' <= char <= 'z':  # Check if the character is lowercase
            new_char = chr((ord(char) - ord('a') + k) % 26 + ord('a'))
            result.append(new_char)
        elif 'A' <= char <= 'Z':  # Check if the character is uppercase
            new_char = chr((ord(char) - ord('A') + k) % 26 + ord('A'))
            result.append(new_char)
        else:
            result.append(char)  # Non-alphabetic characters remain the same

    return ''.join(result)

# Example usage
s = "middle-Outz"
k = 2
print(caesar_cipher(s, k))  # Output: "okffng-Qwvb"
print(chr(122))
