def count_changed_letters(received_message):
    expected_message = "SOS"
    altered_count = 0
    
    for i in range(len(received_message)):
        if received_message[i] != expected_message[i % 3]:
            altered_count += 1
    
    return altered_count

# Example usage
received_message = "SOSSPSSQSSOR"
print(count_changed_letters(received_message))  # Output: 3

def count_altered_letters(received_signal):
    expected_signal = "SOS"
    altered_count = 0
    
    for i in range(0, len(received_signal), 3):
        for j in range(3):
            if received_signal[i + j] != expected_signal[j]:
                altered_count += 1
                
    return altered_count

# Example usage
received_signal = "SOSSOT"
print(count_altered_letters(received_signal))  # Output: 1
