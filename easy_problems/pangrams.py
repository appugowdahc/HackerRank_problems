def pangrams(s):
    # Write your code here
    s = s.split(' ')
    s = "".join(s)
    s = s.lower()
    val = set(s)
    print(val)
    if len(val) == 26:
        return "pangram"
    else:
        return "not pangram"
s ="We promptly judged antique ivory buckles for the next prize"
print(pangrams(s))

####################################################

def is_pangram(sentence):
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    sentence_set = set(sentence.lower())
    
    if alphabet.issubset(sentence_set):
        return "pangram"
    else:
        return "not pangram"

# Example usage
sentence = "The quick brown fox jumps over the lazy dog"
print(is_pangram(sentence))  # Output: pangram

sentence = "Hello world"
print(is_pangram(sentence))  # Output: not pangram
######################################################
def pangrams(s):
    # Write your code here
    s = s.lower()
    alp = "abcdefghijklmnopqrstuvwxyz"
    for i in alp:
        if i != " " and i not in s:
            print(i)
            return "not pangram"
        
    return "pangram"

##################################################3
def is_pangram(sentence):
    # Convert the sentence to lowercase
    sentence = sentence.lower()
    
    # Initialize an empty set to keep track of the letters
    letters = set()
    
    # Iterate through each character in the sentence
    for char in sentence:
        # Check if the character is a letter
        if 'a' <= char <= 'z':
            letters.add(char)
    
    # Check if the set contains all 26 letters
    if len(letters) == 26:
        return "pangram"
    else:
        return "not pangram"

# Example usage
sentence1 = "The quick brown fox jumps over the lazy dog"
sentence2 = "Hello world"
print(is_pangram(sentence1))  # Output: pangram
print(is_pangram(sentence2))  # Output: not pangram

