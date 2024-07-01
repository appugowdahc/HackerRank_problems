def strange_counter(t):
    cycle_start = 1
    cycle_length = 3

    # Find the cycle in which t falls
    while t >= cycle_start + cycle_length:
        cycle_start += cycle_length
        cycle_length *= 2

    # Calculate the counter value at time t
    counter_value = cycle_length - (t - cycle_start)
    return counter_value

# Example usage
time = 10
print(strange_counter(time))  # Output: 12
